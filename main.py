from StartAndGlobalUtils.my_utils import create_path_for_code
from StartAndGlobalUtils.initial_screen import initial_window, initial_elements


def main():
    create_path_for_code()
    root, window = initial_window()
    initial_elements(window)
    root.mainloop()


main()
