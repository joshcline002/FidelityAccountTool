from csv import DictWriter
from StartAndGlobalUtils.my_utils import destroy

from StartAndGlobalUtils.program_variables import PERCENT_STORE
from GetPercentages.percentage_check_page import create_percent_check_page


def validate_percentages(window, entry_dict, label_dict, label_get_percentages, button_continue):
    list_of_percentages = []
    field_names = ['account', 'symbol', 'percentage']
    sum_percentages_per_account = {}
    for key, value in entry_dict.items():
        account, percentage = format_percent_store(key, list_of_percentages, value)
        sum_percentages_per_account[account] = sum_percentages_per_account.get(account,
                                                                               0.0) + percentage
    mis_match_percentages_text = percentage_sum_check(sum_percentages_per_account)
    if bool(mis_match_percentages_text):
        label_get_percentages.config(text=mis_match_percentages_text)
    else:
        write_percent_store_file(field_names, list_of_percentages)
        destroy(button_continue, entry_dict, label_dict, label_get_percentages)
        create_percent_check_page(window)


def format_percent_store(key, list_of_percentages, value):
    account = key.split('_')[0]
    symbol = key.split('_')[1]
    percentage = get_percentage(value)
    list_of_percentages.append({'account': account, 'symbol': symbol, 'percentage': percentage})
    return account, percentage


def write_percent_store_file(field_names, list_of_percentages):
    with open(PERCENT_STORE, 'w+') as csv_file:
        writer = DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(list_of_percentages)


def percentage_sum_check(sum_percentages_per_account):
    mis_match_percentages_text = ''
    for key, value in sum_percentages_per_account.items():
        if not value == 100:
            mis_match_percentages_text = f'{mis_match_percentages_text} Account: {key} has percent {value} ' \
                                         f'which is not 100.'
    return mis_match_percentages_text


def get_percentage(value):
    percentage = value.get()
    if not bool(percentage):
        percentage = 0.0
    return float(percentage)
