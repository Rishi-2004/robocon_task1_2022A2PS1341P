class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coordinates = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        x, y = 0, 0
        for move in moves:
            x, y = x + coordinates[move][0], y + coordinates[move][1]
        return x == y == 0

