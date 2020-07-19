# Bai 23
a, b = map(int, input("Nhap 2 so nguyen sao cho a < b: ").split(' '))

number = a

while number <= b:
    if number % 3 == 0:
        number += 1
        continue
    print("number = {}".format(number))
    number += 1