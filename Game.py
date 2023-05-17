
import random
from Gamers import Gamer

class Game:
    """Основная часть игры"""

    min_of_end_point = 101

    def __init__(self):
        self.board = list([])
        self.count_round = 1
        self.number_first_move = 0
        self.point_team_one = 0
        self.point_team_two = 0
        self.end_round = True
        self.end_game = True
        self.all_shtick = {1: "0-0", 2: "0-1", 3: "0-2", 4: "0-3", 5: "0-4", 6: "0-5", 7: "0-6",
                           8: "1-1", 9: "1-2", 10: "1-3", 11: "1-4", 12: "1-5", 13: "1-6",
                           14: "2-2", 15: "2-3", 16: "2-4", 17: "2-5", 18: "2-6",
                           19: "3-3", 20: "3-4", 21: "3-5", 22: "3-6",
                           23: "4-4", 24: "4-5", 25: "4-6",
                           26: "5-5", 27: "5-6",
                           28: "6-6",
                           29: "0-0", 30: "1-0", 31: "2-0", 32: "3-0", 33: "4-0", 34: "5-0", 35: "6-0",
                           36: "1-1", 37: "2-1", 38: "3-1", 39: "4-1", 40: "5-1", 41: "6-1",
                           42: "2-2", 43: "3-2", 44: "4-2", 45: "5-2", 46: "6-2",
                           47: "3-3", 48: "4-3", 49: "5-3", 50: "6-3",
                           51: "4-4", 52: "5-4", 53: "6-4",
                           54: "5-5", 55: "6-5",
                           56: "6-6"}
        self.doubles = [1, 8, 14, 19, 23, 26, 28]
        # self.X_right = 750
        # self.X_left = 750
        # self.Y_doubles = 345
        # self.Y_not_doubles = 360

    def examination_distribution(self, list_of_shtick):
        """ Проверка разданных фишек на наличие 5 и больше дублей """
        for i in range(0, 4):
            count_doubles = 0
            for number in self.doubles:
                if number in list_of_shtick[i * 7: i * 7 + 7]:
                    count_doubles += 1
            if count_doubles >= 5:
                return False
        return True

    def match_list(self, count):
        """ Функция выбора порядка ходов """
        if count == 1:
            return list([1, 2, 3, 4])
        elif count == 2:
            return list([2, 3, 4, 1])
        elif count == 3:
            return list([3, 4, 1, 2])
        elif count == 4:
            return list([4, 1, 2, 3])

    def find_first_move(self, players):
        """ Выбор игрока, у которого 1-1 """
        tmp = 1
        for player in players:
            for elem in player.shticks:
                if elem == 8:
                    return self.match_list(tmp)
            tmp += 1

    def order(self, players):
        """Возвращаем порядок"""
        if self.count_round == 1:
            return self.find_first_move(players)
        else:
            return self.match_list(self.number_first_move)

    def chip_distribution(self):
        """ Раздача фишек и возврат """
        tmp = list(range(1, 29))
        random.shuffle(tmp)

        if (self.examination_distribution(tmp) == True):
            return tmp
        else:
            return self.chip_distribution()

    def options(self, value, side):
        """Возможные варианты которые можно поставить"""
        tmp_lst = list([])
        if len(self.board) != 0:
            if side == 'left':
                for key in self.all_shtick:
                    if ((self.all_shtick[key][2] == self.all_shtick[self.board[0]][0]) and
                            (self.all_shtick[key] != self.all_shtick[self.board[0]])):
                        tmp_lst.append(key)
            elif side == 'right':
                for key in self.all_shtick:
                    if ((self.all_shtick[key][0] == self.all_shtick[self.board[-1]][2]) and
                            (self.all_shtick[key] != self.all_shtick[self.board[-1]])):
                        tmp_lst.append(key)
        return tmp_lst
    #
    def examination_number_shtics(self, number, key, side, variable):
        """Фишка была выбрана и теперь мы пытаемся ее ставить"""

        ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
        ##доску на экран чтобы он понимал куда можно поставить
        print('мы зашли в функцию')
        print(f"Какой номер из player берем {number}, какая фишка передается {key}, {variable}")
        for var in variable:
            if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == True:
                return (1, key + 28)
            if var[0][0] == number and var[0][1] == side and var[1] == True and var[2] == False:
                return (1, key)
            if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == True:
                return (2, key + 28)
            if var[0][0] == number and var[0][1] == side and var[1] == False and var[2] == False:
                return (2, key)

    def summ_points(self, player_first, player_second):
        """ Считаем количество очков"""
        count = 0
        for shtick in player_first.shticks:
            count += int(self.all_shtick[shtick][0]) + int(self.all_shtick[shtick][2])
            print(f"Какая фишка {self.all_shtick[shtick]}, Сумма очков {count}")
        for shtick in player_second.shticks:
            count += int(self.all_shtick[shtick][0]) + int(self.all_shtick[shtick][2])
            print(f"Какая фишка {self.all_shtick[shtick]}, Сумма очков {count}")
        return count

    def scoring_eligibility_check(self, summ_one, summ_two):
        if self.point_team_one == 0 and (summ_one > 12 or summ_two > 12):
            return True
        else:
            return False
        return True

    def dont_end_round(self, passes, number_of_player, players):
        """ Проверяем кончился ли раунд?"""
        # Проверяем рыбу
        print("Проверяем конец раунда")
        team_one = self.summ_points(players[0], players[2])
        team_two = self.summ_points(players[1], players[3])
        if passes == 4:
            print('Проверяем рыбу')
            self.number_first_move = number_of_player + 1
            self.count_round += 1
            if self.scoring_eligibility_check(team_one, team_two):
                if team_one == team_two:
                    self.point_team_one += team_one
                    self.point_team_two += team_two
                elif team_one > team_two:
                    self.point_team_one += team_one
                elif team_one < team_two:
                    self.point_team_two += team_two
            return True

        ## Проверяем конец раунда в целом
        for count in range(0, 4):
            print('ну что же, мы внутри')
            if len(players[count].shticks) == 0:
                print(f"номер игрока {count}, сам игрок {players[count].name}")
                self.number_first_move = count + 1
                self.count_round += 1
                print(f"номер следущего раунда: {self.count_round}")
                if self.scoring_eligibility_check(team_one, team_two):
                    if count == 0 or count == 2:
                        self.point_team_two += team_two
                    elif count == 1 or count == 3:
                        self.point_team_one += team_one
                return True

        return False

    def possible_chips_that_can_be_placed(self, player):
        """ Отслеживаем номер фишки и куда ее поставить"""

        ## Здесь можно поставить фишку и справа, и слева, поэтому надо предлагать игроку какой-то выбор и выводить
        ##доску на экран чтобы он понимал куда можно поставить
        lst_possible = list([])
        # lst_tmp = list([])
        # Это условие для нового раунда и чел может поставить что хочет
        if len(self.board) == 0:
            for elem in player.shticks:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
            return lst_possible

        options_on_the_left = self.options(self.board[0], 'left')
        options_on_the_right = self.options(self.board[-1], 'right')
        #         print('Номера, которые можно поставить слева', options_on_the_left)
        #         print('Номера, которые можно поставить справа', options_on_the_right)

        for elem in player.shticks:
            if elem in options_on_the_left and elem in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, False])
            elif elem in options_on_the_left:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, False])
            elif elem in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, False])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, False])

        for elem in player.shticks:
            if elem + 28 in options_on_the_left and elem + 28 in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, True])
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, True])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, True])
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, True])
            elif elem + 28 in options_on_the_left:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'left'], True, True])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'left'], False, True])
            elif elem + 28 in options_on_the_right:
                if elem in self.doubles:
                    lst_possible.append([[player.shticks.index(elem), 'right'], True, True])
                else:
                    lst_possible.append([[player.shticks.index(elem), 'right'], False, True])
        if len(lst_possible) == 0:
            return ([[], None, None])
        return lst_possible

    def put_a_chip(self, number_of_player, players):
        """ Выбор фишки, которую можно поставить"""
        if self.count_round == 1 and 8 not in self.board:
            n = players[number_of_player].shticks.index(8)
            return [[[n, 'right'], True, False], [[n, 'left'], True, False]]
        else:
            return self.possible_chips_that_can_be_placed(players[number_of_player])

    def dont_end_game(self):
        if self.point_team_one >= Game.min_of_end_point:
            return 'two'
        elif self.point_team_two >= Game.min_of_end_point:
            return 'one'

    def exam_point(self, key, number):
        if number == 1:
            if self.all_shtick[key][0] == '0':
                return False
            else:
                return True
        if number == 2:
            if self.all_shtick[key][2] == '0':
                return False
            else:
                return True






