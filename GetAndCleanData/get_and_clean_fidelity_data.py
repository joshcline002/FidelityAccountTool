from tkinter import re
from csv import DictReader

from StartAndGlobalUtils.program_variables import get_file_name


def get_fidelity_data():
    cleaned_list_of_fidelity_data = []
    with open(get_file_name(), mode='r') as infile:
        fidelity_file = list(DictReader(infile, delimiter=','))
        for cleaned_fidelity_data in fidelity_file:
            cleaned_fidelity_data.pop(None, None)
            new_dict = {}
            for key, value in cleaned_fidelity_data.items():
                if value is not None:
                    cleaned_key, cleaned_value = clean_value_and_key(key, value)

                    new_dict[cleaned_key] = cleaned_value

            if len(new_dict) > 3:
                cleaned_list_of_fidelity_data.append(new_dict)
    return cleaned_list_of_fidelity_data


def clean_value_and_key(key, value):
    cleaned_key = re.sub(' ', '', re.sub('[^A-Za-z0-9]+', '', key))
    cleaned_value = value.replace('%', '').replace('$', '') or None
    return cleaned_key, cleaned_value
