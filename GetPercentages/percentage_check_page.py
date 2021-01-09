from tkinter import Button, Label
from csv import DictReader

from StartAndGlobalUtils.my_utils import destroy
from StartAndGlobalUtils.program_variables import PERCENT_STORE


def create_percent_check_page(window):
    current_row, percent_label_list = create_percentage_label_grid(window)
    button_correct = Button(window,
                            text="Correct",
                            command=lambda: next_reallocation(percent_label_list,
                                                                           button_correct,
                                                                           button_incorrect,
                                                                           window))
    button_correct.grid(column=0, row=current_row)
    current_row = current_row + 1
    button_incorrect = Button(window,
                              text="Incorrect",
                              command=lambda: next_reset_percentages(percent_label_list,
                                                                     button_correct,
                                                                     button_incorrect,
                                                                     window))
    button_incorrect.grid(column=0, row=current_row)


def create_percentage_label_grid(window):
    percentages = []
    with open(PERCENT_STORE, mode='r') as infile:
        percentages = percentages + list(DictReader(infile, delimiter=','))
    percent_label_list = []
    current_row = 0
    for percents in percentages:
        percent_label = create_account_symbol_from_percent_store_label(percents, current_row,
                                                                       window)
        current_row = current_row + 1
        percent_label_list.append(percent_label)
    return current_row, percent_label_list


def create_account_symbol_from_percent_store_label(percents, current_row, window):
    account = percents.get('account')
    symbol = percents.get('symbol')
    percentage = percents.get('percentage')
    account_symbol_label = Label(window,
                                 text=f'Percent for Account: {account}, Symbol: {symbol},'
                                      f' Percent: {percentage}',
                                 width=100, height=4,
                                 fg="blue")
    account_symbol_label.grid(column=0, row=current_row)
    return account_symbol_label


def next_reallocation(percent_label_list, button_correct, button_incorrect, window):
    destroy(button_correct, button_incorrect, percent_label_list)
    from Reallocation.figure_out_reallocation import reallocation
    reallocation(window)


def next_reset_percentages(percent_label_list, button_correct, button_incorrect, window):
    destroy(button_correct, button_incorrect, percent_label_list)
    from GetPercentages.reset_stored_percents import reset_percentages
    reset_percentages(window)
