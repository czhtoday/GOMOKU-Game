# -*- coding: utf-8 -*-
class AI:
    """Evaluate where to move the white stone"""

    def __init__(self, intersections):
        self.intersections = intersections

    def movement(self):
        bestscore = 0
        bestmove = None
        for x in range(15):
            for y in range(15):
                # if it is a empty intersection
                if self.intersections.board[x][y] == 0:
                    # put a white stone there just for test
                    self.intersections.board[x][y] = 2
                    # receive a score
                    score = self.evaluate_position(x, y)
                    # after we have a score, remove the white stone
                    self.intersections.board[x][y] = 0
                    # find the best score among all empty intersections
                    if score >= bestscore:
                        bestscore = score
                        bestmove = [x, y]
        # place the white stone on the best spot for each round
        if bestmove:
            self.intersections.board[bestmove[0]][bestmove[1]] = 2

    def evaluate_position(self, x, y):
        # firstly see if there are four black stones in a row
        score = self.check_four_black_stones(x, y)
        # if not ,check if there are three black stones in a row
        if score == 0:
            score = self.check_three_black_stones(x, y)
        # if not, just put a white stone black stone
        if score == 0:
            score = self.place_near_black(x, y)
        return score

    def check_four_black_stones(self, x, y):
        patterns = [
            [(1, 0), (2, 0), (3, 0), (4, 0)], # Horizontal
            [(0, 1), (0, 2), (0, 3), (0, 4)], # Vertical
            [(1, 1), (2, 2), (3, 3), (4, 4)], # Diagonal down-right
            [(1, -1), (2, -2), (3, -3), (4, -4)] # Diagonal up-right
        ]

        for pattern in patterns:
            if all(0 <= x + dx < 15 and 0 <= y + dy < 15 and self.intersections.board[x + dx][y + dy] == 1 for dx, dy in pattern):
                start_x, start_y = x + pattern[0][0], y + pattern[0][1]
                end_x, end_y = x + pattern[-1][0], y + pattern[-1][1]

                # Check if the two ends of the four black stones are empty
                if self.is_empty(start_x - pattern[0][0], start_y - pattern[0][1]) and self.is_empty(end_x + pattern[0][0], end_y + pattern[0][1]):
                    return 15  

                # Check if one end of the four black stones is white and the other end is empty
                if self.is_white(start_x - pattern[0][0], start_y - pattern[0][1]) and self.is_empty(end_x + pattern[0][0], end_y + pattern[0][1]):
                    return 12
                elif self.is_empty(start_x - pattern[0][0], start_y - pattern[0][1]) and self.is_white(end_x + pattern[0][0], end_y + pattern[0][1]):
                    return 12

        return 0

    def is_white(self, x, y):
        return 0 <= x < 15 and 0 <= y < 15 and self.intersections.board[x][y] == 2

    def is_empty(self, x, y):
        return 0 <= x < 15 and 0 <= y < 15 and self.intersections.board[x][y] == 0

    def check_three_black_stones(self, x, y):
        patterns = [
            [(1, 0), (2, 0), (3, 0)], # Horizontal
            [(0, 1), (0, 2), (0, 3)], # Vertical
            [(1, 1), (2, 2), (3, 3)], # Diagonal down-right
            [(1, -1), (2, -2), (3, -3)] # Diagonal up-right
        ]

        for pattern in patterns:
            if all(0 <= x + dx < 15 and 0 <= y + dy < 15 and self.intersections.board[x + dx][y + dy] == 1 for dx, dy in pattern):
                return 10

        return 0
    
    def place_near_black(self, x, y):
    # Check if any adjacent position has a black stone
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 15 and 0 <= ny < 15 and self.intersections.board[nx][ny] == 1:
                # Generate a random score using Processing's random function
                return int(random(1, 6))  # Random score between 1 and 5
        return 0

