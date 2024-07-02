import time
import tkinter as tk


class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.nextGrid = [[0 for x in range(self.size)] for y in range(self.size)]

    def set(self, i, j, value):
        if value == 1 or value == 0:
            self.grid[j % self.size][i % self.size] = value

    def subgrid(self, i, j):
        return [[self.grid[(i-1) % self.size][(j+1) % self.size], self.grid[i % self.size][(j+1) % self.size], self.grid[(i+1) % self.size][(j+1) % self.size]],
                [self.grid[(i-1) % self.size][j % self.size], 0, self.grid[(i+1) % self.size][j % self.size]],
                [self.grid[(i-1) % self.size][(j-1) % self.size], self.grid[i % self.size][(j-1) % self.size], self.grid[(i+1) % self.size][(j-1) % self.size]]]

    def next(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    if sum(sum(self.subgrid(i, j), [])) == 3:
                        self.nextGrid[j][i] = 1
                else:
                    if not 2 <= sum(sum(self.subgrid(i, j), [])) <= 3:
                        self.nextGrid[j][i] = 0
                    else:
                        self.nextGrid[j][i] = 1
        self.grid = self.nextGrid
        self.nextGrid = [[0 for x in range(self.size)] for y in range(self.size)]

    def debug(self):
        for row in self.grid:
            for cell in row:
                print(str(cell) + ' ', end='')
            print()
        print()

    def display(self, canvas):
        recSize = 500 / self.size

        canvas.delete('all')
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                color = 'black' if cell == 1 else 'white'
                canvas.create_rectangle(i * recSize, j * recSize, (i+1) * recSize, (j+1) * recSize, fill=color)
        canvas.pack()

    def run(self, window):
        canvas = tk.Canvas(window, width=500, height=500)
        while True:
            self.display(canvas)
            self.debug()
            window.update()
            self.next()
            time.sleep(1)
