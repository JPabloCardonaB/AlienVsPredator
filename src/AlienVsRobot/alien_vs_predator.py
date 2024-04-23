import sys
sys.path.append('src/')

from random import randint
from doubly_linked_list import DoublyLinkedList

class AlienVsPredator:
    def __init__(self):
        '''        self.row_1 = DoublyLinkedList()
                self.row_1.append('+')
                self.row_1.append('+')
                self.row_1.append('+')
                self.row_1.append('+')
                self.row_2 = DoublyLinkedList()
                self.row_2.append('👽')
                self.row_2.append(' ')
                self.row_2.append(' ')
                self.row_2.append(' ')
                self.row_3 = DoublyLinkedList()
                self.row_3.append('🤖')
                self.row_3.append(3)
                self.row_3.append(3)
                self.row_3.append(3)
                self.row_4 = DoublyLinkedList()
                self.row_4.append(4)
                self.row_4.append(4)
                self.row_4.append(4)
                self.row_4.append(0)
                self.game_board = DoublyLinkedList()
                self.game_board.append(self.row_1)
                self.game_board.append(self.row_2)
                self.game_board.append(self.row_3)
                self.game_board.append(self.row_4)

'''
    
        self.game_board = DoublyLinkedList()

    def show_game_board(self):
        for row in self.game_board:
            print(row)

    def create_game_board(self, difficulty, board_size: tuple):

        rows = board_size[0]
        columns = board_size[1]
        difficulty_percentage : float = 0

        #Contiene la cantidad de casillas que ocuparán los porcentajes de la dificultades
        if difficulty == 1:
            difficulty_percentage = 0.40
        elif difficulty == 2:
            difficulty_percentage = 0.60
        elif difficulty == 3:
            difficulty_percentage = 0.75
        
        difficult_level : int = round((rows * columns) * difficulty_percentage)
        amount_operators : int = 0
        
        # Este ciclo rellena todas las posiciones del tablero con '-'

        for i in range(0,rows,1):
            row = DoublyLinkedList()
            for j in range(0,columns,1):
                row.append(' ')
            
            self.game_board.append(row)

        



    # Retorna el porcentaje de los operadores en el game board segun la dificultad
    def manage_difficulty(self, difficulty):
        pass

AVS = AlienVsPredator()
AVS.create_game_board(difficulty=1,board_size=(4,4))
AVS.show_game_board()

