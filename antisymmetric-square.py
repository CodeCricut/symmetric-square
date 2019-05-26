def antisymmetric(main_list):
    n = len(main_list)
    r = 0
    col = []
    while r < n:
        c = 0
        col = []
        while c < n:
            col.append((main_list[c][r]) * -1)
            c += 1
        if col != main_list[r]:
                return False
        r += 1
    return True


print(antisymmetric([[0, 1, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
#>>> True

print(antisymmetric([[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]))
#>>> True

print(antisymmetric([[0, 1, 2],
                     [-1, 0, -2],
                     [2, 2,  3]]))
#>>> False

print(antisymmetric([[1, 2, 5],
                     [0, 1, -9],
                     [0, 0, 1]]))
#>>> False
