import sys
sys.path.append('src/')

from doubly_linked_list import DoublyLinkedList

class AlienVsPredator:
    def __init__(self):
        self.row_1 = DoublyLinkedList()
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


    def show_game_board(self):
        for row in self.game_board:
            print(row)

    def create_game_board(self, difficulty, board_size: tuple):
        pass

    # Retorna el porcentaje de los operadores en el game board segun la dificultad
    def manage_difficulty(self, difficulty):
        pass

AVS = AlienVsPredator()
print(AVS)
print(AVS.show_board())