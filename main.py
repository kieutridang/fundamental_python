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