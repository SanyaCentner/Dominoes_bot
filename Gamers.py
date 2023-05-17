"""Gamers class"""



class Gamer:

    def __init__(self, name, chat_id):
        self.id = chat_id
        self.shticks = []
        self.errors = 0
        self.name = name

    def input_number(self):
        while True:
            try:
                number_shtics = int(input())
                break
            except ValueError:
                print('Неправильно введен номер, попробуйте снова')
                return self.input_number()
        return number_shtics



