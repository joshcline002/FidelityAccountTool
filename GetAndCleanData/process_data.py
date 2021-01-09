from GetAndCleanData.consolidate_and_clean_data import set_consolidated_data_filtered_down, \
    set_account_list_from_fidelity_file
from GetAndCleanData.get_and_clean_fidelity_data import get_fidelity_data


def process_data():
    cleaned_list_of_fidelity_data = get_fidelity_data()
    set_account_list_from_fidelity_file(cleaned_list_of_fidelity_data)
    set_consolidated_data_filtered_down(cleaned_list_of_fidelity_data)
