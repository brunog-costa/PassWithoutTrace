'''
Put your super important code implementation here
'''

import random 
from icecream import ic

def roll_dice(num_dices:int, type_dice:int):
   '''
      Roll a given number of a certain type of dice and tells you the results
   '''
   for roll in range(int(input("How many dice are you rolling?: "))):
      total = random.randint(1,20)


ic()