import sys
import time

sys.path.append('src')

from AlienVsRobot.alien_vs_predator import AlienVsPredator

class ConsoleUI:

    def __init__(self) -> None:
        self.game = AlienVsPredator()

    def show_game_rules(self):

        print('Bienvenido a Alien Vs Depredador')
        print('--------------------------------')
        print('Las reglas son las siguientes: ')
        print('--------------------------------')
        print('En primer lugar el personaje que usted manejará será el Alien. ')
        print('1. No puedes seleccionar una posición inicial ya ocupada por el Depredador, por un "+" o por un "-" ')
        print('2. Cada personaje iniciará el juego con 50 de vida')
        print('3. El juego se basa en un juego clásico por turnos')
        print('4. Solo puedes realizar una accion por turno: ')
        print('4.1. Moverse hacia arriba, abajo, izquierda o derecha ')
        print('4.2. Atacar al depredador si está adyacente a tu posición')
        print('4.3. Si el Alien ataca exitosamente al Depredador se le restará 10 de vida al Depredador')
        print('5. Si el Alien o el Depredador se desplazan a una posición que contenga un "+" le sumará 10 a la vida, siempre y cuando tenga menos de 50.')
        print('6. Si el Alien se desplaza a la posición en la que esté el Depredador se le restará 25 de vida al Depredador')
        print('7. Si el Depredador se desplaza a la posición en la que esté el Alien se le restará 25 de vida al Alien')
    


    def show_welcome_menu(self):
            print('----------------------')
            print('Bienvenido a Alien Vs Depredador')
            print('A continuación encuentras las opciones de juego, escoje de acuerdo a lo que quieras hacer')
            print('----------------------')
            print('1. Jugar')
            print('2. Mostrar reglas de juego')
            print('3. Salir')

    def run_application(self):

        while True:
            self.show_welcome_menu()
            option = int(input('Por favor selecciona una opción: ')) 
            if option == 1:
                self.run_game()
            elif option == 2:
                self.show_game_rules()
            elif option == 3:
                print('Gracias por jugar Alien Vs Depredador')
                break
            else:
                print('Por favor selecciona una opción válida')

    def initialize_game_board(self):
        print('Iniciando juego...')
        print('----------------------')
        print('Ingrese el tamaño del tablero con que desea jugar')
        print('1. Tablero 4x4')
        print('2. Tablero 6x6')
        print('3. Tablero 8x8')
        print('----------------------')
        board_decision = int(input('Por favor selecciona una opción: '))
        print('----------------------')
        print('Ahora ingrese qué dificultad desea jugar')
        print('1. Fácil')
        print('2. Medio')
        print('3. Difícil')
        print('----------------------')
        difficulty_decision = int(input('Por favor selecciona una opción: '))
        print('----------------------')
        if board_decision == 1:
            board_size = (4, 4)
        elif board_decision == 2:
            board_size = (6, 6)
        elif board_decision == 3:
            board_size = (8, 8)
        
        if difficulty_decision == 1:
            difficulty = 1
        elif difficulty_decision == 2:
            difficulty = 2
        elif difficulty_decision == 3:
            difficulty = 3

        game_board = self.game.create_game_board(difficulty, board_size)
        return game_board
    
    def run_game(self):
        game_board = self.initialize_game_board()
        print('----------------------')
        self.game.show_game_board()
        print('Ingresa la posición donde deseas iniciar el juego')
        row = int(input('Ingresa la fila: '))
        column = int(input('Ingresa la columna: '))
        if self.game.set_alien_position(row,column):
            while True:
                actual_turn = self.game.get_turn()
                print('-------------------------------------')
                print(f'Es el turno del {"Alien" if actual_turn == 1 else "Depredador"}')
                print(self.game.show_players_health())
                print('-------------------------------------')
                self.game.show_game_board()
                print('-------------------------------------')
                if actual_turn == 1:
                    print('Es el turno del Alien, decide qué deseas hacer.')
                    print('1. Moverte en el tablero')
                    print('2. Atacar al Depredador')
                    print('3. Salir del juego')
                    print('-------------------------------------')
                    alien_decision = int(input('Por favor selecciona una opción: '))
                    print('-------------------------------------')
                    if alien_decision == 1:
                        print('Ingresa la dirección en la que deseas moverte')
                        print('W. Arriba')
                        print('S. Abajo')
                        print('A. Izquierda')
                        print('D. Derecha')
                        print('-------------------------------------')
                        alien_move_decision = input('Por favor selecciona una opción: ')
                        print('-------------------------------------')
                        print(self.game.make_alien_move(alien_move_decision))
                    elif alien_decision == 2:
                        alien_position = self.game.get_alien_actual_position()
                        print(self.game.attack_predator_position(alien_position))
                    elif alien_decision == 3:
                        print('Gracias por jugar Alien Vs Depredador 💩 ')
                        self.game.reset_life()
                        break
                    else:
                        print('Opción inválida, pierdes turno.')
                elif actual_turn == 2:
                    print('Es el turno del Depredador, espera...')
                    time.sleep(5)
                    print('-------------------------------------')
                    print(self.game.make_predator_move())
                    print('-------------------------------------')
                    self.game.show_game_board()
                    print('-------------------------------------')
                if self.game.check_winner():
                    break