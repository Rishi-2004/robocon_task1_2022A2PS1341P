
class Robot:
    def is_at_origin(self, sequence: str) -> bool:
        pos_x, pos_y = 0, 0
        for move in sequence:
            if move == "U":
                pos_y += 1
            elif move == "D":
                pos_y -= 1
            elif move == "L":
                pos_x -= 1
            elif move == "R":
                pos_x += 1
        return pos_x == 0 and pos_y == 0
