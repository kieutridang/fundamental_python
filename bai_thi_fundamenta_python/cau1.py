#Kieu Tri Dang

from random import randint

def cau1a():
    while True:
        a = input("Nhap so nguyen duong trong khoang 10 den 99:")
        try:
            n = int(a)
        except Exception:
            print("Du lieu vua nhap khong phai la so nguyen, nhap lai:")
        else:
            if n < 10 or n > 99:
                print("Chi trong khoang tu 10 den 99, nhap lai:")
            else:
                return n

def cau1b(n):
    a_list = []
    for index in range(n):
        random_number = randint(1, 5000)
        a_list.append(random_number)
    return a_list

def cau1c(k):
    # xet so palindrome
    return k == k[::-1]

def cau1d(input_list):
    palindromeList = []
    for number in input_list:
        if cau1c(str(number)):
            palindromeList.append(number)
    if len(palindromeList) > 0:
        print("Cac so palindrome co trong list: {}".format(palindromeList))
    else:
        print("Cac so palindrome co trong list: trong list khong co chua so palindrome")
    return palindromeList

n = cau1a()
a_list = cau1b(n)
cau1d(a_list)