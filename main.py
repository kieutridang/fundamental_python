# Bai 3.1.3 > 9

#(i)
from random import randint

def input_n():
    try:
        enter_number = int(input("Please input a number between 2 and 200: "))
        if 2 <= enter_number <= 200:
            return enter_number
    except:
        print("Only integer between 2 and 200 allowed")

#(ii)
def write_file(filename, n):
    try:
        i = 0
        numbers = ''
        while i < n:
            number = randint(-9, 200)
            numbers += ' ' + str(number)
            i += 1
        with open(filename, mode = 'w+', encoding = 'utf-8') as file:
            file.write(numbers)
    except:
        print("Something went wrong when writing to the file")
    finally:
        file.close()

#(iii)
def read_file(filename):
    with open(filename, mode = 'r', encoding = 'utf-8') as file:
        content = file.read()
    print("content: {}".format(content))

n = input_n()
write_file("./Number.txt", n)
read_file("./Number.txt")
