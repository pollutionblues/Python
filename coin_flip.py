# coin flip program

import random

#intialise counters
count = 0
heads_count = 0
tails_count = 0
heads = 1
tails = 2

#Welcome the user to the program

print("\tWelcome to the Coin Flip program")


while count < 100:
    flip = random.randint(1,2)
    if flip == heads:
        heads_count += 1
        count += 1
    elif flip == tails:
        tails_count += 1
        count += 1
    else:
        continue

print("\n\nAfter 100 flips there was", heads_count,"heads"\
      " and", tails_count,"tails!")
