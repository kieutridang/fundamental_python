from string import Template

# Bai 1.a
print('*****')
print('*****')
print('*****')

# Bai 1.b
print('*****')
print('*   *')
print('*****')

# Bai 1.c
print(' ** ')
print('*  *')
print('*  *')
print('*  *')
print(' ** ')

# Bai 1.d
print('*****')
print(' *** ')
print(' *** ')
print(' *** ')
print('*****')

print("XXXXX  XX  XX XXXXXX XX  XX  XXXX  XX  XX")
print("XX  XX  X  X    XX   XX XX  XX  XX XXX XX")
print("XXXXX   X  X    XX   XXXXXX XX  XX XXXXXX")
print("XX       XX     XX   XX  XX XX  XX XXX XX")
print("XX       XX     XX   XX  XX  XXXX  XX  XX")

title = "Que huong"
first = "Que huong la chum khe ngot"
result = Template("$title")
print(result)
print("%s\n...\n{first}\n\tCho con treo hai moi ngay\n\t\tQue huong la duong di hoc\n\t\t\tCon ve rop buom vang bay\n...\n\t\t\t\tDo Trung Quan", title)

# Bai 5
a, b = map(int, input("Nhap 2 so nguyen a, b: ").split(';'))
print("%d + %d = %d"  %(a, b, a + b))

# Bai 6
c = eval(input("Nhap 1 so nguyen c: "))
cc = eval(str(c) * 2)
ccc = eval(str(c) * 3)
print("Ket qua la: %d" %(c + cc + ccc))

# Bai 7
a, b = map(eval, (input("Nhap so nguyen a va b: ").split(' ')))
print("ket qua a luy thua b la: %d" %(a**b))

# Bai 8
width = eval(input("Nhap chieu dai day hinh chu nhat (cm)"))
length = eval(input("Nhap chieu rong day hinh chu nhat (cm)"))
height = eval(input("Nhap chieu cao hinh khoi chu nhat (cm)"))
decimal = eval(input("So luong so le can hien thi"))

print("Dien tich day hinh chu nhat la: %d" %(width * length))

# Bai 10

name, age = input("Nhap ten va tuoi theo thu tu: ").split(',')

yearOfBirth = 2020 - int(age)
yearOf100 = yearOfBirth + 100

print("Nam ma %s tron 100 tuoi la: %d" %(name, yearOf100))

# Bai 11

remain = int(input("Nhap so tien X: "))
money = remain
type500 = 0
type200 = 0
type100 = 0
type50 = 0
type20 = 0
type10 = 0
type5 = 0
type2 = 0
type1 = 0

type500 = remain / 500
remain = remain % 500

type200 = remain / 200
remain = remain % 200

type100 = remain / 100
remain = remain % 100

type50 = remain / 50
remain = remain % 50

type20 = remain / 20
remain = remain % 20

type10 = remain / 10
remain = remain % 10

type5 = remain / 5
remain = remain % 5

type2 = remain / 2
remain = remain % 2

type1 = remain / 1
remain = remain % 1


print("""
    So tien %d duoc doi thanh:
    Loai 500 gom %d to
    Loai 200 gom %d to
    Loai 100 gom %d to
    Loai 50 gom %d to
    Loai 20 gom %d to
    Loai 10 gom %d to
    Loai 5 gom %d to
    Loai 2 gom %d to
    Loai 1 gom %d to
""" %(money, type500, type200, type100, type50, type20, type10, type5, type2, type1))

# Bai 13
intNumber = int(input("Nhap so nguyen: "))

if intNumber % 2 == 0:
    print("Day la so chan")
else:
    print("Day la so le")

print("===================")
print("Mo rong 1:")

if intNumber % 4 == 0:
    print("Day la so chia het cho 4")
elif intNumber % 2 == 0:
    print("Day la so chia het cho 2")
else:
    print("Day la so le")

print("===================")
print("Mo rong 2:")

soBiChia, soChia = map(int, input("Nhap so bi chia va so chia: ").split(','))

if soBiChia % soChia == 0:
    print("{} chia het cho {}".format(soBiChia, soChia))
else:
    print("{} khong chia het cho {}".format(soBiChia, soChia))

# Bai 14
remain = int(input("Nhap so tien X: "))
money = remain
type500 = 0
type200 = 0
type100 = 0
type50 = 0
type20 = 0
type10 = 0
type5 = 0
type2 = 0
type1 = 0

type500 = int(remain / 500)
remain = remain % 500

type200 = int(remain / 200)
remain = remain % 200

type100 = int(remain / 100)
remain = remain % 100

type50 = int(remain / 50)
remain = remain % 50

type20 = int(remain / 20)
remain = remain % 20

type10 = int(remain / 10)
remain = remain % 10

type5 = int(remain / 5)
remain = remain % 5

type2 = int(remain / 2)
remain = remain % 2

type1 = int(remain / 1)
remain = remain % 1

print("So tien {} duoc doi thanh".format(money))
if type500 != 0:
    print("Loai 500 gom {}".format(type500))
if type200 != 0:
    print("Loai 200 gom {}".format(type200))
if type100 != 0:
    print("Loai 100 gom {}".format(type100))
if type50 != 0:
    print("Loai 50 gom {}".format(type50))
if type20 != 0:
    print("Loai 20 gom {}".format(type20))
if type10 != 0:
    print("Loai 10 gom {}".format(type10))
if type5 != 0:
    print("Loai 5 gom {}".format(type5))
if type2 != 0:
    print("Loai 2 gom {}".format(type2))
if type1 != 0:
    print("Loai 1 gom {}".format(type1))

# Bai 15
score = int(input("Nhap diem cua nguoi dung: "))

if score > 100:
    print("Khong nhan gia tri nay.")
elif score >= 90:
    print("Xep loai A")
elif score >= 80:
    print("Xep loai B")
elif score >= 70:
    print("Xep loai C")
elif score >= 65:
    print("Xep loai D")
elif score > 0:
    print("Xep loai E")
else:
    print("Khong nhan gia tri nay.")

# Bai 17
a, b = map(int, input("Nhap so nguyen a va b: ").split(" "))
print("{}.x + {} = 0".format(a, b))

if a == 0 and b != 0:
    print("Phuong trinh vo nghiem")
elif a == 0 and b == 0:
    print("Phuong trinh vo so nghiem")
else:
    print("Nghiem cua phuong trinh la: x = {}".format(-b / a))

# Bai 18
import math

a, b, c = map(float, input("Nhap so nguyen a, b va c: ").split(","))
print("{}.x^2 + {}.x + {} = 0".format(a, b, c))

delta = b**2 - 4*a*c
if (delta < 0):
    print(delta)
    print("Phuong trinh vo nghiem")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("""
    Nghiem cua phuong trinh la:
    x1 = {}
    x2 = {}
    """.format(x1, x2))

# Bai 21
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, StartPoint, EndPoint):
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint

    def length(self):
        HorizontalDistance = self.EndPoint.x - self.StartPoint.x
        VerticalDistance = self.StartPoint.y - self.EndPoint.y
        return math.sqrt(HorizontalDistance**2 + VerticalDistance**2)

class Cycle:
    def __init__(self, CenterPoint, Radius):
        self.CenterPoint = CenterPoint
        self.Radius = Radius

A = Point(3, 2)
B = Point(7, 8)

CycleA = Cycle(A, 5)
CycleB = Cycle(B, 7)

L = Line(A, B)
print("do dai 2 diem A va B: {}".format(L.length()))

TotalRadius = CycleA.Radius + CycleB.Radius
if TotalRadius < L.length():
    print("2 duong tron nam ngoai nhau")
elif TotalRadius > L.length():
    print("2 duong tron cat nhau")
elif TotalRadius == L.length():
    print("2 duong trong giao nhau tai 1 diem")

# Bai 23
a, b = map(int, input("Nhap 2 so nguyen sao cho a < b: ").split(' '))

number = a

while number <= b:
    if number % 3 == 0:
        number += 1
        continue
    print("number = {}".format(number))
    number += 1

# Bai 60
poem = """     Quê hương
Quê hương là   chùm khế   ngọt. 
   Cho con trèo hái   mỗi  ngày   .
Quê  hương là   đường  đi học .
  Con về  rợp bướm  vàng bay .
  Đỗ     Trung Quân    """


def stripPoem(poem):
    poem = poem.strip()
    while poem.find("  ") > 0:
        poem = poem.replace("  ", "")
    while poem.find("\n ") > 0:
        poem = poem.replace("\n ", "\n")
    while poem.find(". ") > 0:
        poem = poem.replace(". ", ".")
    while poem.find(" .") > 0:
        poem = poem.replace(" .", ".")
    print(poem)

stripPoem(poem)

# Bai 61
originString = input("Input a string please: ")

# Cach 1
i = 0
result = True
while (i < len(originString)):
    reversedIndex = -i - 1
    if originString[i] != originString[reversedIndex]:
        print("originString[i]", originString[i])
        print("originString[reversedIndex]", originString[reversedIndex])
        result = False
    i += 1

if result == True:
    print("palindrome")
else:
    print("un-palindrome")

# Cach 2
reversedString = originString[::-1]

if (originString == reversedString):
    print("palindrome cach 2")
else:
    print("un-palindrome cach 2")

# Bai 91

from datetime import *
print("Ngày giờ hiện tại: " , datetime.now())
print("Năm hiện tại: ", date.today().strftime("%Y"))
print("Tháng hiện tại bằng chữ: ", date.today().strftime("%b"))
print("Tuần hiện tại là tuần thứ mấy trong năm:", date.today().strftime("%W"))
print("Ngày hiện tại là ngày thứ mấy trong năm: ", date.today().strftime("%j"))
print("Ngày dương lịch hiện tại là ngày: ", date.today().strftime("%d"))
print("Thứ của ngày hiện tại: ", date.today().strftime("%A"))
print("Ba Thứ của ngày hiện tại: ", date.today().strftime("%a"))
print("Giờ phút giây hiện tại: ", datetime.now().time().strftime("%X"))


# Bai tap bo sung
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

# Bai 71
def create_n_numbers():
    aList = []
    while True:
        number = input("Input a number please: ")
        aList.append(number)
        answer = input("Input more?")
        if answer.upper() == "N":
            break
    return aList

def convert_list_to_set(aList):
    return set(aList)

def sum_set(set):
    result = 0
    for number in set:
        result += int(number)
    return result

aList = create_n_numbers()
aSet = convert_list_to_set(aList)
result = sum_set(aSet)

print(result)

# Bai 72

import string
#Cách 1: tự khai báo set
alphabet = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
#Cách 2: tạo set bằng thuộc tính ascii_lowercase trong module string
#alphabet = set(string.ascii_lowercase)
print(alphabet)
#kết quả =True vì S chưa đầy đủ các ký tự từ a-z
S = 'The quick brown fox jumps over the lazy dog'
#sử dụng toán tử >= vì S có chứa ký tự khoảng trắng (' ')
print(set(S.lower()) >= alphabet)
#kết quả =False vì S thiếu 2 ký tự d và g
S = 'The quick brown fox jumps over the lazy cat'
print(set(S.lower()) >= alphabet)

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


# Bai 3.2 15
import csv
def read_CSV_file(filename):
    with open(filename,'r', encoding='utf8')as f:
        csvReaderObj = csv.reader(f)
        # Lấy dòng đầu tiên chứa các tên field ra
        lst=csvReaderObj.__next__()
        #In tiêu đề cột
        print('| %21s | %20s | %10s | %13s | ' % (lst[0], lst[1], lst[2], lst[3]))
        print('_' * 75)
        for row in csvReaderObj:
            print('| {: >21s}'.format(row[0]),'|', '{: <20s}'.format(row[1]), '| %10s | %13s | ' % (row[2], row[3]))
            # print(f'Dữ liệu gồm {csvReaderObj.line_num-1}dòng')
            
read_CSV_file('./Departments.csv')