print('Задание 5. Пароль\n')

while True:
    upper_case = False
    digits_count = 0
    password = input('Введите пароль: ')
    for sym in password:
        if sym.isdigit():
            digits_count += 1
        elif sym.isupper():
            upper_case = True

    if digits_count >= 3 and upper_case and len(password) >= 8:
        print('Это надёжный пароль.')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')