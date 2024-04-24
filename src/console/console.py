import sys

sys.path.append('src')

from AlienVsRobot.alien_vs_predator import AlienVsPredator

class ConsoleUI:

    def __init__(self) -> None:
        self.game = AlienVsPredator()

    def show_game_rules(self):

        print('Bienvenido a Alien Vs Depredador')

    def run_application(self):

        while True:
            print('----------------------')
            print('Bienvenido a Alien Vs Depredador')
            print('A continuación encuentras las opciones de juego, escoje de acuerdo a lo que quieras hacer')
            print('----------------------')
            print('')