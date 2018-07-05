def update_dictionary(d, key, value):
    lst, key_true = [], key
    if key not in d:
        key_true = 2 * key
        if key_true in d:
            lst = d[key_true]
    else:
        lst = d[key]
    lst.append(value)
    d[key_true] = lst
