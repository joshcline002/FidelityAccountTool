from my_utils import create_path_for_code
from initial_screen import initial_window, initial_elements


def main():
    create_path_for_code()
    window = initial_window()
    initial_elements(window)
    window.attributes('-fullscreen', True)
    window.mainloop()


main()
