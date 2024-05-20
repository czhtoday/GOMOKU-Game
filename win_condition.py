class Win:
    """Evaluate if there are five stones in a row"""
    # we don't need a init function to use a instance, so use staticmethod here
    @staticmethod
    def check_line(board, column, row):
        for i in range(column):
            for j in range(row):
                if board[i][j] != 0:
                    stone_color = board[i][j]
                    # the first condition to check if there are 4 'space' after this intersection
                    # the second condition is to check if all color are the same
                    # check horizon
                    if i + 4 < column and all(board[i + k][j] == stone_color for k in range(5)):
                        return stone_color
                    # check vertical
                    if j + 4 < row and all(board[i][j + k] == stone_color for k in range(5)):
                        return stone_color
                    # check diagonal I (left top to right bottom)
                    if i + 4 < column and j + 4 < row and all(board[i + k][j + k] == stone_color for k in range(5)):
                        return stone_color
                    # check diagonal II (right top to left bottom)
                    if i - 4 >= 0 and j + 4 < row and all(board[i - k][j + k] == stone_color for k in range(5)):
                        return stone_color
        return None
                

    





