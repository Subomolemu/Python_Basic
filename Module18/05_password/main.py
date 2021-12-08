while True:
    password = input('Придумайте пароль: ')

    if len(password) < 8:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    if password.lower() == password:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    if password.upper() == password:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    if password.isalpha():
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    if password.isdigit():
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    if not password.isalnum():
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue
    count = 0
    for i in password:
        if i.isdigit():
            count += 1
    if count < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
        continue

    print('Это надёжный пароль!')
    break
