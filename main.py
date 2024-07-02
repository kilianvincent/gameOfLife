from src.py.grid import *
import tkinter as tk


def main():
    window = tk.Tk()

    G = Grid(50)
    G.set(2, 3, 1)
    G.set(2, 2, 1)
    G.set(2, 1, 1)
    G.set(0, 4, 1)

    G.run(window)


if __name__ == '__main__':
    main()
