#1 ---тут есть вопросы---
import datetime
class Calendar ():
    def __init__ (self):
    #     self.name = name
    #     self.date_ev = date_ev
        self.ev=[]

    def add_Event (self, event_n, event_date):
        event = {
            'name':event_n,
            'date':event_date
        }
        self.ev.append(event)
    
    def show_event(self, event_date):
        for i in self.ev:
            if i['date'] == event_date:
                print(i['name'])

calendar = Calendar()
calendar.add_Event("HB", datetime(2022, 11, 15).date())
calendar.show_event(datetime(2022, 11, 15).date())

#2
class InventoryItem():
    def __init__(self, tovar_name, count, price):
        self.tovar_name=tovar_name
        self.count=count
        self.price=price

    def Uvel_count_tov(self,count_uv):
        self.count= self.count+count_uv
        price= self.price*self.count 
        print (self.count, price)

    def Umensh_count_tov(self,count_um):
        self.count= self.count-count_um
        print (self.count)
        price= self.price*self.count 
        print (self.count, price)

inver = InventoryItem('kkk',15,20)
inver.Uvel_count_tov(10)
inver.Umensh_count_tov(5)

#3 не получилось с крестиками и ноликами с интернета задача
class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-----")

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.current_player = "O" if self.current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    def check_winner(self):
      
        for row in self.board:
            if row[0] != " " and row[0] == row[1] == row[2]:
                return row[0]

      
        for col in range(3):
            if self.board[0][col] != " " and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]

        
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != " " and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return None

    def is_draw(self):
        for row in self.board:
            if " " in row:
                return False
        return True
game = TicTacToe()

while True:
    game.print_board()
    row = int(input("Enter the row number (0-2): "))
    col = int(input("Enter the column number (0-2): "))
    game.make_move(row, col)

    winner = game.check_winner()
    if winner:
        print("Player", winner, "wins!")
        break

    if game.is_draw():
        print("It's a draw!")
        break

        