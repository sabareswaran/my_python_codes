import random
import math


#generating random nummber
num =int (random.randint(1,10))
print("Game started....")
print("You have four chances to guess the number...")

#generating clues for number

clue1 = num * num 
clue2 = math.sqrt(num)
clue3 = num * 2
clue = [clue1,clue2,clue3]
score = 100
print(num)
#loop for clues and answer check
for x in range(1,5):
    guess = int(input("Guess the number:-"))
    if (guess == num):
        print("correct")
        break
    elif (x == 4):
        print("GAME OVER!!!")
        score = 0
        break
    else:
        print(clue[x -1])
    score = score - 20
print("points:-",score)