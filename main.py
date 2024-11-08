import os
import random
from logo import *
from game_data import *

def get_a_guess():
  """Ask the user to choose a option and validate that the input is in 
  a correct format"""
  guess = None
  while not guess:
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess != 'A' and guess != 'B':
      guess = None
      print("Wrong input. Try again.")
  return guess

def get_a_and_b(a=-1, b=-1): #value by default in case that a or b are empty
  """Generate values random and assign them to variables a and b. Also check that a and b doesn't contain same data and return the values"""
  if a < 0:
    a= random.randint(0, len(data) - 1)
  b = random.randint(0, len(data) - 1)

  while a == b:
    b = random.randint(0, len(data) - 1)
  
  return a, b

def main():
  """Main function to run the game, set score variables and a flag to track the state of the game. Also trigger get_a_and_b function to display options and control the flow of the application depending on the user answer."""
  score = 0
  game_over = False
  a = b = -1

  while not game_over:
    print(logo)
    print()

    a, b = get_a_and_b(a, b)
    if score > 0:
      print(f"You're right! Current score: {score}.")

    print(f"Compare A: {data[a]['name']}, {data[a]['description']} from {data[a]['country']}")
    print()
    print(vs)
    print()
    print(f"Against B: {data[b]['name']}, {data[b]['description']} from {data[b]['country']}")

    guess = get_a_guess()

    if(guess == 'A' and data[a]['follower_count'] > data[b]['follower_count']) or (guess == 'B' and data[a]['follower_count'] < data[b]['follower_count']):
      score += 1
      os.system('cls')
      if guess == 'B':
        a = b
    else:
      game_over = True
  
  os.system('cls')
  print(logo)
  print()
  print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == "__main__":
  main()
