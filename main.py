from logo import logo, vs
from game_data import data
import random

print(logo)


def game():
  is_playing = True
  current_score = 0
  optionA = random.choice(data)
  optionB = random.choice(data)
  while current_score < 5 and is_playing:
      
      
      print(f"Compare A: {optionA['name']}, a {optionA['description']}, from {optionA['country']}.")
      print(vs)
      print(f"Against B: {optionB['name']}, a {optionB['description']}, from {optionB['country']}.")

      user_answer = input("How has more followers? Type 'A' or 'B': ").lower()


      if optionA['follower_count'] > optionB['follower_count'] and user_answer == 'a':
        current_score+=1
        optionA = optionA
        optionB = random.choice(data)
        print(f"You're right! Current score: {current_score}.")

      elif optionA['follower_count'] < optionB['follower_count'] and user_answer == 'b':
        current_score+=1
        optionA = optionB
        optionB = random.choice(data)
        print(f"You're right! Current score: {current_score}.")
      else:
        is_playing = False
        print(f"Sorry, that's wrong. Final score: {current_score}")

game()







  