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

