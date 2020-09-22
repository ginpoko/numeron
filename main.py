import sub
import time
import random

A_check = []
B_check = []
print('-' * 20)
print('START NUMERON')
print('-' * 20)
print('\n')
time.sleep(1)
A = input("Input the first player's name :")

print('-' * 40)
B = input("Input the first player's name :")

sub.select(A,A_check)
sub.select(B,B_check)
# print(A_check)
# print(B_check)
while True:
    battle1 = sub.battle(A,B_check)
    if battle1==1:
        break
    battle2 = sub.battle(B,A_check)
    if battle2==1:
        break

print('GAME OVER')
