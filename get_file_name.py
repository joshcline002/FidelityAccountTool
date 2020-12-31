from tkinter import Button, filedialog
from my_utils import destroy
from program_variables import set_file_name


def get_file_name_page(window):
    page_element_dict = {}
    button_explore = Button(window,
                            text="Select Fidelity CSV",
                            command=lambda: get_file_name(page_element_dict, window))

    page_element_dict['button_explore'] = button_explore
    button_explore.grid(column=0, row=0)


def get_file_name(page_element_dict, window):
    set_file_name(filedialog.askopenfilename(initialdir="/",
                                             title="Select a csv File downloaded from Fidelity positions.",
                                             filetypes=(("CSV files", "*.csv*"), ("all files", "*.*"))))
    destroy(page_element_dict)
    from check_file_name_page import check_file_name_page
    check_file_name_page(window)
