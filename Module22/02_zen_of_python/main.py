zen = open('zen.txt', 'r')
revers_zen = [string for string in zen]
revers_zen = ''.join(reversed(revers_zen))
zen.close()
print(revers_zen)