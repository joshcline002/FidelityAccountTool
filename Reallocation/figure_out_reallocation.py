from tkinter import Label

from StartAndGlobalUtils.program_variables import CONSOLIDATED_FILTERED_DATA, ADD_AMOUNT


def reallocation(window):
    create_data_frame(CONSOLIDATED_FILTERED_DATA, ADD_AMOUNT)
    last_label = Label(window,
                       text=f'Current Correct End',
                       width=100, height=4,
                       fg="blue")
    last_label.grid(column=0, row=0)


def create_data_frame(list_of_data, add_amount):
    total_market_value = add_amount
    for data in list_of_data:
        total_market_value = total_market_value + data.get('CurrentValue', 0)
    print(total_market_value)
