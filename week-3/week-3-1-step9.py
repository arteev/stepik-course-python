def modify_list(lst):
    for i in range(len(lst), -1, -1):
        if lst[i] % 2 == 1:
            del lst[i]
        else:
            lst[i] //= 2
