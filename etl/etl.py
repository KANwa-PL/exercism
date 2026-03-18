def transform(legacy_data):
    data = {}
    for index, value_list in legacy_data.items():
        for value in value_list:
            data.setdefault(str(value).lower(), index)
    return data
