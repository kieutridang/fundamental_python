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
    return content

#(iv)
def sum(filename):
    sum = 0
    content = read_file(filename).strip()
    numbers = content.split(' ')
    for number in numbers:
        sum += int(number)
    return sum

#(v)
def list_out_prime_numbers(filename):
    prime_numbers = []
    content = read_file(filename)
    numbers_as_string = content.strip().split(' ')
    for number_as_string in numbers_as_string:
        is_prime_number = int(number_as_string) > 0 and check_prime(int(number_as_string))
        if is_prime_number:
            prime_numbers.append(int(number_as_string))
    return prime_numbers

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

n = input_n()
write_file("./Number.txt", n)
read_file("./Number.txt")

print("sum: {}".format(sum("./Number.txt")))

print("prime numbers: {}".format(list_out_prime_numbers("./Number.txt")))