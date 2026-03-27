def find(search_list, value):
    offset = 0

    while len(search_list) > 0:
        middle = len(search_list) // 2

        if value == search_list[middle]:
            return offset + middle
        elif value < search_list[middle]:
            search_list = search_list[:middle]
        else:
            offset += middle + 1
            search_list = search_list[middle + 1:]
    raise ValueError("value not in array")


find([1, 3, 4, 6, 8, 9, 11],6)