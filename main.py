from random import randint, choice, random

print("Well John I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?")

attempts = 1

trys = 8

secretNumber = randint(1,100)
guess = int(input("What your guess John? (NO DECIMALS): "))

while secretNumber != guess:
    if guess < 1 or guess > 100:
      print("Your guess is out of bounds")
      guess = int(input("Guess another number: "))
      attempts += 1
    elif guess < secretNumber:
      print("Your guess is less than the secret number")
      guess = int(input("Guess another number: "))
      attempts += 1
    elif guess > secretNumber:
      print("Your guess is greater than the secret number")
      guess = int(input("Guess another number: "))
      attempts += 1
    if attempts == 8:
      print("Well John your number of attempts are gone, game over pal") 
      break
    if guess == secretNumber:
      print(f'Well done John you guessed it with only {attempts} attempts')
      break