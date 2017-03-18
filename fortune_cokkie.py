# fortune cookie program


print("Fortune cookie program")
print("\n\nThis program will tell you you're fortune!")

#import random

import random

#assign each cookie a random number

cookie = random.randint(1, 5)

if cookie == 1:
    print("\n\nThe study of history is the beginning of political wisdom.")
    
elif cookie == 2:
    print ("\n\nThe wit of a graduate student is like champagne.")
    
elif cookie == 3:
    print("\n\nA book is in your future.")
    
elif cookie == 4:
    print("\n\nA committee of one gets things done. - Joe Ryan.")
    
elif cookie == 5:
    print("\n\nA diamond is a hunk of coal that stuck with it.")
    
else:
    print("\n\nThe cookies are finished")
