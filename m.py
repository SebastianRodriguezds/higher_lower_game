from game_data import data
from logo import logo, vs
import random

def format_date(account):
  """Format the account data into printable format."""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
  """Take a user's guess and the follower counts and return if they got it right"""
  if a_followers > b_followers:
      return user_guess == "a" 
  else:
      return user_guess == "b"


#Display logo
print(logo)
score = 0
game_should_continue = True
correct_answer = ""

#Make the game repeatable.
while game_should_continue:

  #Generate a random account from the game data.
  if correct_answer == "":
    account_a = random.choice(data) 
    account_b = random.choice(data) 
  else:
    account_a = correct_answer
    account_b = random.choice(data) 

  if account_a == account_b:
    account_b = random.choice(data)
    
  print(f"Compare A: {format_date(account_a)}.")
  print(vs)
  print(f"Against B: {format_date(account_b)}.")

  #Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  if guess == 'a':
    correct_answer  = account_a
  elif guess == 'b':
    correct_answer = account_b

  #Clear the screen
  print("\n" * 50)
  print(logo)

  #Check if the user is correct.
  #Get follower count of each account 
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  #Use if statemnt to check if user is correct.
  #Give user feedback on their guess.
  #score keeping.
  if is_correct:
    score+= 1
    print(f"You're right! Current score {score}.")
  else:
    print(f"Sorry, that's wrong.Final score: {score}.")
    game_should_continue = False

#Making account at position B became the next account at position A.
