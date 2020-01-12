import sys
import os
import settings
import math
from antlr4 import *
from JavaLexer import JavaLexer
from JavaParser import JavaParser
from PatternListener import PatternListener
from RepositoryData import Repository
from datetime import datetime

csv_delimiter = ','


def get_pattern_list_data():
    listener_cnt = 0
    visitor_cnt = 0
    for row in settings.extended_class_list:
        if 'Listener' in row:
            listener_cnt += 1
        elif 'Visitor' in row:
            visitor_cnt += 1

    return listener_cnt, visitor_cnt


def get_method_list_data():
    enter_method_cnt = len(settings.method_enter_list)
    exit_method_cnt = len(settings.method_exit_list)
    visit_method_cnt = len(settings.method_visit_list)
    enter_exit_method_cnt = 0

    for exit_method_name in settings.method_exit_list:
        if exit_method_name in settings.method_enter_list:
            enter_exit_method_cnt += 1

    return enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt


def parse_for_methods(repo_path):
    try:
        istream = FileStream(repo_path, encoding='utf-8')
        lexer = JavaLexer(istream)
        stream = CommonTokenStream(lexer)
        parser = JavaParser(stream)
        tree = parser.compilationUnit()

        walker = ParseTreeWalker()
        walker.walk(PatternListener(), tree)

    except Exception as e:
        print("Unexpected error:  " + repo_path + "   " + str(e))


def walk_repositories(repos_path):
    repo_list = []

    repo_dirs = os.listdir(repos_path)
    for repo_index, repo_name in enumerate(repo_dirs):

        total_file_cnt = 0
        total_java_files = 0
        listener_pattern_cnt = 0
        visitor_pattern_cnt = 0
        enter_method_cnt = 0
        exit_method_cnt = 0
        enter_exit_method_cnt = 0
        visit_method_cnt = 0
        settings.init()

        repository_data = Repository(
            repo_name, total_file_cnt, total_java_files, listener_pattern_cnt, visitor_pattern_cnt, enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt)

        for subdir, dirs, files in os.walk(os.path.join(repos_path, repo_name)):
            for file in files:
                total_file_cnt += 1
                if file.endswith('.java') and 'BaseListener' not in file and 'BaseVisitor' not in file:
                    total_java_files += 1
                    parse_for_methods(os.path.join(subdir, file))

        listener_pattern_cnt, visitor_pattern_cnt = get_pattern_list_data()
        enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt = get_method_list_data()
        
        repository_data.total_file_cnt = total_file_cnt
        repository_data.total_java_files = total_java_files
        repository_data.listener_pattern_cnt = listener_pattern_cnt
        repository_data.visitor_pattern_cnt = visitor_pattern_cnt
        repository_data.enter_method_cnt = enter_method_cnt
        repository_data.exit_method_cnt = exit_method_cnt
        repository_data.visit_method_cnt = visit_method_cnt
        
        repo_list.append(repository_data)

    return repo_list


def process_repositories(repo_path):
    repo_list = walk_repositories(repo_path)
    write_to_csv(repo_list)


def write_to_csv(repo_list):
    filename = 'repository_mining_data_'
    now = datetime.now()
    date_time = now.strftime("%d%m%Y_%H%M%S")
    filename += date_time + '.csv'

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

    for repo_data in repo_list:
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


if __name__ == "__main__":
    process_repositories(
        sys.argv[1])
