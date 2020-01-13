import sys
import os
import settings
import math
import logging
from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from PatternListener import PatternListener
from RepositoryData import Repository

csv_delimiter = ','


def configure_log_settings():
    """[this method is primarily used to configure all log relating settings - default log level is INFO]
    """
    logging.basicConfig(level=logging.INFO, filename='analysing_repositories_antlr4.log',
                        filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def check_for_new_iteration():
    """[this method validates whether the current itertion is a new mining process
       or a continuation of an existing mining process]

    Returns:
        [boolean, list] -- [True - new mining process/False- old
                            , holds the list of repository names which are already processed ]
    """
    repo_done_name_list = []
    with open('repo_names_done.txt', 'r') as f:
        for line in f:
            repo_done_name_list.append(line.strip())

    if len(repo_done_name_list) == 0:
        return True, repo_done_name_list
    else:
        return False, repo_done_name_list


def get_all_repo_names():
    """[this method fetchesall the repository names]

    Returns:
        [list] -- [holds the list of all repository names]
    """
    repo_name_list = []
    with open('repo_names.txt', 'r') as f:
        for line in f:
            repo_name_list.append(line.strip())

    return repo_name_list


def get_pattern_list_data():
    """[this method finds all the count of listener and visitor classes]

    Returns:
        [int, int] -- [listener class counts, visitor class counts]
    """
    listener_cnt = 0
    visitor_cnt = 0
    for row in settings.extended_class_list:
        if 'Listener' in row:
            listener_cnt += 1
        elif 'Visitor' in row:
            visitor_cnt += 1

    return listener_cnt, visitor_cnt


def get_method_list_data():
    """[this method gives the counts of all enter, exit and visit method implementation]

    Returns:
        [int, int, int, int] -- [counts of enter, exit, both enter and exit, and visit methods respectively]
    """
    enter_method_cnt = len(settings.method_enter_list)
    exit_method_cnt = len(settings.method_exit_list)
    visit_method_cnt = len(settings.method_visit_list)
    enter_exit_method_cnt = 0

    for exit_method_name in settings.method_exit_list:
        if exit_method_name in settings.method_enter_list:
            enter_exit_method_cnt += 1

    return enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt


def parse_for_methods(repo_path):
    """[this is the main mehtod where the actual antlr4 parsing happens]

    Arguments:
        repo_path {[str]} -- [holds repository path and only used for logging purpose]
    """
    try:
        istream = FileStream(repo_path, encoding='utf-8')
        lexer = JavaLexer(istream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()

        # _using PatternListener to walk only through class and method Declarations
        walker = ParseTreeWalker()
        walker.walk(PatternListener(), tree)

    except Exception as e:
        print("Unexpected error:  " + repo_path + "   " + str(e))


def mine_repositories(repos_path, repo_name):
    """[this method takes repo path, name and tries to mine only java files other than Baselistener and BaseVisitor]

    Arguments:
        repos_path {[str]} -- [holds absolute path of the folder which contains all repositories]
        repo_name {[str]} -- [holds the name of a repository]

    Returns:
        [int, int] -- [returns the count total files and java files in the repository]
    """
    total_file_cnt = 0
    total_java_files = 0
    for subdir, dirs, files in os.walk(os.path.join(repos_path, repo_name)):
        for file in files:
            total_file_cnt += 1
            if file.endswith('.java') and 'BaseListener' not in file and 'BaseVisitor' not in file:
                total_java_files += 1

                # _parse only for method and class declarations in the target java class file
                parse_for_methods(os.path.join(subdir, file))

    return total_file_cnt, total_java_files


def walk_repositories(repos_path, repo_name_list, repo_done_name_list):
    """[this method walk repositories iterates over all the existing repositories and processes them accordingly]

    Arguments:
        repos_path {[str]} -- [holds absolute path of the folder which contains all repositories]
        repo_name_list {[list]} -- [list of all repository names]
        repo_done_name_list {[type]} -- [list of all repository names which are already processed]
    """
    for repo_index, repo_name in enumerate(repo_name_list):

        # _process the repository only if its not processed earlier
        if repo_name not in repo_done_name_list:

            logging.info(
                f'Start processing repository -- {repo_name} with repo id - {repo_index}')

            total_file_cnt = 0
            total_java_files = 0
            listener_pattern_cnt = 0
            visitor_pattern_cnt = 0
            enter_method_cnt = 0
            exit_method_cnt = 0
            enter_exit_method_cnt = 0
            visit_method_cnt = 0
            settings.init()

            # _initialize the repository object with all zero counts
            repository_data = Repository(int(repo_index+1),
                                         repo_name, total_file_cnt, total_java_files, listener_pattern_cnt, visitor_pattern_cnt, enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt)

            total_file_cnt, total_java_files = mine_repositories(
                repos_path, repo_name)

            listener_pattern_cnt, visitor_pattern_cnt = get_pattern_list_data()
            enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt = get_method_list_data()

            # _update all the data points of repository object using respectivev setter methods
            repository_data.total_file_cnt = total_file_cnt
            repository_data.total_java_files = total_java_files
            repository_data.listener_pattern_cnt = listener_pattern_cnt
            repository_data.visitor_pattern_cnt = visitor_pattern_cnt
            repository_data.enter_method_cnt = enter_method_cnt
            repository_data.exit_method_cnt = exit_method_cnt
            repository_data.visit_method_cnt = visit_method_cnt

            # _write repository object data to csv file
            write_to_csv(repository_data, header=False)

            logging.info(
                f'Done processing repository -- {repo_name} with repo id - {repo_index}')


def process_repositories(repo_path):
    """[this method is responsible for getting all repository names and names of repositories which are already processed]

    Arguments:
        repo_path {[str]} -- [holds absolute path of the folder which contains all repositories]
    """
    header_flag, repo_done_name_list = check_for_new_iteration()
    if header_flag:
        write_to_csv(None, header=True)
    repo_name_list = get_all_repo_names()

    # _walk through all the repositories
    walk_repositories(repo_path, repo_name_list, repo_done_name_list)


def write_to_csv(repo_data, header=False):
    filename = 'repository_mining_data'
    filename += '.csv'

    if header is True:
        with open('mining_results/' + filename, 'a') as the_file:
            the_file.write('repo_id' + csv_delimiter
                           + 'repo_name' + csv_delimiter
                           + 'total_file_cnt' + csv_delimiter
                           + 'total_java_files' + csv_delimiter
                           + 'listener_pattern_cnt' + csv_delimiter
                           + 'visitor_pattern_cnt' + csv_delimiter
                           + 'enter_method_cnt' + csv_delimiter
                           + 'exit_method_cnt' + csv_delimiter
                           + 'enter_exit_method_cnt' + csv_delimiter
                           + 'visit_method_cnt' + '\n')

    else:
        with open('mining_results/' + filename, 'a') as the_file:
            the_file.write(repo_data.repo_id + csv_delimiter
                           + repo_data.repo_name + csv_delimiter
                           + repo_data.total_file_cnt + csv_delimiter
                           + repo_data.total_java_files + csv_delimiter
                           + repo_data.listener_pattern_cnt + csv_delimiter
                           + repo_data.visitor_pattern_cnt + csv_delimiter
                           + repo_data.enter_method_cnt + csv_delimiter
                           + repo_data.exit_method_cnt + csv_delimiter
                           + repo_data.enter_exit_method_cnt + csv_delimiter
                           + repo_data.visit_method_cnt + '\n')

        with open('repo_names_done.txt', 'a') as the_file:
            the_file.write(repo_data.repo_name + '\n')


if __name__ == "__main__":
    """[main method is the starting point of the whole processing all the repositories]
    """
    configure_log_settings()
    logging.info(f'Starting Analysing Antlr4   Repositories...')

    # _start porcessing the repositories
    process_repositories(
        sys.argv[1])

    logging.info(f'Finished Analysing Antlr4   Repositories...')
