print("Guess a number between 1 and 10")
import random
number = random.randint(1,10)
while True:
  guess = int(input("Guess your number: "))
  if guess == number:
      print("Congrats! You guessed the number!")
      break
  if guess < number:
      print("Guess higher!")
  if guess > number:
      print("Guess lower!")