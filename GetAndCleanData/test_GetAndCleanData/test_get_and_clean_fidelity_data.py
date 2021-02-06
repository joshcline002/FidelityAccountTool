from GetAndCleanData.get_and_clean_fidelity_data import clean_value_and_key


def test_clean_value_and_key_remove_extras():
    key = "Today's Gain/Loss Dollar"
    value = "$Value%"

    expected_key = 'TodaysGainLossDollar'
    expected_value = 'Value'

    actual_key, actual_value = clean_value_and_key(key, value)

    assert actual_key == expected_key
    assert actual_value == expected_value

def test_clean_value_and_key_blank_field():
    key = "Normal Key"
    value = ""

    expected_key = "NormalKey"
    expected_value = None

    actual_key, actual_value = clean_value_and_key(key, value)

    assert actual_key == expected_key
    assert actual_value == expected_value
