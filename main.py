from random import randint, choice


# The task is this: the program will ask for the user's name and then it will say
# something like: “Well John, I've thought of a number between 1 and 100 and you
# have only eight tries to guess it. What number do you think it is?” On each try, the
# # player will say a number and the program can answer for different things.
print("Well John I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")

secretNumber = randint(1, 5)

guess = int(input("What your guess John? (NO DECIMALS): "))

attempts = 0

trys = 8



# 1 If the number the user said is less than 1 or greater than 100, it will tell them that  he/she has chosen a number that is out of play.

if guess < 1 or guess > 5:
  print("You have chosen a number that is out of play")
 int(input("Pick another number: "))


# 2 If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.

if guess < secretNumber:
  print("Your answer is wrong, because it is lower than the secret number") 
int(input("Pick another number: "))


# 3 If the user chose a number greater than the secret number, it will let them know that it was greater.

if guess > secretNumber:
  print("Your answer is wrong, because it is greater than the secret number") int(input("Pick another number: "))

# 4 And if the user got the secret number right, they will be informed that they have won,and how many tries that has taken them.

if guess == secretNumber:
  attempts += 1
  print(f"You have won! You used {attempts} attempts!")



# 5 If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done.

