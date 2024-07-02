class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for x in range(self.size)] for y in range(self.size)]
        self.nextGrid = [[0 for x in range(self.size)] for y in range(self.size)]

    def subgrid(self, i, j):
        return [[self.grid[(i-1) % self.size][(j+1) % self.size], self.grid[i % self.size][(j+1) % self.size], self.grid[(i+1) % self.size][(j+1) % self.size]],
                [self.grid[(i-1) % self.size][j % self.size], 0, self.grid[(i+1) % self.size][j % self.size]],
                [self.grid[(i-1) % self.size][(j-1) % self.size], self.grid[i % self.size][(j-1) % self.size], self.grid[(i+1) % self.size][(j-1) % self.size]]]

    def next(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == 0:
                    if sum(sum(self.subgrid(i, j), [])) == 3:
                        self.nextGrid[i][j] = 1
                else:
                    if not 2 <= sum(sum(self.subgrid(i, j), [])) <= 3:
                        self.nextGrid[i][j] = 0
                    else:
                        self.nextGrid[i][j] = 1
        self.grid = self.nextGrid
        self.nextGrid = [[0 for x in range(self.size)] for y in range(self.size)]
