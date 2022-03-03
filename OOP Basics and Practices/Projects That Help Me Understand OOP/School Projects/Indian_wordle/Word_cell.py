import pygame

pygame.font.init()
font = pygame.font.Font("freesansbold.ttf",40)
class WordCell:

	def __init__(self, row, column):
		self.row = row
		self.column = column
		self.x_pos = (column + 1) * 80 - 25
		self.y_pos = (row + 1) * 80 + 50
		self.size = 70
		self._chosen_letter = None
		self._colour = None
		


	def set_chosen_letter(self, assigned_letter):
		self._chosen_letter = assigned_letter

	def cancel_letter(self):
		self._chosen_letter = None

	def set_colour(self, new_colour):
		self._colour = new_colour

	def draw_sq(self, game_window):
		
		# this is for while sq itself
		pygame.draw.rect(game_window,(54, 54 ,54), (self.x_pos, self.y_pos, self.size, self.size))
		pygame.draw.rect(game_window, self._colour, (self.x_pos + 2, self.y_pos + 2, self.size - 4, self.size - 4))
		if self._chosen_letter != None:
			txt = font.render(self._chosen_letter,False, (255,255,255))
			game_window.blit(txt,(self.x_pos + 20, self.y_pos + 19))