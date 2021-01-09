from os import path

from GetPercentages.create_percentage_page import create_percentage_store
from GetPercentages.percentage_check_page import create_percent_check_page

from StartAndGlobalUtils.program_variables import PERCENT_STORE


def check_and_set_percentage(window):
    if not path.exists(PERCENT_STORE):
        create_percentage_store(window)
    else:
        create_percent_check_page(window)
