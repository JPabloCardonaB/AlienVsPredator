import sys

sys.path.append('src')

from console.console import ConsoleUI


if __name__ == '__main__':
    console = ConsoleUI()
    console.run_application()