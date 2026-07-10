import random

#printing title
print("\n========== SNAKE AND LADDER ==========\n")

#taking players input
playerA = input("Enter name of Player A: ")
playerB = input("Enter name of Player B: ")

#setting start position of players and turn
posA = 0
posB = 0
turn = 0

print("\nGet '1' or '6' on the dice to start the game.")
print("\nLadders at: 5, 29, 46, 58, 64, 79, 84")
print("Snakes at: 30, 44, 55, 67, 88, 94, 99\n")

#function to check positions of snakes and ladders
def check_position(pos):
    snakes = [30, 44, 55, 67, 88, 94, 99]
    ladders = [5, 29, 46, 58, 64, 79, 84]

    if pos in snakes:
        pos -= 5
        print("Snake! Slide down to", pos)

    elif pos in ladders:
        pos += 5
        print("Ladder! Climb up to", pos)

    return pos


#function to draw the board
def draw_board(posA, posB):
    for row in range(9, -1, -1):
        for col in range(10):

            if row % 2 == 0:
                cell = row * 10 + (col + 1)
            else:
                cell = row * 10 + (10 - col)

            print("|", end="")

            if cell == posA and cell == posB:
                print("A&B", end="")
            elif cell == posA:
                print(" A  ", end="")
            elif cell == posB:
                print(" B  ", end="")
            elif cell < 10:
                print(f" 0{cell} ", end="")
            else:
                print(f" {cell} ", end="")

        print("|")


# Main game loop
while posA < 100 and posB < 100:

    if turn % 2 == 0:

        currentPlayer = playerA
        input(f"{currentPlayer}, press ENTER to roll the dice...")

        dice = random.randint(1, 6)
        print(f"{currentPlayer} rolled a {dice}")

        # check condition for playerA
        if posA == 0 and dice not in [1, 6]:
            print(f"{playerA}, you need 1 or 6 to start the game. Try again next turn!\n")

        else:
            posA += dice

            if posA > 100:
                posA = 100

            posA = check_position(posA)
            print(f"{playerA}'s new position: {posA}\n")

    else:

        currentPlayer = playerB
        input(f"{currentPlayer}, press ENTER to roll the dice...")

        dice = random.randint(1, 6)
        print(f"{currentPlayer} rolled a {dice}")

        # check condition for playerB
        if posB == 0 and dice not in [1, 6]:
            print(f"{playerB}, you need 1 or 6 to start the game. Try again next turn!\n")

        else:
            posB += dice

            if posB > 100:
                posB = 100

            posB = check_position(posB)
            print(f"{playerB}'s new position: {posB}\n")

    # Draw game board
    print("\nCurrent Board:")
    draw_board(posA, posB)

    print("\nPositions:")
    print(f"{playerA}: {posA}")
    print(f"{playerB}: {posB}")
    print("----------------------------------------\n")

    if posA >= 100:
        print(f"{playerA} wins the game!")
        print("\n========== GAME OVER ==========")
        break

    if posB >= 100:
        print(f"{playerB} wins the game!")
        print("\n========== GAME OVER ==========")
        break

    turn += 1