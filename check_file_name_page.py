from tkinter import Button, Label, Frame

from my_utils import destroy, correct_incorrect_button_setup
from program_variables import get_file_name


def check_file_name_page(window):
    page_element_dict = {}
    label_file_check = Label(window, text=f'File to use: {get_file_name()}', width=100, height=4, fg="blue")
    page_element_dict['label_file_check'] = label_file_check

    buttons_frame = Frame(window)
    page_element_dict['buttons_frame'] = buttons_frame

    button_correct = Button(buttons_frame,
                            text="Correct",
                            command=lambda: next_add_amount_page(page_element_dict, window))
    page_element_dict['button_correct'] = button_correct

    button_incorrect = Button(buttons_frame,
                              text="Incorrect",
                              command=lambda: next_get_file_name_page(page_element_dict, window))
    page_element_dict['button_incorrect'] = button_incorrect

    label_file_check.grid(row=0, column=0)

    correct_incorrect_button_setup(buttons_frame, button_correct, button_incorrect, 1, 0)


def next_add_amount_page(page_element_dict, window):
    destroy(page_element_dict)
    from add_amount_screen import added_amount_page
    added_amount_page(window)


def next_get_file_name_page(page_element_dict, window):
    destroy(page_element_dict)
    from get_file_name import get_file_name_page
    get_file_name_page(window)
