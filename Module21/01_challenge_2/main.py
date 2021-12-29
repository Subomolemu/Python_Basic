def outputs_numbers(number, printed_number):
    if printed_number == number:
        return number
    print(printed_number)
    return outputs_numbers(number, printed_number + 1)


num = int(input('Введите число: '))
printed_num = 1
print(outputs_numbers(num, printed_num))
