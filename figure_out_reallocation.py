from tkinter import Label


def figure_out_buy_sell_stuff(window):
    last_label = Label(window,
                       text=f'Current Correct End',
                       width=100, height=4,
                       fg="blue")
    last_label.grid(column=0, row=0)
