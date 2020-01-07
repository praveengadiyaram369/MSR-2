
class Repository():

    num_of_repos = 0

    def __init__(self, repo_name, total_file_cnt, total_java_files, listener_pattern_cnt, visitor_pattern_cnt, enter_method_cnt, exit_method_cnt, enter_exit_method_cnt, visit_method_cnt):
        Repository.num_of_repos += 1
        self._repo_id = Repository.num_of_repos
        self._repo_name = repo_name
        self._total_file_cnt = total_file_cnt
        self._total_java_files = total_java_files
        self._listener_pattern_cnt = listener_pattern_cnt
        self._visitor_pattern_cnt = visitor_pattern_cnt
        self._enter_method_cnt = enter_method_cnt
        self._exit_method_cnt = exit_method_cnt
        self._enter_exit_method_cnt = enter_exit_method_cnt
        self._visit_method_cnt = visit_method_cnt

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

    