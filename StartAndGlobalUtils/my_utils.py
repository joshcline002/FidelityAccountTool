from os import path, mkdir

from StartAndGlobalUtils.program_variables import STORE_PATH


def destroy(*args):
    for arg in args:
        if bool(arg):
            if type(arg) == list:
                list_destroy(arg)
            elif type(arg) == dict:
                dict_destroy(arg)
            else:
                single_destroy(arg)


def single_destroy(some_destroyable_object):
    some_destroyable_object.destroy()


def list_destroy(some_destroyable_object_list):
    for item in some_destroyable_object_list:
        item.destroy()


def dict_destroy(some_destroyable_object_dict):
    for key, value in some_destroyable_object_dict.items():
        value.destroy()


def create_path_for_code():
    if not path.exists(STORE_PATH):
        mkdir(STORE_PATH)


def correct_incorrect_button_setup(frame, correct, incorrect, row, column):
    frame.grid(row=row, column=column, sticky="nsew")
    correct.pack(side="left")
    incorrect.pack(side="left")
