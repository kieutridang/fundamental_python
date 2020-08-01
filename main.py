from random import *

def input_number():
    while True:
        n = input('Please input n as an integer: ')
        if n.isnumeric() == False:
            print("Only accept integer")
            continue
        else:
            break
    return int(n)

def create_list_to_n(n):
    myList = []
    for i in range (n):
        myList.append(randint(0, 101))
    return myList

def print_list(myList):
    for item in myList:
        print(item)

def print_prime_list(myList):
    for item in myList:
        if check_prime(item) == False:
            print("{} is not prime number".format(item))
        else:
            print("{} is prime number".format(item))

def check_prime(n):
    if n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True
    

def check_lucky_number(n):
    strN = str(n)
    for char in strN:
        if char != '8' and char != '6':
            return False
    return True

def print_lucky_number(myList):
    for item in myList:
        if check_lucky_number(item) == False:
            print("{} is not lucky number".format(item))
        else:
            print("{} is lucky number".format(item))

number = input_number()
myList = create_list_to_n(number)
print_prime_list(myList)
print("-------------")
print_lucky_number(myList)
