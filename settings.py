def init():
    """[this method is primarly used to hold global variables all around the project
         and mainly for initialization of variables to empty]
    """

    # _holds method names which are tracking in the listener - enter, exit and visit
    global target_method_list
    target_method_list = ['enter', 'exit', 'visit']

    # _holds all the method names in the repository
    global method_list
    method_list = []

    # _holds all the class names in the repository which are either a listener or a visitor
    global extended_class_list
    extended_class_list = []

    # _holds all the X part of enterX method names in the repository
    global method_enter_list
    method_enter_list = []

    # _holds all the X part of exitX method names in the repository
    global method_exit_list
    method_exit_list = []

    # _holds all the X part of visitX method names in the repository
    global method_visit_list
    method_visit_list = []
