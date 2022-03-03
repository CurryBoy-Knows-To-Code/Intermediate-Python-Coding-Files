import math
import random


class Player():
	def __init__(self, players_letter):
		self.players_letter = players_letter

	def get_move(self, game):
		pass


class Human_Player(Player):
	def __init__(self, players_letter):
		super().__init__(players_letter)

	def get_move(self, game):
		valid_players_square = False
		val = None
		while not valid_players_square:
			players_square = input(self.players_letter + '\'s turn. Input move (0-8): ')
			try:
				val = int(players_square)
				if val not in game.available_moves():
					raise ValueError
				valid_players_square = True
			except ValueError:
				print('Invalid players_square. Try again.')
		return val


class Smart_Computer_Player(Player):
	def __init__(self, players_letter):
		super().__init__(players_letter)

	def get_move(self, game):
		if len(game.available_moves()) == 9:
			players_square = random.choice(game.available_moves())
		else:
			players_square = self.minimax(game, self.players_letter)['position']
		return players_square

	def minimax(self, state, player):
		max_player = self.players_letter  # yourself
		other_player = 'O' if player == 'X' else 'X'
		# first we want to check if the previous move is a winner
		if state.current_winner == other_player:
			return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
		elif not state.empty_squares():
			return {'position': None, 'score': 0}
		if player == max_player:
			best = {'position': None, 'score': -math.inf}  # each score should maximize
		else:
			best = {'position': None, 'score': math.inf}  # each score should minimize
		for possible_move in state.available_moves():
			state.make_move(possible_move, player,None)
			sim_score = self.minimax(state, other_player)  # simulate a game after making that move
			# undo move
			state.game_board[possible_move] = ' '
			state.current_winner = None
			sim_score['position'] = possible_move  # this represents the move optimal next move
			if player == max_player:  # X is max player
				if sim_score['score'] > best['score']:
					best = sim_score
			else:
				if sim_score['score'] < best['score']:
					best = sim_score
		return best


