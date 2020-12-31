from consolidate_and_clean_data import get_consolidated_data_filtered_down
from get_and_clean_fidelity_data import get_fidelity_data
from check_and_set_percentages import check_and_set_percentage

from program_variables import set_consolidated_filtered_data, get_consolidated_filtered_data


def process_data(window):
    cleaned_list_of_fidelity_data = get_fidelity_data()
    set_consolidated_filtered_data(get_consolidated_data_filtered_down(cleaned_list_of_fidelity_data))
    check_and_set_percentage(window)
