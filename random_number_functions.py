# generate a random num between 1 & 9
# note that I have to IMPORT 'random' first and foremost
import random
# note the function 'randint()' < basically 'random integer'
# use the dot notation to indicate where to assign the 'randint()' function
passkey = random.randint(1, 9)
print (passkey)

# another method of producing a random number is to use the random range function
# again, IMPORT 'random' first
import random
# random range function is 'randrange()'
# # use the dot notation to indicate where to assign the 'randrange()' function
password = random.randrange(9)
print (password)
