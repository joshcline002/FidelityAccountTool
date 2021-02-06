from tkinter import Tk, Button, ttk, Canvas


from StartAndGlobalUtils.my_utils import destroy
from GetFile.get_file_name import get_file_name_page


def initial_window():
    root = Tk()
    container = ttk.Frame(root)
    canvas = Canvas(container)
    scrollbar_vertical = ttk.Scrollbar(container, command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand=scrollbar_vertical.set)

    root.title('Re-allocate')
    root.config(background="white")

    container.pack(fill='both', expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar_vertical.pack(side="right", fill="y")

    button_exit = Button(scrollable_frame, text="Exit",
                         command=lambda: destroy(root))
    button_exit.grid(column=4, row=0)
    return root, scrollable_frame


def initial_elements(window):
    get_file_name_page(window)
