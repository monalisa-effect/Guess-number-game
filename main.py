#The computer randomly generates a number. the user enters a number ,
#and the computer will tell you if you are too high or too low. then you keep guessing until you guess the number.



import random

num = random.randint(1, 10)
# print(num)
print('enter number')

while num:
  user = int(input())
  if num > user:
    print('too low ')
    continue
  elif num < user:
    print('too high ')
    continue
  else:
    print('correct')



