#to create a game
#choose between rock paper and scissors
#import random if random =rock and user=scissors computer wins
#if random=scissors and user =rock user wins
#if random = scissors and user=paper then computer wins
#if random=paper and user=scissors then user wins
#if random=rock and user=paper then user wins
#if random = paper and user=rock then computer wins

import random
ran = random.choice(['rock', 'paper', 'scissors'])
user_score = 0
comp_score = 0
count = 0
while count <= 5:
    user_choice = input('choose rock, paper or scissors: ')
    if ran == user_choice:
        print('both your choices are same and cannot be counted and null')
    if ran == 'scissors' and user_choice == 'rock':
        user_score += 1
        print('computer choice= ', ran, 'user choice= ', user_choice)
        print('user gets point')
    if ran == 'paper' and user_choice == 'scissors':
        user_score += 1
        print('computer choice= ', ran, 'user choice= ', user_choice)
        print('user gets point')
    if ran == 'rock' and user_choice == 'paper':
        user_score += 1
        print('computer choice= ', ran, 'user choice= ', user_choice)
        print('user gets point')
    if ran == 'rock' and user_choice == 'scissors':
        comp_score += 1
        print('computer choice= ', ran, 'user choice= ', user_choice)
        print('computer gets point')
    if ran == 'scissors' and user_choice == 'paper':
        comp_score += 1
        print('computer choice= ', ran, 'user choice= ', user_choice)
        print('computer gets point')
    if ran == 'paper' and user_choice == 'rock':
        comp_score += 1
        print('computer choice= ', ran, 'user choice= ', user_choice)
        print('computer gets point')
    count += 1



if user_score > comp_score:
    print('user wins',comp_score ,'-',user_score)
elif comp_score > user_score:
    print('computer wins',comp_score,'-',user_score)
else:
    print('its a tie ',comp_score,'-',user_score)













