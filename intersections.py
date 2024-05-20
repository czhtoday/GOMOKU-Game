class Intersections:
    def __init__(self, ROW_NUM, COL_NUM, X, Y):
        """
        record the board and stones on it
        """
        self.SPACING = 35
        self.ROW_NUM = ROW_NUM
        self.COL_NUM = COL_NUM
        # X, Y are the coordinates of the top left point
        self.X = X
        self.Y = Y
        self.board = [[0 for _ in range(COL_NUM)] for _ in range(ROW_NUM)]
        self.count = ROW_NUM * COL_NUM

    def display(self):
        for i in range(15):
            for j in range(15):
                current = self.board[i][j]
                # based on the value of each intersection, draw stones
                if current == 0:
                    fill(0)
                    circle((i+1)*35, (j+1)*35, 5)
                if current == 1:
                     fill(0)
                     circle((i+1)*35, (j+1)*35, 20)
                if current == 2:
                     fill(255)
                     circle((i+1)*35, (j+1)*35, 20)

    def add_gridlines(self):
        stroke(0)
        strokeWeight(1)
        for i in range(self.COL_NUM):
            line(self.X + i * self.SPACING, self.Y, self.X + i * self.SPACING, self.Y + self.SPACING * (self.ROW_NUM - 1))
        for j in range(self.ROW_NUM):
            line(self.X, self.Y + j * self.SPACING, self.X + self.SPACING * (self.COL_NUM - 1), self.Y + j * self.SPACING)

    # for the human click, each click give a '1' value as black
    def mark_stonecolor(self, intersection, stone_number):
            self.board[intersection[0]][intersection[1]] = stone_number
            return
    
    # check if the intersection is 0 (if not, its occupied)
    def is_occupied(self, intersection):
        if self.board[intersection[0]][intersection[1]] != 0:
                return True
        return False

    # if any one intersection is still 0, it's not full 
    def is_full(self):
        for row in self.board:
            for intersection in row:
                if intersection == 0:
                    return False
        return True


