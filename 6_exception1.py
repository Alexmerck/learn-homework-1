"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user():
    while True:
        try:
            user_answer = input('Как дела? ')
            if user_answer == 'Хорошо':
                print('Правильный ответ')
                break
        except KeyboardInterrupt:
            print('Пока!')
            break
        else:
            print('Неправльный ответ')


if __name__ == "__main__":
    hello_user()
