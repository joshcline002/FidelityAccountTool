from Reallocation.figure_out_reallocation import create_data_frame


def test_create_data_frame():
    data_list = [{'AccountNumberOrName': '219765093', 'Symbol': 'CORE**', 'Quantity': 21.3,
                  'CurrentValue': 21.3, 'LastPrice': 1.0, 'PercentOfAccount': '2.38'},
                 {'AccountNumberOrName': '219765093', 'Symbol': 'IXUS', 'Quantity': 2.0,
                  'CurrentValue': 132.66, 'LastPrice': 66.33, 'PercentOfAccount': '2.38'},
                 {'AccountNumberOrName': '219765093', 'Symbol': 'SHV', 'Quantity': 1.0,
                  'CurrentValue': 110.52, 'LastPrice': 110.52, 'PercentOfAccount': '2.38'},
                 {'AccountNumberOrName': '219765093', 'Symbol': 'AGG', 'Quantity': 1.0,
                  'CurrentValue': 117.99, 'LastPrice': 117.99, 'PercentOfAccount': '2.38'},
                 {'AccountNumberOrName': '219765093', 'Symbol': 'ITOT', 'Quantity': 6.0,
                  'CurrentValue': 513.18, 'LastPrice': 85.53, 'PercentOfAccount': '2.38'}]
    add_amount = 0
    create_data_frame(data_list, add_amount)