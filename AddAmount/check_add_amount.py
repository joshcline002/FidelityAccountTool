from tkinter import Button, Label, Frame
from StartAndGlobalUtils.my_utils import correct_incorrect_button_setup, destroy
from StartAndGlobalUtils.program_variables import get_add_amount


def check_add_amount(window):
    page_element_dict = {}
    label_file_check = Label(window, text=f'Amount to Add: {get_add_amount()}', width=100, height=4, fg="blue")
    page_element_dict['label_file_check'] = label_file_check

    buttons_frame = Frame(window)
    page_element_dict['buttons_frame'] = buttons_frame

    button_correct = Button(buttons_frame,
                            text="Correct",
                            command=lambda: next_process_data(page_element_dict, window))
    page_element_dict['button_correct'] = button_correct

    button_incorrect = Button(buttons_frame,
                              text="Incorrect",
                              command=lambda: next_added_amount_page(page_element_dict, window))
    page_element_dict['button_incorrect'] = button_incorrect

    label_file_check.grid(column=0, row=0)
    correct_incorrect_button_setup(buttons_frame, button_correct, button_incorrect, column=0, row=1)


def next_added_amount_page(page_element_dict, window):
    destroy(page_element_dict)
    from AddAmount.add_amount_screen import added_amount_page
    added_amount_page(window)


def next_process_data(page_element_dict, window):
    destroy(page_element_dict)
    from GetPercentages.check_and_set_percentages import check_and_set_percentage
    check_and_set_percentage(window)
