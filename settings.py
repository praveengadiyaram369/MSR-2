def init():
    global target_method_list
    target_method_list = ['enter', 'exit', 'visit']
    global method_list
    method_list = []
    global class_list
    class_list = []
    global enter_no_exit
    enter_no_exit = 0
    global exit_no_enter
    exit_no_enter = 0
    global enter_and_exit
    enter_and_exit = 0


def class_data_init():
    global class_method_enter_list
    class_method_enter_list = []
    global class_method_exit_list
    class_method_exit_list = []
