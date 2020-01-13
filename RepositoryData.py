
class Repository():
    """[class Repository is used to encapsulate all the data points related to a repository]
    """

    def __init__(self, repo_id, repo_name, total_file_cnt, total_java_files, listener_pattern_cnt, visitor_pattern_cnt, enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt):
        """[this constructor is used to initialize the values of a repository object and returns the same]

        Arguments:
            repo_id {[int]} -- [holds the unique id of the repository]
            repo_name {[type]} -- [holds the name of the repository]
            total_file_cnt {[type]} -- [holds the total count of files in a repository]
            total_java_files {[type]} -- [holds the total count of the java files]
            listener_pattern_cnt {[type]} -- [holds the count of listener patterns]
            visitor_pattern_cnt {[type]} -- [holds the count of visitor patterns]
            enter_method_cnt {[type]} -- [holds the count of enter methods in listener patterns]
            exit_method_cnt {[type]} -- [holds the count of exit methods in listener patterns]
            enter_exit_method_cnt {[type]} -- [holds the count of both enter and exit methods in listener patterns]
            visit_method_cnt {[type]} -- [holds the count of visit methods in visitor patterns]
        """
        self._repo_id = repo_id
        self._repo_name = repo_name
        self._total_file_cnt = total_file_cnt
        self._total_java_files = total_java_files
        self._listener_pattern_cnt = listener_pattern_cnt
        self._visitor_pattern_cnt = visitor_pattern_cnt
        self._enter_method_cnt = enter_method_cnt
        self._exit_method_cnt = exit_method_cnt
        self._enter_exit_method_cnt = enter_exit_method_cnt
        self._visit_method_cnt = visit_method_cnt

    """[Below all getter methods defined to get the value of Repository private attributes]
    
    Returns:
        [int/str] -- [returns respective data points]
    """
    @property
    def repo_id(self):
        return str(self._repo_id)

    @property
    def repo_name(self):
        return str(self._repo_name)

    @property
    def total_file_cnt(self):
        return str(self._total_file_cnt)

    @property
    def total_java_files(self):
        return str(self._total_java_files)

    @property
    def listener_pattern_cnt(self):
        return str(self._listener_pattern_cnt)

    @property
    def visitor_pattern_cnt(self):
        return str(self._visitor_pattern_cnt)

    @property
    def enter_method_cnt(self):
        return str(self._enter_method_cnt)

    @property
    def exit_method_cnt(self):
        return str(self._exit_method_cnt)

    @property
    def enter_exit_method_cnt(self):
        return str(self._enter_exit_method_cnt)

    @property
    def visit_method_cnt(self):
        return str(self._visit_method_cnt)

    """[Below all setter methods defined to set the value of Repository private attributes]
    """
    @repo_id.setter
    def repo_id(self, repo_id):
        self._repo_id = repo_id

    @repo_name.setter
    def repo_name(self, repo_name):
        self._repo_name = repo_name

    @total_file_cnt.setter
    def total_file_cnt(self, total_file_cnt):
        self._total_file_cnt = total_file_cnt

    @total_java_files.setter
    def total_java_files(self, total_java_files):
        self._total_java_files = total_java_files

    @listener_pattern_cnt.setter
    def listener_pattern_cnt(self, listener_pattern_cnt):
        self._listener_pattern_cnt = listener_pattern_cnt

    @visitor_pattern_cnt.setter
    def visitor_pattern_cnt(self, visitor_pattern_cnt):
        self._visitor_pattern_cnt = visitor_pattern_cnt

    @enter_method_cnt.setter
    def enter_method_cnt(self, enter_method_cnt):
        self._enter_method_cnt = enter_method_cnt

    @exit_method_cnt.setter
    def exit_method_cnt(self, exit_method_cnt):
        self._exit_method_cnt = exit_method_cnt

    @enter_exit_method_cnt.setter
    def enter_exit_method_cnt(self, enter_exit_method_cnt):
        self._enter_exit_method_cnt = enter_exit_method_cnt

    @visit_method_cnt.setter
    def visit_method_cnt(self, visit_method_cnt):
        self._visit_method_cnt = visit_method_cnt
