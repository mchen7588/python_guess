import random

print('-------------------------')
print('----------guess----------')
print('-------------------------')

num = random.randint(0, 100)
name = input('name? ')
guess = -1

while guess != num:
    guess = int(input('guess: '))
    if guess < num:
        print('sorry {1}, {0} is too low'.format(guess, name))
    elif guess > num:
        print('sorry {1}, {0} is too high'.format(guess, name))
    else:
        print('{} is correct!'.format(guess))
        exit()
