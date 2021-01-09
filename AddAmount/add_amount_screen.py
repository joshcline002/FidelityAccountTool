from tkinter import Label, Entry, Button
from StartAndGlobalUtils.my_utils import destroy
from StartAndGlobalUtils.program_variables import set_add_amount


def added_amount_page(window):
    page_element_dict = {}
    added_dollars_label = Label(window, text='Add dollar amount before recalibration. Example: 40000',
                                font=('calibre', 10, 'bold'))
    page_element_dict['added_dollars_label'] = added_dollars_label

    added_dollars_entry = Entry(window, text='Add dollar amount before reallocation. Example: 40000',
                                font=('calibre', 10, 'normal'))
    page_element_dict['added_dollars_entry'] = added_dollars_entry

    button_submit = Button(window, text="Submit",
                           command=lambda: next_check_add_amount(page_element_dict, window))
    page_element_dict['button_submit'] = button_submit

    added_dollars_label.grid(column=0, row=1)
    added_dollars_entry.grid(column=0, row=2)
    button_submit.grid(column=0, row=3)


def next_check_add_amount(page_element_dict, window):
    set_add_amount(get_add_amount(page_element_dict['added_dollars_entry']))
    destroy(page_element_dict)
    from AddAmount.check_add_amount import check_add_amount
    check_add_amount(window)


def get_add_amount(added_dollars_entry):
    add_amount = added_dollars_entry.get()
    if not bool(add_amount):
        add_amount = 0
    return add_amount
