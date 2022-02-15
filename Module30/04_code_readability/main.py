from typing import List


def prime_number(max_num) -> List[int]:
    """Функция, возвращающая список простых чисел от 2 до max_num"""
    num_lst: List = list()
    for i in range(2, max_num + 1):
        count = 0
        for num in range(1, i // 2 + 1):
            if i % num == 0:
                count += 1
        if count < 2:
            num_lst.append(i)
    return num_lst


print(prime_number(max_num=1000))

a: List[int] = list(filter(lambda x:
                           len(list(filter(lambda i: x % i == 0,
                                           [num for num in
                                            range(2, x // 2 + 1)]))) == 0,
                           [x for x in range(2, 1001)]))  # очень сложно
# читать, и к тому же сложно составить, гораздо проще функцией

print(a)
