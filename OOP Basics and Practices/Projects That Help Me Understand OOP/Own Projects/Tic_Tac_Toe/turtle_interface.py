# this file is for the board layout, board nums, and main menu
import turtle
import time
screen = turtle.Screen()
screen.setup(1845,450)
turtle.title("Tic Tac Toe")

class Main_Interface:
	
	def __init__(self):
		self.main_pen = turtle.Turtle(visible = False)
		self.main_pen.speed(10)
		self.main_pen.pensize(10)

	def clear_screen(self):
		self.main_pen.clear()

	def board_layout(self):
		self.main_pen.penup()
		self.main_pen.goto(-205,220)
		self.main_pen.pendown()
		# this is for drawing the border
		for _ in range(4):
			self.main_pen.forward(415)
			self.main_pen.right(90)
		# this is vertical borders
		self.main_pen.penup()
		self.main_pen.goto(-70,220)
		self.main_pen.pendown()
		self.main_pen.right(90)
		self.main_pen.forward(415)
		self.main_pen.penup()
		self.main_pen.goto(70,220)
		self.main_pen.pendown()
		self.main_pen.forward(415)
		# this is for horizontal borders
		self.main_pen.penup()
		self.main_pen.goto(-205,80)
		self.main_pen.pendown()
		self.main_pen.left(90)
		self.main_pen.forward(415)
		self.main_pen.penup()
		self.main_pen.goto(-205,-60)
		self.main_pen.pendown()
		self.main_pen.forward(415)

	def available_board_nums(self):
		self.main_pen.penup()
		self.main_pen.goto(600,175)
		self.main_pen.pendown()
		self.main_pen.write("Available board numbers", align = "center",font = ("Verdana",20, "normal"))
		self.main_pen.penup()
		self.main_pen.goto(450,150)
		self.main_pen.pendown()
		for _ in range(4):
			self.main_pen.forward(300)
			self.main_pen.right(90)
		# this is for drawing vertical borders
		self.main_pen.penup()
		self.main_pen.goto(650,150)
		self.main_pen.pendown()
		self.main_pen.right(90)
		self.main_pen.forward(300)
		self.main_pen.penup()
		self.main_pen.goto(550,150)
		self.main_pen.pendown()
		self.main_pen.forward(300)
			# this is for drawing the horizontel borders
		self.main_pen.penup()
		self.main_pen.goto(450,50)
		self.main_pen.pendown()
		self.main_pen.left(90)
		self.main_pen.forward(300)
		self.main_pen.penup()
		self.main_pen.goto(450,-50)
		self.main_pen.pendown()
		self.main_pen.forward(300)
		self._draw_numbers()
			
	def _draw_numbers(self):
		self.main_pen.penup()
		self.main_pen.goto(500,75)
		self.main_pen.pendown()
		self.main_pen.write("0", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 1
		self.main_pen.penup()
		self.main_pen.goto(600,75)
		self.main_pen.pendown()
		self.main_pen.write("1", align = "center",font = ("Verdana",35, "normal")) 
		# this is for drawing num 2
		self.main_pen.penup()
		self.main_pen.goto(700,75)
		self.main_pen.pendown()
		self.main_pen.write("2", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 3
		self.main_pen.penup()
		self.main_pen.goto(500,-25)
		self.main_pen.pendown()
		self.main_pen.write("3", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 4
		self.main_pen.penup()
		self.main_pen.goto(600,-25)
		self.main_pen.pendown()
		self.main_pen.write("4", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 5
		self.main_pen.penup()
		self.main_pen.goto(700,-25)
		self.main_pen.pendown()
		self.main_pen.write("5", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 6
		self.main_pen.penup()
		self.main_pen.goto(500,-125)
		self.main_pen.pendown()
		self.main_pen.write("6", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 7
		self.main_pen.penup()
		self.main_pen.goto(600,-125)
		self.main_pen.pendown()
		self.main_pen.write("7", align = "center",font = ("Verdana",35, "normal"))
		# this is for drawing num 8
		self.main_pen.penup()
		self.main_pen.goto(700,-125)
		self.main_pen.pendown()
		self.main_pen.write("8", align = "center",font = ("Verdana",35, "normal"))
		
	def update_available_nums(self, players_chosen_number):
		if players_chosen_number == 0:
			self._fill_square(450,150)
		elif players_chosen_number == 1:
			self._fill_square(550,150)
		elif players_chosen_number == 2:
			self._fill_square(650,150)
		elif players_chosen_number == 3:
			self._fill_square(450,50)
		elif players_chosen_number == 4:
			self._fill_square(550,50)
		elif players_chosen_number == 5:
			self._fill_square(650,50)
		elif players_chosen_number == 6:
			self._fill_square(450,-50)
		elif players_chosen_number == 7:
			self._fill_square(550,-50)
		elif players_chosen_number == 8:
			self._fill_square(650,-50)

	def _fill_square(self, x_cordinate, y_cordinate):
		self.main_pen.penup()
		self.main_pen.begin_fill()
		self.main_pen.goto(x_cordinate, y_cordinate)
		self.main_pen.pendown()
		for _ in range(4):
			self.main_pen.forward(100)
			self.main_pen.right(90)
		self.main_pen.end_fill()
		screen.update()

	def show_game_title(self):
		turtle.Screen().clear()
		self.main_pen.penup()
		self.main_pen.goto(0,100)
		self.main_pen.pendown()
		self.main_pen.write("Welcome to my", align = "center",font = ("verdana",75, "normal"))
		self.main_pen.penup()
		self.main_pen.goto(10,0)
		self.main_pen.pendown()
		self.main_pen.write("Tic Tac Toe game !", align = "center",font = ("verdana",75, "normal"))
		time.sleep(3)

	def player_game_mode(self):
		self.main_pen.clear()
		self.main_pen.penup()
		self.main_pen.goto(0,100)
		self.main_pen.pendown()
		self.main_pen.write("Which game mode do you want to play", align = "center",font = ("verdana",50,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(0,50)
		self.main_pen.pendown()
		self.main_pen.write("Press 1 if you want to play against Christopher Crippen",align = "center",font = ("verdana",25,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(-81,0)
		self.main_pen.pendown()
		self.main_pen.write("Press 2 if you want to play against your friend",align = "center",font = ("verdana",25,"normal"))

	def invalid_input(self):
		self.main_pen.clear()
		self.main_pen.penup()
		self.main_pen.goto(0,100)
		self.main_pen.pendown()
		self.main_pen.write("Are you an idiot,", align = "center",font = ("verdana",75, "normal"))
		self.main_pen.penup()
		self.main_pen.goto(-10,0)
		self.main_pen.pendown()
		self.main_pen.write("just do what the question says", align = "center",font = ("verdana",75, "normal"))
		time.sleep(3)


	def ask_player_name(self, letter):
		self.main_pen.clear()
		string = f"What is your name player {letter}"
		self.main_pen.penup()
		self.main_pen.goto(-10,0)
		self.main_pen.pendown()
		self.main_pen.write(string, align = "center",font = ("verdana",75, "normal"))

	
	def ask_chosen_colours(self, letter):
		self.main_pen.clear()
		string = f"Which colour do you choose player {letter}"
		self.main_pen.penup()
		self.main_pen.goto(-10,150)
		self.main_pen.pendown()
		self.main_pen.write(string, align = "center",font = ("verdana",35, "normal"))
		self._show_available_colours()

	def _show_available_colours(self):
		self.main_pen.penup()
		self.main_pen.goto(-10,90)
		self.main_pen.pendown()
		self.main_pen.color("red")
		self.main_pen.write("Press 1 for the colour RED", align = "center", font = ("verdana",20,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(-5,50)
		self.main_pen.pendown()
		self.main_pen.color("blue")
		self.main_pen.write("Press 2 for the colour BLUE", align = "center", font = ("verdana",20,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(8,10)
		self.main_pen.pendown()
		self.main_pen.color("green")
		self.main_pen.write("Press 3 for the colour GREEN", align = "center", font = ("verdana",20,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(10,-30)
		self.main_pen.pendown()
		self.main_pen.color("purple")
		self.main_pen.write("Press 4 for the colour PURPLE", align = "center", font = ("verdana",20,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(15,-70)
		self.main_pen.pendown()
		self.main_pen.color("orange")
		self.main_pen.write("Press 5 for the colour ORANGE", align = "center", font = ("verdana",20,"normal"))
		self.main_pen.penup()
		self.main_pen.goto(8,-110)
		self.main_pen.pendown()
		self.main_pen.color("brown")
		self.main_pen.write("Press 6 for the colour BROWN", align = "center", font = ("verdana",20,"normal"))
		self.main_pen.color("black")

	

	def tell_its_draw(self):
		turtle.Screen().clear()
		self.main_pen.home()
		self.main_pen.write("HAHAHA it is a draw !!", align = "center",font = ("Verdana",50, "normal"))
		time.sleep(2)







class Player_Interface:
	# constructor
	def __init__(self, players_colour, player_name):
		self.player_pen = turtle.Turtle(visible = False)
		self.player_pen.pencolor(players_colour)
		self.player_name = player_name
		self.player_pen.speed(10)
		self.player_pen.pensize(10)

	def identify_player(self):
		self.player_pen.penup()
		if self.__class__.__name__ == "X_Drawer":
			x_str = "X Player = {}".format(self.player_name)
			self.player_pen.goto(-900,100)
			self.player_pen.write(x_str, align = "left",font = ("Verdana", 20, "normal"))
		elif self.__class__.__name__ == "O_Drawer":
			o_str = "O Player = {}".format(self.player_name)
			self.player_pen.goto(-900,0)
			self.player_pen.write(o_str, align = "left", font = ("Verdana", 20, "normal"))


	def draw_winning_row_line(self, row_num):
		if row_num == 0:
			y_cordinate = 150
		elif row_num == 1:
			y_cordinate = 10
		elif row_num == 2:
			y_cordinate = -130
		self.player_pen.penup()
		self.player_pen.goto(-205,y_cordinate)
		self.player_pen.pendown()
		self.player_pen.forward(415)
		time.sleep(2)
		self._show_winner()
		
	def draw_winning_column_line(self, col_num):
		if col_num == 0:
			x_cordinate = -140
		elif col_num == 1:
			x_cordinate = 0
		elif col_num == 2:
			x_cordinate = 140
		self.player_pen.right(90)
		self.player_pen.penup()
		self.player_pen.goto(x_cordinate,220)
		self.player_pen.pendown()
		self.player_pen.forward(415)
		time.sleep(2)
		self._show_winner()

	def draw_winning_diagonal_line(self, diag_num): 
		self.player_pen.penup()
		if diag_num == 1:
			self.player_pen.goto(-205,220)
			self.player_pen.pendown()
			self.player_pen.goto(215,-200)
		elif diag_num == 2:
			self.player_pen.goto(205,215)
			self.player_pen.pendown()
			self.player_pen.goto(-215,-200)
		time.sleep(2)
		self._show_winner()
		
	def _show_winner(self):
		turtle.Screen().clear()
		string = "{} wins the game".format(self.player_name)
		self.player_pen.home()
		self.player_pen.write(string, align = "center",font = ("Verdana",50, "normal"))
		time.sleep(2)



class X_Drawer(Player_Interface):
	
	def update_game_board(self,players_chosen_number):
		if players_chosen_number == 0:
			self._write_X(-140,50)
		elif players_chosen_number == 1:
			self._write_X(0,50)
		elif players_chosen_number == 2:
			self._write_X(140,50)
		elif players_chosen_number == 3:
			self._write_X(-140,-90)
		elif players_chosen_number == 4:
			self._write_X(0,-90)
		elif players_chosen_number == 5:
			self._write_X(140,-90)
		elif players_chosen_number == 6:
			self._write_X(-140,-225)
		elif players_chosen_number == 7:
			self._write_X(0,-225)
		elif players_chosen_number == 8:
			self._write_X(140,-225)

	def _write_X(self, x_cordinate, y_cordinate):
		self.player_pen.penup()
		self.player_pen.goto(x_cordinate, y_cordinate)
		self.player_pen.pendown()
		self.player_pen.write("X",align = "center",font = ("Verdana",120, "normal"))
		screen.update()
	
		
class O_Drawer(Player_Interface):
	
	def update_game_board(self,players_chosen_number):
		if players_chosen_number == 0:
			self._write_O(-140,50)
		elif players_chosen_number == 1:
			self._write_O(0,50)
		elif players_chosen_number == 2:
			self._write_O(140,50)
		elif players_chosen_number == 3:
			self._write_O(-140,-90)
		elif players_chosen_number == 4:
			self._write_O(0,-90)
		elif players_chosen_number == 5:
			self._write_O(140,-90)
		elif players_chosen_number == 6:
			self._write_O(-140,-225)
		elif players_chosen_number == 7:
			self._write_O(0,-225)
		elif players_chosen_number == 8:
			self._write_O(140,-225)

	def _write_O(self, x_cordinate, y_cordinate):
		self.player_pen.penup()
		self.player_pen.goto(x_cordinate, y_cordinate)
		self.player_pen.pendown()
		self.player_pen.write("O",align = "center",font = ("Verdana",120, "normal"))
		screen.update()
		