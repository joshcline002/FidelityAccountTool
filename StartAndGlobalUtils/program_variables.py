from os import path
from csv import DictReader

STORE_PATH = path.join(path.expanduser('~'), 'Documents', 'ReAllocatePythonProgram')
PERCENT_STORE = path.join(STORE_PATH, 'FundPercents.csv')
CONSOLIDATED_FILTERED_DATA = []
ADD_AMOUNT = {}
FILE_NAME = None
ACCOUNT_LIST = []
PERCENTAGE_DATA = {}


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


def set_account_list(account_list):
    global ACCOUNT_LIST
    if type(account_list) == list:
        ACCOUNT_LIST = account_list


def get_account_list():
    return ACCOUNT_LIST


def set_percentage_data():
    global PERCENTAGE_DATA
    with open(PERCENT_STORE, mode='r') as infile:
        percent_data = list(DictReader(infile, delimiter=','))
        percent_data_for_account = [d for d in percent_data if d['account'] in ACCOUNT_LIST]
        PERCENTAGE_DATA = percent_data_for_account


def get_percentage_data():
    return PERCENTAGE_DATA
