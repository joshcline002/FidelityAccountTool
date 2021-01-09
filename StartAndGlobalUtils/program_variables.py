from os import path

STORE_PATH = path.join(path.expanduser('~'), 'Documents', 'ReAllocatePythonProgram')
PERCENT_STORE = path.join(STORE_PATH, 'FundPercents.csv')
CONSOLIDATED_FILTERED_DATA = None
ADD_AMOUNT = None
FILE_NAME = None


def set_consolidated_filtered_data(consolidated_filtered_data):
    global CONSOLIDATED_FILTERED_DATA
    if type(consolidated_filtered_data) == list:
        CONSOLIDATED_FILTERED_DATA = consolidated_filtered_data


def get_consolidated_filtered_data():
    return CONSOLIDATED_FILTERED_DATA


def set_add_amount(add_amount):
    global ADD_AMOUNT
    ADD_AMOUNT = add_amount


def get_add_amount():
    return ADD_AMOUNT


def set_file_name(file_name):
    global FILE_NAME
    FILE_NAME = file_name


def get_file_name():
    return FILE_NAME
