from intersections import Intersections
from win_condition import Win
from computer_ai import AI


# Canvas size
WIDTH = 560
HEIGHT = 560
ROW_NUM = 15
COL_NUM = 15
#  origin coordinates(left up corner), as the first intersection
X = 35
Y = 35
# as the gap between two intersection
FACTOR = 35 
# stone will only be placed within this range
MAX_DISTANCE = 17.5
intersections = Intersections(ROW_NUM, COL_NUM, X, Y)
computerAI = AI(intersections)
# set a condition to end the game when we have a winner
winner = None
# player goes first as black rock, then AI
currentPlayer = "black"
# AI will wait 3 seconds then move. (1s with 60 frames)
AIDelay = 3 * 60

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB)

def draw():
    global currentPlayer, winner, AIDelay
    background(153, 126, 76)
    # draw all the grid line connecting intersections
    intersections.add_gridlines()
    # draw all the intersection points and stones
    intersections.display()

    # When the AI could make a move
    if currentPlayer == "white":
        # create a delay, so the AI will wait for 5s then move
        if AIDelay <= 0:
            computerAI.movement()
            # see after the movement, if the AI have won the game
            winner = Win.check_line(intersections.board, COL_NUM, ROW_NUM)
            AIDelay = 3 * 60
            # switch the move turn to human player
            currentPlayer = "black"
        else:
            AIDelay -= 1
    
    # If the board is full, end the game as draw
    if intersections.is_full():
        textAlign(CENTER, CENTER)
        textSize(30)
        fill(255, 0, 0)
        text("DRAW", width / 2, height / 2)
        return
    
    # If black stone (human) win, save the result to a new file
    if winner == 1:
        textAlign(CENTER, CENTER)
        textSize(30)
        fill(0, 0, 255)
        text("Human Win", width / 2, height / 2)
        # ask for player's name
        answer = input('Enter your name')
        if answer:
            print('hi ' + answer)
        elif answer == '':
            print('[empty string]')
        else:
            print(answer) # Canceled dialog will print None
        update_score(answer)
        return
    
    # If white stone (AI) win, print the result
    if winner == 2:
        textAlign(CENTER, CENTER)
        textSize(30)
        fill(255, 0, 0)
        text("AI Win", width / 2, height / 2)
        return

def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def mousePressed():
    """This is the human movement"""
    global winner, currentPlayer
    # if the game is over, do not proceed
    if winner is not None:
        return
    # when it's player's turn
    if currentPlayer == "black":
        # on click, if the click point is near an empty intersection, place a stone
        nearestIntersection = getNearestIntersection(mouseX, mouseY, intersections)
        if not intersections.is_occupied(nearestIntersection):
            # change the value of that point from 0 to 1
            intersections.mark_stonecolor(nearestIntersection, 1)
            # check if win after each move
            winner = Win.check_line(intersections.board, COL_NUM, ROW_NUM)
            # if not win, the turn is AI's
            currentPlayer = "white"

        
def getNearestIntersection(x, y, intersections):
    # caculate which intersection is nearest to the click point 
    nearestIntersection = None
    minDistance = float('inf')
    for i in range(ROW_NUM):
        for j in range(COL_NUM):
            if not intersections.is_occupied([i, j]):
                distance = dist(x, y, (i+1)*FACTOR, (j+1)*FACTOR)
                if distance < minDistance and distance <= MAX_DISTANCE:
                    minDistance = distance
                    nearestIntersection = [i, j]
    return nearestIntersection


def update_score(winner_name):
    # initialize the scores dictionary
    scores = {}
    # read existing file (if there is one)
    try:
        with open('scores.txt', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2 and parts[1].isdigit():
                    name, score = parts[0], int(parts[1])
                    scores[name] = score
    except IOError:
        # if no file, skip for now
        pass

    # update the winner's score
    if winner_name in scores:
        scores[winner_name] += 1
    else:
        scores[winner_name] = 1

    # arrange the order of name based on score
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    with open('scores.txt', 'w') as file:
        for name, score in sorted_scores:
            file.write("{} {}\n".format(name, score))



