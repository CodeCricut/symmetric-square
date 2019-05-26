def symmetric(main_list):
    n = len(main_list)
    r = 0
    col = []
    while r < n:
        c = 0
        col = []
        while c < n:
            col.append(main_list[c][r])
            c += 1
        if col != main_list[r]:
                return False
        r += 1
    return True


print(symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]]))