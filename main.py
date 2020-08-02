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
