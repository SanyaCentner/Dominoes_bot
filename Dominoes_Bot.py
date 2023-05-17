# """Пробуем писать телеграмм-бот домино"""
"""
This Example will show you how to use register_next_step handler.
"""
import telebot
from telebot import types
from Gamers import Gamer
from Game import Game

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
token = "5921260531:AAH7rsua62QwrqwK4XJcMNeL8D9tIUjr6BM"
bot = telebot.TeleBot(token)

# Функция возврата фишек для дальнейшей отправки в кнопки
def send_shticks_player(distribution):
    players[0].shticks = sorted(distribution[: 7])
    players[1].shticks = sorted(distribution[7: 14])
    players[2].shticks = sorted(distribution[14: 21])
    players[3].shticks = sorted(distribution[21: 28])

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
        Добро пожаловать в игру. Введи свое имя
        """)
    bot.register_next_step_handler(msg, process_name_step)

# Записываем свое имя и добавляем пользователя в словарь с ключом по id
def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = Gamer(name, chat_id)
        players.append(user)
    except Exception as e:
        bot.reply_to(message, 'oooops')

# Когда подключилось 2 игрока, то можно начинать игру
@bot.message_handler(commands=['start_game'])
def start_game(message):
    if len(players) == 4:
        print('Игра началась')
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
        number_of_passes = 0
        game.board = list([])
        print(f"Начало {game.count_round}-го раунда")
        for i in order:
            print(players[i - 1].shticks)
            try:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                if len(players[i - 1].shticks) == 7:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    item2 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[1]])
                    item3 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[2]])
                    item4 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[3]])
                    item5 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[4]])
                    item6 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[5]])
                    item7 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[6]])
                    markup.add(item1, item2, item3, item4, item5, item6, item7)
                elif len(players[i - 1].shticks) == 6:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    item2 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[1]])
                    item3 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[2]])
                    item4 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[3]])
                    item5 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[4]])
                    item6 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[5]])
                    markup.add(item1, item2, item3, item4, item5, item6)
                elif len(players[i - 1].shticks) == 5:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    item2 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[1]])
                    item3 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[2]])
                    item4 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[3]])
                    item5 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[4]])
                    markup.add(item1, item2, item3, item4, item5)
                elif len(players[i - 1].shticks) == 4:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    item2 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[1]])
                    item3 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[2]])
                    item4 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[3]])
                    markup.add(item1, item2, item3, item4)
                elif len(players[i - 1].shticks) == 3:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    item2 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[1]])
                    item3 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[2]])
                    markup.add(item1, item2, item3)
                elif len(players[i - 1].shticks) == 2:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    item2 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[1]])
                    markup.add(item1, item2)
                elif len(players[i - 1].shticks) == 1:
                    item1 = types.KeyboardButton(all_shtick_draw[players[i - 1].shticks[0]])
                    markup.add(item1)
                bot.send_message(players[i - 1].id,  reply_markup=markup)
                # msg = bot.reply_to(message, 'What is your gender', reply_markup=markup)
                # bot.register_next_step_handler(msg, process_sex_step)
            except Exception as e:
                bot.reply_to(message, 'oooops')
            print('Прошли try')

@bot.message_handler(content_types=["text"])
def test_callback(message): # <- passes a CallbackQuery type object to your function
    print('Мы зашли в какую-то функцию')
    print(message.text)

# @bot.message_handler(commands=['kek'])
# def add_gamer(message):
#     # if len(user_dict) == 2:
#     #     print('Игра началась')
#     # else:
#     #     print('pisun')
#     bot.register_next_step_handler(message, process_change_shticks)


# def process_sex_step(message):
#     try:
#         chat_id = message.chat.id
#         number_shticks = message.text
#         user = user_dict[chat_id]
#         if (sex == u'Male') or (sex == u'Female'):
#             user.sex = sex
#         else:
#             raise Exception("Unknown sex")
#         bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
#     except Exception as e:
#         bot.reply_to(message, 'oooops')

def start_game():
    if len(players) == 2:
        print('Игра началась')
    else:
        print('pisun')


if __name__ == "__main__":
    # Enable saving next step handlers to file "./.handlers-saves/step.save".
    # Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
    # saving will hapen after delay 2 seconds.
    players = list([])
    game = Game()
    bot.enable_save_next_step_handlers(delay=2)
    # Load next_step_handlers from save file (default "./.handlers-saves/step.save")
    # WARNING It will work only if enable_save_next_step_handlers was called!
    bot.load_next_step_handlers()
    bot.infinity_polling()
