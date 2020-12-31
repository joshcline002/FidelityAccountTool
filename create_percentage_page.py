from tkinter import Label, Button, Entry
from process_percentage_button import validate_percentages

from program_variables import get_consolidated_filtered_data


def create_percentage_store(window):
    page_elements = {}
    current_row = 0

    label_get_percentages = Label(window,
                                  text=f'Fund Percentages Do Not Exist Please Enter Them. Example 49.5',
                                  width=100, height=4,
                                  fg="blue")
    page_elements['label_get_percentages'] = label_get_percentages
    label_get_percentages.grid(column=0, row=current_row)

    current_row = current_row + 1
    label_dict = {}
    entry_dict = {}

    current_row = create_percentage_grid(current_row, entry_dict, label_dict, window)
    button_continue = Button(window,
                             text="Continue",
                             command=lambda: validate_percentages(entry_dict, label_dict, label_get_percentages,
                                                                  button_continue))
    button_continue.grid(column=0, row=current_row)


def create_percentage_grid(current_row, entry_dict, label_dict, window):
    account_name_number_list = list(
        set(d['AccountNumberOrName'] for d in get_consolidated_filtered_data() for val in d))
    symbol_list = list(set(d['Symbol'] for d in get_consolidated_filtered_data() for val in d))
    for account_number in account_name_number_list:
        for symbol in symbol_list:
            account_symbol_label = create_account_symbol_label(account_number, current_row, symbol, window)
            label_dict.update(account_symbol_label)

            account_symbol_entry = create_account_symbol_entry(current_row, window, account_number, symbol)
            entry_dict.update(account_symbol_entry)
            current_row = current_row + 1
    return current_row


def create_account_symbol_entry(current_row, window, account_number, symbol):
    account_symbol_entry = Entry(window, font=('calibre', 10, 'normal'))
    account_symbol_entry.grid(column=1, row=current_row)
    account_symbol_entry_dictionary = {f'{account_number}_{symbol}': account_symbol_entry}
    return account_symbol_entry_dictionary


def create_account_symbol_label(account_number, current_row, symbol, window):
    account_symbol_label = Label(window,
                                 text=f'Account: {account_number}, Symbol: {symbol}, Percent:',
                                 width=100, height=4,
                                 fg="blue")
    account_symbol_label.grid(column=0, row=current_row)
    account_symbol_label_dictionary = {f'{account_number}_{symbol}': account_symbol_label}
    return account_symbol_label_dictionary
