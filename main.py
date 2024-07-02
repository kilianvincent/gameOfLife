from src.py.grid import *


def main():
    G = Grid(5)
    G.set(2, 3, 1)
    G.set(2, 2, 1)
    G.set(2, 1, 1)

    G.run()


if __name__ == '__main__':
    main()
