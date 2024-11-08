from logo import logo, vs
from game_data import data
import random

# print(logo)

current_score = 0
while current_score < 10:
  for opt in data:
    print(random.choice(data))


user_answer = input("How has more followers? Type 'A' or 'B': ").lower()