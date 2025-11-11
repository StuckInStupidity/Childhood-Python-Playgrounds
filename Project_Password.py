import random
lower_case = "azertyuiopqsdfghjklmwxcvbn"
upper_case = "AZERTYUIOPQSDFGHJKLMWXCVBN"
number = "0123456789"
symbol = "@#!?&%$"
use_for = lower_case + upper_case + number + symbol
length_for_pwd = 12
password = "".join(random.sample(use_for, length_for_pwd))
print("Generated password : ",password)
print("\n")