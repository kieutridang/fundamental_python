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