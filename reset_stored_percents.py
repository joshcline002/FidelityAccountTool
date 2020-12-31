from tkinter import Label, Entry
from csv import DictReader

from program_variables import PERCENT_STORE, get_consolidated_filtered_data


def reset_percentages(window):
    percentages = []
    with open(PERCENT_STORE, mode='r') as infile:
        percentages = percentages + list(DictReader(infile, delimiter=','))
    account_name_number_list_portfolio = list(
        set(d['AccountNumberOrName'] for d in get_consolidated_filtered_data() for val in d))

    for account in account_name_number_list_portfolio:
        account_percentages = [d for d in percentages if d['account'] in [account]]
        missing_symbol_list = get_missing_symbol_list(account_percentages, account)
        for missing_symbol in missing_symbol_list:
            missing_percent = {'account': account,
                               'symbol': missing_symbol}
            percentages.append(missing_percent)
    account_numbers = list(set(d['account'] for d in percentages for val in d))
    account_symbol_entry_dictionary = {}
    for account_number in account_numbers:
        account_percantages = [d for d in percentages if d['account'] == account_number]
        account_symbol = list(set(d['account'] for d in percentages for val in d))
    current_row, percent_label_list = create_percentage_label_grid(window, percentages)
    create_account_symbol_entry(current_row, window, percentages)


def get_missing_symbol_list(percentages, account):
    consolidated_list_for_account = [d for d in get_consolidated_filtered_data() if d['AccountNumberOrName'] == account]
    symbol_list_portfolio_for_account = list(set(d['Symbol'] for d in consolidated_list_for_account for val in d))
    symbol_list_stored = list(set(d['symbol'] for d in percentages for val in d))
    missing_symbol_list = list(set(symbol_list_portfolio_for_account) - set(symbol_list_stored))
    return missing_symbol_list


def get_missing_account_list(percentages):
    account_name_number_list_portfolio = list(
        set(d['AccountNumberOrName'] for d in get_consolidated_filtered_data() for val in d))
    account_name_number_list_stored = list(set(d['account'] for d in percentages for val in d))
    missing_account_list = list(set(account_name_number_list_portfolio) - set(account_name_number_list_stored))
    return missing_account_list


def create_percentage_label_grid(window, percentages):
    percent_label_list = []
    current_row = 0
    for percents in percentages:
        percent_label = create_account_symbol_from_percent_store_label(percents, current_row, window)
        current_row = current_row + 1
        percent_label_list.append(percent_label)
    return current_row, percent_label_list


def create_account_symbol_from_percent_store_label(percents, current_row, window):
    account = percents.get('account')
    symbol = percents.get('symbol')
    percentage = percents.get('percentage')
    account_symbol_label = Label(window,
                                 text=f'Percent for Account: {account}, Symbol: {symbol}, Old Percent: {percentage}',
                                 width=100, height=4,
                                 fg="blue")
    account_symbol_label.grid(column=0, row=current_row)
    return account_symbol_label


def create_account_symbol_entry(current_row, window, percentages):
    account_numbers = list(set(d['account'] for d in percentages for val in d))
    account_symbol_entry_dictionary = {}
    for account_number in account_numbers:
        account_percantages = [d for d in percentages if d['account'] == account_number]
        account_symbol = list(set(d['account'] for d in percentages for val in d))
        account_symbol_entry = Entry(window, font=('calibre', 10, 'normal'))
        account_symbol_entry.grid(column=1, row=current_row)
        account_symbol_entry_dictionary = {f'{account_number}_{symbol}': account_symbol_entry}
    return account_symbol_entry_dictionary
