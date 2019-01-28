from random import randint
import queue

class Board:

    #-1 is a bomb

    def __init__(self, size, mine_size):
        self.size = int(size)
        self.mine_size = mine_size
        self.field = [[0 for x in range(self.size)]
                      for y in range(self.size)]

        self.visibility = [[0 for x in range(self.size)]
                           for y in range(self.size)]

        self.bombs = list()

        count_mines = 1
        while count_mines <= mine_size:
            x = randint(0, self.size-1)
            y = randint(0, self.size-1)
            if self.field[x][y] == 0:
                self.bombs.append((x, y))
                self.field[x][y] = -1
                count_mines += 1

        self._set_clues()

        self.status = 'running'

    def _set_clues(self):
        for b in self.bombs:
            (row_i, col_i) = b
            for i in range(row_i - 1, row_i + 2):
                for j in range(col_i - 1, col_i + 2):
                    if (0 <= i < self.size and 0 <= j < self.size
                                and self.field[i][j] != -1):
                        self.field[i][j] += 1

    def _show_clues(self, x, y):
        to_check = queue.Queue()
        if self.field[x][y] == 0:
            self.visibility[x][y] = 1
            to_check.put((x, y))
        while not to_check.empty():
            (current_i, current_j) = to_check.get()
            for i in range(current_i - 1, current_i + 2):
                for j in range(current_j - 1, current_j + 2):
                    if 0 <= i < self.size and 0 <= j < self.size and self.field[i][j]  == 0 and self.visibility[i][j] == 0:
                        self.visibility[i][j] = 1
                        to_check.put((i, j))

    def _is_winner(self):
        count = 0
        for i in range(0, self.size):
            for j in range(0,self.size):
                if self.visibility[i][j] == 1:
                    count = count + 1
        if count + self.mine_size == self.size*self.size:
            return True
        else:
            return False

    def move(self, x, y):
        if x < 0 or x >= self.size:
            return self.print_game()
        if y < 0 or y >=self.size:
            return self.print_game()
        if self.visibility[x][y] == 1:
            print("choose another one don't afraid")
            return self.print_game()
        if self.field[x][y] == -1:
            self.status = "lose"
            return self.__str__()

        self.visibility[x][y] = 1
        if self._is_winner():
            self.status = "winner"
            return self.print_game()
        else:
            self._show_clues(x, y)
            return self.print_game()

    def build_header(self):
        result = ""
        for i in range(self.size//2):
            result += "#"
        result += " Game Status: " + self.status + " "
        for i in range(self.size//2):
            result += "#"
        return result + "\n"

    def build_footer(self):
        result = ""
        for i in range(self.size*5):
            result += "#"
        return result + "\n"

    def print_game(self):
        if self.status == "lose":
            print("You lose, try again")
            return self.__str__()

        result = self.build_header()
        for x in range(0, self.size):
            tmp = ""
            for y in range(0, self.size):
                if  self.visibility[x][y] == 1:
                    tmp += " {:2} ".format(self.field[x][y])
                else:
                    tmp += " {:1} ".format("[]")
            result += tmp + '\n'
        result += self.build_footer()
        return result

    def __str__(self):
        result = self.build_header()
        for x in range(0, self.size):
            tmp = ""
            for y in range (0, self.size):
                if self.field[x][y] == -1:
                    tmp += " {} ".format("[x]")
                else:
                    tmp += " {:3} ".format(self.field[x][y])
            result += tmp + '\n'

        result += self.build_footer()
        return result
