def is_prime(num):
    k = 0
    for i_num in range(2, num // 2 + 1):
        if num % i_num == 0:
            k += 1
    if k == 0:
        return num
    else:
        return 0


def crypto(string):
    lst = []
    block = (0, 1)
    for i, sym in enumerate(string):
        if i in block:
            continue
        if is_prime(i) == 0:
            continue
        else:
            lst.append(sym)
    return lst


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
