import random

from art import logo, vs
from game_data import data
from replit import clear

print(logo)
score = 0
guess2 = random.choice(data)
true=True
while true:

  guess1 = guess2
  guess2 = random.choice(data)
  while guess1 == guess2:
    guess2 = random.choice(data)
  # print(guess1)
  
  def he(guess):
    '''Controls the values '''
    name = guess['name']
    count = guess['follower_count']
    description = guess['description']
    country = guess['country']
    return f'{name}, a {description}, from {country}'
  
  def answer(guess, a_follower,b_follower):
    if a_follower > b_follower:
      return guess == 'a'
    else:
      return guess == 'b'
  
  print(logo)
  print(f'Compare A: {he(guess1)}')
  print(vs)
  # print(guess2)
  print(f'Against B: {he(guess2)}')
  guess = input('Who has the more followers? "A" or "B": ').lower()
  if guess != 'A' and 'B':
    print("Wrong option!")
  
  followers_1 = guess1['follower_count']
  # print(followers)
  followers_2 = guess2['follower_count']
  
  correct = answer(guess,followers_1,followers_2)
  # print(correct)
  clear()
  
  
  if correct:
    score+=1
    print(f'You\'re right! Current score: {score}.\n')
    # clear()
  else:
    true=False
    print(f'It\'s a wrong guess. Final score is: {score}.')
    # clear()
  
    

# for _ in range(1):
#   he = random.choice(data)
#   for i in he:
#     for j in i.values():
#       print(j)
#   print()
    # for j in i:
    #   print(j)


# print(j)
# print(f'Comapre A: {he}')