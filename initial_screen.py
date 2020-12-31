from tkinter import Tk, Button


from my_utils import destroy
from get_file_name import get_file_name_page


def initial_window():
    window = Tk()
    window.title('Re-allocate')
    window.geometry("500x500")
    window.config(background="white")
    return window


def initial_elements(window):
    get_file_name_page(window)
    button_exit = Button(window, text="Exit", command=lambda: destroy(window))
    button_exit.grid(column=4, row=0)
