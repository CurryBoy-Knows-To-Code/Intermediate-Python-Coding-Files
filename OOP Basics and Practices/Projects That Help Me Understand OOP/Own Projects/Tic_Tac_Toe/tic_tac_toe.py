import math
import random
from player import Human_Player, Smart_Computer_Player
from turtle_interface import Main_Interface, X_Drawer, O_Drawer

# main class
class Tic_Tac_Toe:
	def __init__(self):
		self.game_board = self.create_board()
		self.current_winner = None
	# the static method basically changes the functionality of the method to a normal function which means it wont take a instance or a class as a arguement
	@staticmethod
	def create_board():
		return[" " for _ in range(9)]
	
	def show_board(self):
		# here we create a row wich looks like this |  |  |  |, another 2 below 
		for row in [self.game_board[i*3:(i+1)*3] for i in range(3)]:
			print("| " + " | ".join(row) + " |")

	@staticmethod
	def show_board_nums():
		# here it is the samee thing as the show_board method but the squares are instead filled with numbers ranging from 0 to 8 from left to right 
		for row in [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]:
			print("| " + " | ".join(row) + " |")
	
	def make_move(self, players_square, players_letter, main_interface, *args):
		# here we check if the chosen square of the player is empty and if it is empty then we replace the empty square with the player's letter, after that we check if the player has won
		if len(args) == 0:
			use_interface = False
		else:
			player = Tic_Tac_Toe._get_instance(players_letter, *args)
			use_interface = True
		if self.game_board[players_square] == " ":
			if use_interface:
				player.update_game_board(players_square)
				main_interface.update_available_nums(players_square)
			else:
				pass
			self.game_board[players_square] = players_letter
			if self.check_winner(players_square, players_letter, *args):
				self.current_winner = players_letter
			return True
		return False

	@staticmethod
	def _get_instance(players_letter, *args):
		if players_letter == "X":
			return args[0]
		else:
			return args[1]
		
	def check_winner(self, players_square, players_letter, *args):
		if len(args) == 0:
			use_interface = False
		else:
			player = Tic_Tac_Toe._get_instance(players_letter, *args)
			use_interface = True
		# check the row
		row_ind = math.floor(players_square / 3)
		row = self.game_board[row_ind*3:(row_ind+1)*3]
		if all([s == players_letter for s in row]):
			if use_interface:
				player.draw_winning_row_line(row_ind)
				return True
			else:
				return True
		col_ind = players_square % 3
		column = [self.game_board[col_ind+i*3] for i in range(3)]
		if all([s == players_letter for s in column]):
			if use_interface:
				player.draw_winning_column_line(col_ind)
				return True
			else:
				return True
		if players_square % 2 == 0:
			diagonal1 = [self.game_board[i] for i in [0, 4, 8]] 
			if all([s == players_letter for s in diagonal1]):
				if use_interface:
					player.draw_winning_diagonal_line(1)
					return True
				else:
					return True
			diagonal2 = [self.game_board[i] for i in [2, 4, 6]]
			if all([s == players_letter for s in diagonal2]):
				if use_interface:
					player.draw_winning_diagonal_line(2)
					return True
				else:
					return True
		return False

	def empty_squares(self):
		return " " in self.game_board

	def num_empty_squares(self):
		return self.game_board.count(" ")

	def available_moves(self):
		# the enumerate keep a track of how many times it has looped
		return [i for i, empty_spot in enumerate(self.game_board) if empty_spot == " "]

		
def execute_Tic_Tac_Toe(game, main_interface, X_player, X_drawer, O_player, O_drawer, print_game = True):
	
	if print_game:
		main_interface.clear_screen()
		main_interface.board_layout()
		main_interface.available_board_nums()
		X_drawer.identify_player()
		O_drawer.identify_player()
	players_letter = "X"
	while game.empty_squares():
		if players_letter == "O":
			players_square = O_player.get_move(game)
		else:
			players_square = X_player.get_move(game)
		if game.make_move(players_square, players_letter, main_interface, X_drawer, O_drawer):
			if print_game:
				print(players_letter + " makes a move to square {}".format(players_square))
				print("")
			if game.current_winner:
				if print_game:
					main_menu()
				# here we end the loop and exit the game
				return players_letter
			# here we switch players
			players_letter = "O" if players_letter == "X" else "X"
		# add delay to make it more nice
	if print_game:
		main_interface.tell_its_draw()
		main_menu()


def get_player_name(letter, main_interface):
	print()
	while True:
		main_interface.ask_player_name(letter)
		player_name = input("Enter your name here\n")
		check_string = player_name.replace(" ","")
		if (check_string.isalpha()) and (len(player_name) <=21):
			return player_name
		else:
			main_interface.invalid_input()
			


def players_pen_colour(list_of_colours, letter, main_interface):
	print()
	while True:
		try:
			main_interface.ask_chosen_colours(letter)
			users_choice = int(input("Choose your number here\n")) 
			if users_choice <= 0 or users_choice >=7:
				raise ValueError
			else:
				return list_of_colours[users_choice - 1]
		except ValueError:
			main_interface.invalid_input()

def against_AI(list_of_colours, main_interface, game):
	x_name = get_player_name("X", main_interface)
	x_colour = players_pen_colour(list_of_colours,"X",main_interface)
	x_player = Human_Player("X")
	x_drawer = X_Drawer(x_colour, x_name)
	o_colour = list_of_colours[random.randint(0,5)]
	o_player = Smart_Computer_Player("O")
	o_drawer = O_Drawer(o_colour,"Christopher Crippen")
	execute_Tic_Tac_Toe(game, main_interface, x_player, x_drawer, o_player, o_drawer, print_game = True)

def two_players(list_of_colours, main_interface, game):
	x_name = get_player_name("X", main_interface)
	x_colour = players_pen_colour(list_of_colours,"X", main_interface)
	x_player = Human_Player("X")
	x_drawer = X_Drawer(x_colour, x_name)
	o_name = get_player_name("O", main_interface)
	o_colour = players_pen_colour(list_of_colours,"O", main_interface)
	o_player = Human_Player("O")
	o_drawer = O_Drawer(o_colour, o_name)
	execute_Tic_Tac_Toe(game, main_interface, x_player, x_drawer, o_player, o_drawer, print_game = True)

def main_menu():
	game = Tic_Tac_Toe()
	main_interface = Main_Interface()
	list_of_colours = ["red","blue","green","purple","orange","brown"]
	# interface works in this func
	main_interface.show_game_title()
	valid = False
	while not valid:
		main_interface.player_game_mode()
		users_choice = input("Which number do you choose\n")
		if users_choice == "1":
			valid = True
			against_AI(list_of_colours, main_interface, game)
		elif users_choice == "2":
			valid = True
			two_players(list_of_colours, main_interface, game)
		else:
			main_interface.invalid_input()
		
if __name__ == '__main__':
	main_menu()