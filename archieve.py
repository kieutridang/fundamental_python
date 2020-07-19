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
