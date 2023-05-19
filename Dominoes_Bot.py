# """Пробуем писать телеграмм-бот домино"""
"""
This Example will show you how to use register_next_step handler.
"""
import os
import telebot
from telebot import types
from Gamers import Gamer
from Game import Game

NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP = 0
players = list([])
game = Game()
board_for_draw = list([])
all_all_shtick_draw_tg = {1: "🁣", 2: "🀲", 3: "🀳", 4: "🀴", 5: "🀵", 6: "🀶", 7: "🀷",
                   8: "🁫", 9: "🀺", 10: "🀻", 11: "🀼", 12: "🀽", 13: "🀾",
                   14: "🁳", 15: "🁂", 16: "🁃", 17: "🁄", 18: "🁅",
                   19: "🁻", 20: "🁊", 21: "🁋", 22: "🁌",
                   23: "🂃", 24: "🁒", 25: "🁓",
                   26: "🂋", 27: "🁚",
                   28: "🂓",
                   29: "🁣", 30: "🀸", 31: "🀿", 32: "🁆", 33: "🁍", 34: "🁔", 35: "🁛",
                   36: "🁫", 37: "🁀", 38: "🁇", 39: "🁎", 40: "🁕", 41: "🁜",
                   42: "🁳", 43: "🁈", 44: "🁏", 45: "🁖", 46: "🁝",
                   47: "🁻", 48: "🁐", 49: "🁗", 50: "🁞",
                   51: "🂃", 52: "🁘", 53: "🁟",
                   54: "🂋", 55: "🁠|",
                   56: "🂓"}

all_shtick_draw = {1: "|__|__|", 2: "|__|•|", 3: "|__|.°|", 4: "|__|.•°|", 5: "|__|::|", 6: "|__|:•:|",
                   7: "|__|:::|",
                   8: "|•|•|", 9: "|•|.°|", 10: "|•|.•°|", 11: "|•|::|", 12: "|•|:•:|", 13: "|•|:::|",
                   14: "|.°|.°|", 15: "|.°|.•°|", 16: "|.°|::|", 17: "|.°|:•:|", 18: "|.°|:::|",
                   19: "|.•°|.•°|", 20: "|.•°|::|", 21: "|.•°|:•:|", 22: "|.•°|:::|",
                   23: "|::|::|", 24: "|::|:•:|", 25: "|::|:::|",
                   26: "|:•:|:•:|", 27: "|:•:|:::|",
                   28: "|:::|:::|",
                   29: "|__|__|", 30: "|•|__|", 31: "|.°|__|", 32: "|.•°|__|", 33: "|::|__|", 34: "|:•:|__|",
                   35: "|:::|__|",
                   36: "|•|•|", 37: "|.°|•|", 38: "|.•°|•|", 39: "|::|•|", 40: "|:•:|•|", 41: "|:::|•|",
                   42: "|.°|.°|", 43: "|.•°|.°|", 44: "|::|.°|", 45: "|:•:|.°|", 46: "|:::|.°|",
                   47: "|.•°|.•°|", 48: "|::|.•°|", 49: "|:•:|.•°|", 50: "|:::|.•°|",
                   51: "|::|::|", 52: "|:•:|::|", 53: "|:::|::|",
                   54: "|:•:|:•:|", 55: "|:::|:•:|",
                   56: "|:::|:::|"}


f = open('/Users/aleksandr/Documents/token.txt')
token = f.read()
token = token[1: -2]
bot = telebot.TeleBot(token)
NUMBER_OF_PASSES = 0

# Функция возврата фишек для дальнейшей отправки в кнопки
def send_shticks_player(distribution):
    """Раздаем каждому фишки"""
    players[0].shticks = sorted(distribution[: 7])
    players[1].shticks = sorted(distribution[7: 14])
    players[2].shticks = sorted(distribution[14: 21])
    players[3].shticks = sorted(distribution[21: 28])


def get_params(players, count, pos, count_round, board):
    """Возвращаем каждому его параметры"""
    lst = []
    for i in range(len(players)):
        if count == i:
            dct = {'pos': pos,
                   'name': players[count].name,
                   'count_of_round': count_round,
                   'board': board,
                   'shticks': players[count].shticks}
            lst.append(dct)
        else:
            dct = {'pos': list([[], None, None]),
                   'name': players[count].name,
                   'count_of_round': count_round,
                   'board': board,
                   'shticks': players[i].shticks}
            lst.append(dct)
    return lst


def get_button(player, position):
    buttons = list([])
    """Если ничего поставить нельзя, то оправляем просто фишки, которые имеются у игрока"""
    if position == [[], None, None]:
        for shtick in player.shticks:
            buttons.append(all_shtick_draw[shtick])
        return buttons

    count_in_position = []
    """Иначе будем смотреть что и куда можно поставить"""
    for elem in position:
        if elem[0][0] not in count_in_position:
            count_in_position.append(player.shticks[elem[0][0]])
        buttons.append(all_shtick_draw[player.shticks[elem[0][0]]] + ' ' + elem[0][1])

    """Добавляем остальные клавиши"""
    for shtick in player.shticks:
        if shtick not in count_in_position:
            buttons.append(all_shtick_draw[shtick])
    return buttons


def examination_shtick_on_draw(side, number):
    if len(board_for_draw) == 0:
        return number
    if side == 'left':
        first_shticks = board_for_draw[0]
        if game.all_shtick[number][2] == game.all_shtick[first_shticks][0]:
            return number
        else:
            return number + 28
    elif side == 'right':
        first_shticks = board_for_draw[-1]
        if game.all_shtick[number][0] == game.all_shtick[first_shticks][2]:
            return number
        else:
            return number + 28

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):

    msg = bot.reply_to(message, """\
        Добро пожаловать в игру. Введи свое имя
        """)
    bot.register_next_step_handler(msg, process_name_step)


# Записываем свое имя и добавляем пользователя в словарь с ключом по id
def process_name_step(message):
    print(players)
    try:
        chat_id = message.chat.id
        name = message.text
        user = Gamer(name, chat_id)
        players.append(user)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def get_board():
    message = ''
    print(game.board)
    if len(game.board) == 0:
        return 'Поставьте первую фишку'
    for shtick in game.board:
        message += all_all_shtick_draw_tg[shtick]
    return message

def next_step():
    print(f"ходит игрок "
          f"{players[NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP].name, players[NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP].shticks}")
    pos_var = game.put_a_chip(NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP, players)
    print(pos_var)
    params = get_params(players, NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP, pos_var, game.count_round, game.board)
    for i in range(0, 4):
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for elem in get_button(players[i - 1], params[i - 1]['pos']):
                item1 = types.KeyboardButton(elem)
                markup.add(item1)
            bot.send_message(players[i - 1].id, get_board(), reply_markup=markup)
        except Exception as e:
            print('Не прошло')

    # if pos_var[NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP] == [[], None, None]:
    #     next_step()




def start_round():
    list_shticks = game.chip_distribution()
    send_shticks_player(list_shticks)
    print('Раздача окончена')
    order = game.order(players)
    print(order)
    print(f"Имя первого чела {players[order[0] - 1].name} "
          f"и его фишки {players[order[0] - 1].shticks}")
    # Раунд начался.
    # Пишем номер раунда.
    game.end_round = True
    global NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP
    NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP = order[0] - 1
    number_of_passes = 0
    game.board = list([])
    print(f"Начало {game.count_round}-го раунда")
    print('Количество пропусков', number_of_passes)
    print(f"ходит игрок {players[order[0] - 1].name, players[order[0] - 1].shticks}")
    pos_var = game.put_a_chip(order[0] - 1, players)
    params = get_params(players, order[0] - 1, pos_var, game.count_round, game.board)
    for i in order:
        try:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for elem in get_button(players[i - 1], params[i - 1]['pos']):
                item1 = types.KeyboardButton(elem)
                markup.add(item1)
            bot.send_message(players[i - 1].id, 'Начало раунда ставьте фишку', reply_markup=markup)
        except Exception as e:
            print('Хуета')
        print('Прошли try')


# Когда подключилось 2 игрока, то можно начинать игру
@bot.message_handler(commands=['start_game'])
def start_game(message):
    if len(players) == 4:
        print('Игра началась')
        start_round()


def find_number(shtick):
    number = shtick[: shtick.index(' ')]
    print(number)
    _side = shtick[shtick.index(' ') + 1:]
    print(_side)
    for key in all_shtick_draw:
        if all_shtick_draw[key] == number:
            return key, _side


@bot.message_handler(content_types=["text"])
def test_callback(message):
    print(message)
    number = 0
    global NUMBER_OF_PASSES
    if len(message.text) > 9:
        NUMBER_OF_PASSES = 0
        print(message.text)
        number_of_shtick, side = find_number(message.text)
        if side == 'left':
            game.board.insert(0, examination_shtick_on_draw('left', number_of_shtick))
            for player in players:
                if player.id == message.from_user.id:
                    number = players.index(player)
                    print(player.shticks)
                    player.shticks.remove(number_of_shtick)
        elif side == 'right':
            game.board.append(examination_shtick_on_draw('right', number_of_shtick))
            for player in players:
                if player.id == message.from_user.id:
                    number = players.index(player)
                    print(player.shticks)
                    player.shticks.remove(number_of_shtick)
    else:
        NUMBER_OF_PASSES += 1
    global NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP
    if NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP != 3:
        NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP += 1
    else:
        NUMBER_OF_HUMAN_WHO_PUTS_A_CHIP = 0

    if game.dont_end_round(NUMBER_OF_PASSES,
                                number, players) \
            and len(game.board) >= 12:
        game.end_round = False
        print('Раунд должен быть закончен')
        for player in players:
            bot.send_message(player.id, f"Счет между командой {players[0].name, players[2].name} и "
                                        f"{players[1].name, players[3].name}: {game.point_team_one} :"
                                        f"{game.point_team_two}")
        start_round()
    next_step()




def start_game():
    if len(players) == 2:
        print('Игра началась')
    else:
        print('pisun')


if __name__ == "__main__":
    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    bot.enable_save_next_step_handlers(delay=2)
    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()
    bot.infinity_polling()
