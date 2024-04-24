import sys
sys.path.append('src/')

from random import randint
from doubly_linked_list import DoublyLinkedList
from alien import Alien
from predator import Predator

class AlienVsPredator:

    def __init__(self):
        self.game_board = DoublyLinkedList()
        self.game_boar_size : tuple = None
        self.alien = Alien()
        self.predator = Predator()
        self.actual_turn = 1

    def show_game_board(self):
        for row in self.game_board:
            print(row)

    def create_game_board(self, difficulty, board_size: tuple):

        self.game_board_size = board_size

        rows = self.game_board_size[0]
        columns = self.game_board_size[1]
        
        # Este ciclo rellena todas las posiciones del tablero con ' '

        for i in range(0,rows,1):
            row = DoublyLinkedList()
            for j in range(0,columns,1):
                row.append(' ')
            self.game_board.append(row)

        self.change_difficulty(difficulty)
        self.set_predator_initial_position()

    # Retorna el porcentaje de los operadores en el game board segun la dificultad
    def get_difficulty_percentage(self, difficulty):
        
        difficulty_percentaje : float = 0
        
        #Contiene la cantidad de casillas que ocuparán los porcentajes de la dificultades

        if difficulty == 1:
            difficulty_percentage = 0.40
        elif difficulty == 2:
            difficulty_percentage = 0.60
        elif difficulty == 3:
            difficulty_percentage = 0.75

        return difficulty_percentage

    def change_difficulty(self,difficulty):
        

        difficulty_percentage = self.get_difficulty_percentage(difficulty)

        # Esta variable almacena la cantidad de operadores que se van a colocar en el tablero (+ y -)
        operator_amount: int = round(difficulty_percentage * (self.game_board_size[0] * self.game_board_size[1]))

        #print(operator_amount)
        while operator_amount > 0:
            
            row = randint(0,self.game_board_size[0] - 1)
            column = randint(0,self.game_board_size[1] - 1)
                             
            if self.game_board.get(row).value.get(column).value == ' ':
                random_number = randint(0,100)
                if random_number % 2 == 0:
                    self.game_board.get(row).value.remove(column)
                    self.game_board.get(row).value.insert('+', column)
                    operator_amount -= 1
                else:
                    self.game_board.get(row).value.remove(column)
                    self.game_board.get(row).value.insert('-', column)
                    operator_amount -= 1
    
    # Asigna la posicion del depredador en el tablero
    def set_predator_initial_position(self):
        while True:
            row = randint(0,self.game_board_size[0] - 1)
            column = randint(0,self.game_board_size[1] - 1)
    
            if self.game_board.get(row).value.get(column).value == ' ':
                self.game_board.get(row).value.remove(column)
                self.game_board.get(row).value.insert(self.predator,column)
                break

    # Asigna la posicion elegida del alien en el tablero
    def set_alien_position(self, row: int, column: int):

        if self.game_board.get(row).value.get(column).value == ' ':
            self.game_board.get(row).value.remove(column)
            self.game_board.get(row).value.insert(self.alien,column) 
        else:
            print('La casilla está ocupada o es inválida.')

    def get_predator_actual_position(self):
        for i in range(0,self.game_board_size[0],1):
            for j in range(0,self.game_board_size[1],1):
                if self.game_board.get(i).value.get(j).value == self.predator or self.game_board.get(i).value.get(j).value == f'{self.predator} {self.alien}':
                    return (i,j)
        return None
    
    def get_alien_actual_position(self):
        for i in range(0,self.game_board_size[0],1):
            for j in range(0,self.game_board_size[1],1):
                if self.game_board.get(i).value.get(j).value == self.alien or self.game_board.get(i).value.get(j).value == f'{self.predator} {self.alien}':
                    return (i,j)
        return None

    def make_predator_move_above(self, predator_position: tuple):

        '''
        Este metodo contiene las validaciones para los movimientos del predator en la direccion hacia arriba

        Parametros
        ---------
        predator_position: tuple
            Tupla que contiene indice de la fila y la columna que determinan la posicion del predator en el tablero

        '''
        
        # Valida si el predator se va a mover hacia una casilla vacia y le deje hacer el movimiento
        if self.game_board.get(predator_position[0]- 1).value.get(predator_position[1]).value == ' ':

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]) == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.insert(self.predator,predator_position[1])

            else:
                    
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.insert(self.predator,predator_position[1])

        # Evalua si hay un mas en la casilla hacia la que se va a mover y le suma 10 de vida al predator
        elif self.game_board.get(predator_position[0] - 1).value.get(predator_position[1]).value == '+':
            self.predator.increase_life(10)

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]) == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.insert(self.predator,predator_position[1])

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.insert(self.predator,predator_position[1])

        # Evalua si hay un menos en la casilla a la que se va a mover y le resta 10 vida al predator  
        elif self.game_board.get(predator_position[0] - 1).value.get(predator_position[1]).value == '-':
            self.predator.decrease_life(10)


            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]) == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.insert(self.predator,predator_position[1])

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] - 1).value.insert(self.predator,predator_position[1])

        #Evalua si esta el predator entra en la casilla del alien y le resta 25 de vida
        elif self.game_board.get(predator_position[0] -1).value.get(predator_position[1]) == self.alien:
            self.alien.decrease_life(25)
            self.game_board.get(predator_position[0]).value.remove(predator_position[1])
            self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
            self.game_board.get(predator_position[0] - 1).value.remove(predator_position[1])
            self.game_board.get(predator_position[0] - 1).value.insert((f'{self.predator} {self.alien}'),predator_position[1])

    def make_predator_move_below(self, predator_position: tuple):
        '''
        Este metodo contiene las validaciones para los movimientos del predator en la direccion hacia abajo

        Parametros
        ---------
        predator_position: tuple
            Tupla que contiene indice de la fila y la columna que determinan la posicion del predator en el tablero
        
        '''

        # Valida si el predator se va a mover hacia una casilla vacia y le deje hacer el movimiento
        if self.game_board.get(predator_position[0] + 1).value.get(predator_position[1]).value == ' ':

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.insert(self.predator,predator_position[1])
                
            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.insert(self.predator,predator_position[1])
                
        # Evalua si hay un mas en la casilla hacia la que se va a mover y le suma 10 de vida al predator
        elif self.game_board.get(predator_position[0] + 1).value.get(predator_position[1]).value == '+':
            self.predator.increase_life(10)

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.insert(self.predator,predator_position[1])

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.insert(self.predator,predator_position[1])

        # Evalua si hay un menos en la casilla a la que se va a mover y le resta 10 vida al predator  
        elif self.game_board.get(predator_position[0] + 1).value.get(predator_position[1]).value == '-':
            self.predator.decrease_life(10)
            
            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.insert(self.predator,predator_position[1])

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
                self.game_board.get(predator_position[0] + 1).value.insert(self.predator,predator_position[1])

        #Evalua si esta el predator entra en la casilla del alien y le resta 25 de vida
        elif self.game_board.get(predator_position[0] +1).value.get(predator_position[1]) == self.alien:
            
            self.alien.decrease_life(25)
            self.game_board.get(predator_position[0]).value.remove(predator_position[1])
            self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
            self.game_board.get(predator_position[0] + 1).value.remove(predator_position[1])
            self.game_board.get(predator_position[0] + 1).value.insert((f'{self.predator} {self.alien}'),predator_position[1])

    def make_predator_move_left(self, predator_position: tuple):

        '''
        Este metodo contiene las validaciones para los movimientos del predator en la direccion hacia izquierda

        Parametros
        ---------
        predator_position: tuple
            Tupla que contiene indice de la fila y la columna que determinan la posicion del predator en el tablero
        
        '''

        if self.game_board.get(predator_position[0]).value.get(predator_position[1] - 1).value == ' ':

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] - 1)
            else:
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] - 1)

        # Evalua si hay un mas en la casilla hacia la que se va a mover y le suma 10 de vida al predator
        elif self.game_board.get(predator_position[0]).value.get(predator_position[1] - 1).value == '+':
            self.predator.increase_life(10)

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] - 1)

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] - 1)

        # Evalua si hay un menos en la casilla a la que se va a mover y le resta 10 vida al predator  
        elif self.game_board.get(predator_position[0]).value.get(predator_position[1] - 1).value == '-':
            self.predator.decrease_life(10)

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':
                
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] - 1)

            else: 

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] - 1)
                
        #Evalua si esta el predator entra en la casilla del alien y le resta 25 de vida
        elif self.game_board.get(predator_position[0]).value.get(predator_position[1] - 1).value == self.alien:
            
            self.alien.decrease_life(25)
            self.game_board.get(predator_position[0]).value.remove(predator_position[1])
            self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
            self.game_board.get(predator_position[0]).value.remove(predator_position[1] - 1)
            self.game_board.get(predator_position[0]).value.insert((f'{self.predator} {self.alien}'),predator_position[1] - 1)

    def make_predator_move_right(self,predator_position:tuple):

        '''
        Este metodo contiene las validaciones para los movimientos del predator en la direccion hacia derecha

        Parametros
        ---------
        predator_position: tuple
            Tupla que contiene indice de la fila y la columna que determinan la posicion del predator en el tablero
        
        '''

        if self.game_board.get(predator_position[0]).value.get(predator_position[1] + 1).value == ' ':

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] + 1)
            else:
                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] + 1)

        # Evalua si hay un mas en la casilla hacia la que se va a mover y le suma 10 de vida al predator
        elif self.game_board.get(predator_position[0]).value.get(predator_position[1] + 1).value == '+':
            self.predator.increase_life(10)

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] + 1)

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] + 1)

        # Evalua si hay un menos en la casilla a la que se va a mover y le resta 10 vida al predator  
        elif self.game_board.get(predator_position[0]).value.get(predator_position[1] + 1).value == '-':
            self.predator.decrease_life(10)

            # Valida si en la casilla actual se encuentra el alien y el predator
            if self.game_board.get(predator_position[0]).value.get(predator_position[1]).value == f'{self.predator} {self.alien}':

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(self.alien,predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] + 1)

            else:

                self.game_board.get(predator_position[0]).value.remove(predator_position[1])
                self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
                self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
                self.game_board.get(predator_position[0]).value.insert(self.predator,predator_position[1] + 1)

        #Evalua si esta el predator entra en la casilla del alien y le resta 25 de vida
        elif self.game_board.get(predator_position[0]).value.get(predator_position[1] + 1).value == self.alien:
            self.alien.decrease_life(25)
            self.game_board.get(predator_position[0]).value.remove(predator_position[1])
            self.game_board.get(predator_position[0]).value.insert(' ',predator_position[1])
            self.game_board.get(predator_position[0]).value.remove(predator_position[1] + 1)
            self.game_board.get(predator_position[0]).value.insert((f'{self.predator} {self.alien}'),predator_position[1] + 1)

    def make_predator_move(self):
        # 1 = Arriba, 2 = Abajo, 3 = Izquierda, 4 = Derecha
        random_direction = randint(1,4)
        print(f'direccion = {random_direction}')
        predator_position = self.get_predator_actual_position()

        if random_direction == 1:
            if predator_position[0] == 0:
                return 'No se puede mover hacia arriba'
            
            else:
                self.make_predator_move_above(predator_position)

        elif random_direction == 2:
            if predator_position[0] == self.game_board_size[1] - 1:
                return 'No se puede mover hacia abajo' 
            else:
                self.make_predator_move_below(predator_position)
                    
        elif random_direction == 3:
            if predator_position[1] == 0:
                return 'No se puede mover hacia la izquierda'
            else:
                self.make_predator_move_left(predator_position)

        elif random_direction == 4:
            if predator_position[1] == self.game_board_size[0] - 1:
                return 'No se puede mover hacia la derecha'
            else:
                self.make_predator_move_right(predator_position)

    def make_alien_move(self, direction : str):
        # w = arriba, s = abajo, a = izquierda, d = derecha
        alien_position = self.get_alien_actual_position()

        if direction.lower() == 'w' :
            if alien_position[0] == 0:
                return 'No se puede mover hacia arriba'
            
            else:
                self.make_alien_move_above(alien_position)

        elif direction.lower() == 's':
            if alien_position[0] == self.game_board_size[1] - 1:
                return 'No se puede mover hacia abajo' 
            else:
                self.make_alien_move_below(alien_position)
                    
        elif direction.lower() == 'a':
            if alien_position[1] == 0:
                return 'No se puede mover hacia la izquierda'
            else:
                self.make_alien_move_left(alien_position)

        elif direction.lower() == "d":
            if alien_position[1] == self.game_board_size[0] - 1:
                return 'No se puede mover hacia la derecha'
            else:
                self.make_alien_move_right(alien_position)

    def make_alien_move_above(self, alien_position: tuple):
        if self.game_board.get(alien_position[0] - 1).value.get(alien_position[1]).value == ' ':
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.insert(self.alien,alien_position[1])
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.insert(self.alien,alien_position[1])
        
        elif self.game_board.get(alien_position[0] - 1).value.get(alien_position[1]).value == '+':
            self.alien.increase_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.insert(self.alien,alien_position[1])
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.insert(self.alien,alien_position[1])

        elif self.game_board.get(alien_position[0] - 1).value.get(alien_position[1]).value == '-':
            self.alien.decrease_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.insert(self.alien,alien_position[1])
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] - 1).value.insert(self.alien,alien_position[1])
            
        elif self.game_board.get(alien_position[0] - 1).value.get(alien_position[1]).value == self.predator:

            self.predator.decrease_life(25)

            self.game_board.get(alien_position[0]).value.remove(alien_position[1])
            self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
            self.game_board_size.get(alien_position[0] - 1).value.remove(alien_position[1])
            self.game_board.get(alien_position[0] - 1).value.insert((f'{self.predator} {self.alien}'),alien_position[1])
    
    def make_alien_move_below(self, alien_position: tuple):
        if self.game_board.get(alien_position[0] + 1).value.get(alien_position[1]).value == ' ':
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.insert(self.alien,alien_position[1])
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.insert(self.alien,alien_position[1])

        elif self.game_board.get(alien_position[0] + 1).value.get(alien_position[1]).value == '+':
            self.alien.increase_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.insert(self.alien,alien_position[1])
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.insert(self.alien,alien_position[1])
        
        elif self.game_board.get(alien_position[0] + 1).value.get(alien_position[1]).value == '-':
            self.alien.decrease_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.insert(self.alien,alien_position[1])
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
                self.game_board.get(alien_position[0] + 1).value.insert(self.alien,alien_position[1])

        elif self.game_board.get(alien_position[0] + 1).value.get(alien_position[1]).value == self.predator:

            self.predator.decrease_life(25)

            self.game_board.get(alien_position[0]).value.remove(alien_position[1])
            self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
            self.game_board.get(alien_position[0] + 1).value.remove(alien_position[1])
            self.game_board.get(alien_position[0] + 1).value.insert((f'{self.predator} {self.alien}'),alien_position[1])

    def make_alien_move_left(self, alien_position: tuple):
        
        if self.game_board.get(alien_position[0]).value.get(alien_position[1] - 1).value == ' ':
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] - 1)
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] - 1)

        elif self.game_board.get(alien_position[0]).value.get(alien_position[1] - 1).value == '+':
            self.alien.increase_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] - 1)
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] - 1)
        
        elif self.game_board.get(alien_position[0]).value.get(alien_position[1] - 1).value == '-':
            self.alien.decrease_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] - 1)
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] - 1)

        elif self.game_board.get(alien_position[0]).value.get(alien_position[1] - 1).value == self.predator:

            self.predator.decrease_life(25)

            self.game_board.get(alien_position[0]).value.remove(alien_position[1])
            self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
            self.game_board.get(alien_position[0]).value.remove(alien_position[1] - 1)
            self.game_board.get(alien_position[0]).value.insert((f'{self.predator} {self.alien}'),alien_position[1] - 1)
        
    def make_alien_move_right(self, alien_position: tuple):
        
        if self.game_board.get(alien_position[0]).value.get(alien_position[1] + 1).value == ' ':
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] + 1)
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] + 1)

        elif self.game_board.get(alien_position[0]).value.get(alien_position[1] + 1).value == '+':
            self.alien.increase_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] + 1)
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] + 1)

        elif self.game_board.get(alien_position[0]).value.get(alien_position[1] + 1).value == '-':
            self.alien.decrease_life(10)
            if self.game_board.get(alien_position[0]).value.get(alien_position[1]).value == f'{self.predator} {self.alien}':
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(self.predator,alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] + 1)
            else:
                self.game_board.get(alien_position[0]).value.remove(alien_position[1])
                self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
                self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
                self.game_board.get(alien_position[0]).value.insert(self.alien,alien_position[1] + 1)

        elif self.game_board.get(alien_position[0]).value.get(alien_position[1] + 1).value == self.predator:

            self.predator.decrease_life(25)

            self.game_board.get(alien_position[0]).value.remove(alien_position[1])
            self.game_board.get(alien_position[0]).value.insert(' ',alien_position[1])
            self.game_board.get(alien_position[0]).value.remove(alien_position[1] + 1)
            self.game_board.get(alien_position[0]).value.insert((f'{self.predator} {self.alien}'),alien_position[1] + 1)
    
    def get_turn(self):
        
        if self.actual_turn == 1:
            self.actual_turn == 2

        else:
            self.actual_turn == 1

    def check_winner(self):
        if self.predator.life <= 0:
            print('El Alien ha ganado')
            return True
        
        elif self.alien.life <= 0:
            print('El Depredador ha ganado')
            return True
        
        return False
  
    def attack_predator(self, alien_position: tuple):

        #Verificar si está adyacente a la derecha
        if self.game_board.get(alien_position[0]).value.get(alien_position[1]).next.value == self.predator:
            self.predator.decrease_life(10)
        
        #Verificar si está adyacente a la izquierda
        elif self.game_board.get(alien_position[0]).value.get(alien_position[1]).prev.value == self.predator:
            self.predator.decrease_life(10)
        
        # Verificar si está adyacente aririba
        elif self.game_board.get(alien_position[0]).prev.value.get(alien_position[1]).value == self.predator:
            self.predator.decrease_life(10)

        # Verificar si está adyacente abajo
        elif self.game_board.get(alien_position[0]).next.value.get(alien_position[1]).value == self.predator:
            self.predator.decrease_life(10)

        else:
            return 'No puedes atacar al depredador. Pierdes el turno'
        
    def show_players_health(self) -> str:
        return (f'Depredador: {self.predator.life} | Alien: {self.alien.life}')