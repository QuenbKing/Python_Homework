print('Задача 4. Чат\n')


def view_chat():
    with open("chat.txt", "r", encoding="utf8") as chat_file:
        print(chat_file.read())


def send_chat(user_name):
    with open("chat.txt", "a", encoding="utf8") as chat_file:
        message = input('Введите сообщение: ')
        chat_file.write(f'{user_name}: {message}\n')


while True:
    try:
        name = input("Введите имя: ")
        if not name.isalpha():
            raise SyntaxError

        action = int(input('Выберите действие'
                           '(1.Посмотреть текущий текст чата, 2.Отправить сообщение (затем вводит сообщение): '))
        if action == 1:
            view_chat()
        elif action == 2:
            send_chat(name)
        else:
            raise ValueError
    except SyntaxError:
        print('Имя должно состоять только из букв')
    except ValueError:
        print('Введено неверное значение. Допустимые номера действий(1,2)')
