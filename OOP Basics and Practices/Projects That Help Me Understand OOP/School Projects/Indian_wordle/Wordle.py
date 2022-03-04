# optimisation of code is important but readability is also important, a balance between the two is the best type of code
# importing modules
import pygame
import random
import time
from Word_cell import WordCell
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 22)
# all the colours we use
BG_COLOUR, GREY, YELLOW, GREEN, WHITE = (18, 18, 20),(54, 54, 54),(177, 159, 59),(91, 141, 74),(211, 218, 224)


class Wordle:
    def __init__(self, WIDTH, HEIGHT):
        # initialise variables
        self.game_window = pygame.display.set_mode((WIDTH, HEIGHT))
        # a 2d list that has 30 obj of wordcell to keep track of specific cells
        self.grid = [[WordCell(row, column)for column in range(5)] for row in range(6)]
        self.word_of_the_day = self.get_or_check_random_word()
        self.word_of_the_day_list = [letter for letter in self.word_of_the_day if letter.strip()]
        # this will append each input from keyboard that is valid
        self.players_input_list = []
        # this will track the cells index so that it can be accessed later
        self.tracking_row = 0
        self.tracking_column = 0
        self.running = True
        self.won = False

    @staticmethod
    def get_or_check_random_word(*inputted_word):
        random_words = open("list_of_rnd_words.txt").read().splitlines()
        # getting random word
        if len(inputted_word) == 0: return random.choice(random_words).upper()
        # checking if inputted word exists in a list
        return True if inputted_word[0].lower() in random_words else False

    def draw_initial_layout(self):
        # rgb val of col
        pygame.display.set_caption("INDIAN WORDLE")
        self.game_window.fill((BG_COLOUR))
        for row in self.grid:
            for cell in row:
                # drawing the grid
                cell.set_colour(BG_COLOUR)
                cell.draw_sq(self.game_window)
        pygame.display.update()

    def show_ending(self):
        message = f"Congratulations! The word was {self.word_of_the_day}" if self.won else f"YOU LOST!!!!!, the word was {self.word_of_the_day}"
        message_screen = font.render(message, False, (WHITE))
        self.game_window.blit(message_screen, (50, 620))
        pygame.display.update()
        time.sleep(5)

    def show_error_message(self, message):
        message_screen = font.render(message, False, (WHITE))
        self.game_window.blit(message_screen, (90, 620))
        pygame.display.update()
        time.sleep(2)
        message_screen = font.render(message, False, (BG_COLOUR))
        self.game_window.blit(message_screen, (90, 620))

    @staticmethod
    def validate_input(letter):
        available_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        return True if letter in available_letters else False

    def input_letter(self, letter):
        try:
            # the input is an int so we convert it to a string
            letter = chr(letter).upper()
            # validate the list and letter
            if len(self.players_input_list) >= 5 or not self.validate_input(letter): self.show_error_message("Invalid input")
            # inputting letter into list and cell
            else:
                self.players_input_list.append(letter)
                self.grid[self.tracking_row][self.tracking_column].set_chosen_letter(letter)
                self.grid[self.tracking_row][self.tracking_column].set_colour(BG_COLOUR)
                self.grid[self.tracking_row][self.tracking_column].draw_sq(self.game_window)
                pygame.display.update()
                self.tracking_column += 1
        # val error means invalid
        except ValueError: self.show_error_message("Invalid input")

    def remove_letter(self, letter):
        # same thing but removing the letter
        letter = chr(letter).upper()
        if len(self.players_input_list) == 0: self.show_error_message("There is no input")
        else:
            self.tracking_column -= 1
            self.players_input_list.pop(self.tracking_column)
            self.grid[self.tracking_row][self.tracking_column].cancel_letter()
            self.grid[self.tracking_row][self.tracking_column].draw_sq(
                self.game_window)
            pygame.display.update()

    def check_winner(self):
        player_word = "".join(letter for letter in self.players_input_list)
        # validating the list and word
        if (len(self.players_input_list) != 5 or self.get_or_check_random_word(player_word) == False): self.show_error_message("Not a 5 letter word")
        else:
            # making copies of the lists
            answer_list_copy = self.word_of_the_day_list.copy()
            list_of_current_colours = [GREY] * 5
            # this check if letter in correct position
            for i in range(5):
                if self.players_input_list[i] == answer_list_copy[i]:
                    list_of_current_colours[i] = GREEN
                    answer_list_copy[i] = None
                    self.players_input_list[i] = None
            # this check if they are in the list thingy
            for i in range(5):
                if (self.players_input_list[i] is not None and self.players_input_list[i] in answer_list_copy):
                    list_of_current_colours[i] = YELLOW
                    answer_list_copy[answer_list_copy.index(self.players_input_list[i])] = None


            for i in range(5):
                self.grid[self.tracking_row][i].set_colour(list_of_current_colours[i])
                self.grid[self.tracking_row][i].draw_sq(self.game_window)
                pygame.display.update()
                time.sleep(0.5)
            # ckecks if both lists are same
            if self.players_input_list == self.word_of_the_day_list:
                self.won = True
                self.show_ending()
                self.running = False
                pygame.quit()
            else:
                # show ending
                if self.tracking_row == 5:
                    self.show_ending()
                    self.running = False
                    pygame.quit()
                else:
                    self.players_input_list.clear()
                    # reset the column to 0 but increase the row by 1
                    self.tracking_row += 1
                    self.tracking_column = 0


def main(game):
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                pygame.quit()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: game.remove_letter(event.key)
                    elif event.key == pygame.K_RETURN: game.check_winner()
                    else: game.input_letter(event.key)
                else: continue


if __name__ == "__main__":
    game = Wordle(500, 700)
    game.draw_initial_layout()
    main(game)
