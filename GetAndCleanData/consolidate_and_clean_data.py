from StartAndGlobalUtils.program_variables import set_consolidated_filtered_data, set_account_list, \
    get_account_list


def set_consolidated_data_filtered_down(cleaned_list_of_fidelity_data):
    consolidate_and_filter_columns = {}
    account_name_number_list = get_account_list()
    symbol_list = list(set(d['Symbol'] for d in cleaned_list_of_fidelity_data for val in d))
    for fidelity_data in cleaned_list_of_fidelity_data:
        current_account_number = fidelity_data['AccountNameNumber']
        current_symbol = fidelity_data['Symbol']
        percent_of_account = fidelity_data['PercentOfAccount (Percent)']

        aggregate_quantity = aggregate_quantity_and_create_key(consolidate_and_filter_columns,
                                                               current_account_number,
                                                               current_symbol,
                                                               fidelity_data)
        consolidate_and_filter_columns[list(aggregate_quantity.keys())[0]] = \
            aggregate_quantity.get(list(aggregate_quantity.keys())[0])

        aggregate_value = aggregate_value_and_create_key(consolidate_and_filter_columns,
                                                         current_account_number, current_symbol,
                                                         fidelity_data)
        consolidate_and_filter_columns[list(aggregate_value.keys())[0]] = \
            aggregate_value.get(list(aggregate_value.keys())[0])

        current_price = fund_current_price(current_account_number, current_symbol, fidelity_data)
        consolidate_and_filter_columns[list(current_price.keys())[0]] = current_price.get(
            list(current_price.keys())[0])
    output = []
    for account_name_number in account_name_number_list:
        for symbol in symbol_list:
            output_dictionary = {'AccountNumberOrName': account_name_number,
                                 'Symbol': symbol,
                                 'Quantity': consolidate_and_filter_columns.get(
                                     f'{account_name_number}_{symbol}_Quantity', 0.0),
                                 'CurrentValue': consolidate_and_filter_columns.get(
                                     f'{account_name_number}_{symbol}_CurrentValue', 0.0),
                                 'LastPrice': consolidate_and_filter_columns.get(
                                     f'{account_name_number}_{symbol}_CurrentPrice', 0.0),
                                 'PercentOfAccount': percent_of_account}
            output.append(output_dictionary)
    set_consolidated_filtered_data(output)


def set_account_list_from_fidelity_file(cleaned_list_of_fidelity_data):
    account_name_number_list = list(
        set(d['AccountNameNumber'] for d in cleaned_list_of_fidelity_data for val in d))
    set_account_list(account_name_number_list)


def aggregate_quantity_and_create_key(consolidate_and_filter_columns, current_account_number,
                                      current_symbol,
                                      fidelity_data):
    current_quantity = consolidate_and_filter_columns.get(
        f'{current_account_number}_{current_symbol}_Quantity', 0.0)
    fidelity_quantity = float(fidelity_data.get('Quantity', 0.0))
    quantity_key = f'{current_account_number}_{current_symbol}_Quantity'
    consolidated_quantity = current_quantity + fidelity_quantity
    aggregate = {quantity_key: consolidated_quantity}
    return aggregate


def aggregate_value_and_create_key(consolidate_and_filter_columns, current_account_number,
                                   current_symbol,
                                   fidelity_data):
    value_key = f'{current_account_number}_{current_symbol}_CurrentValue'
    current_value = consolidate_and_filter_columns.get(value_key, 0.0)
    fidelity_value = float(fidelity_data.get('CurrentValue (In Dollars)', 0.0))
    consolidated_value = current_value + fidelity_value
    aggregate = {value_key: consolidated_value}
    return aggregate


def fund_current_price(current_account_number, current_symbol, fidelity_data):
    price_key = f'{current_account_number}_{current_symbol}_CurrentPrice'
    fidelity_price = float(fidelity_data.get('LastPrice (In Dollars)', 0.0))
    current_price = {price_key: fidelity_price}
    return current_price
