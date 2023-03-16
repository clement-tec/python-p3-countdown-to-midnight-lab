# your code goes here!
from time import sleep

def countdown(n):
    while n :
        print(f'{n} SECOND(S)!')
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):

    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
        sleep(1)

    print('HAPPY NEW YEAR!')