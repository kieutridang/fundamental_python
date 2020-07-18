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