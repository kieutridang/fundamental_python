# Cho nhập 1 chuỗi (S). Sửdụng dictionary để đếm số lần xuất hiện của từng ký tựtrong (S)
def char_frequency(Str):
    dict = {}
    for C in Str:
        keys = dict.keys()
        if C in keys: #có trong dict => tăng value
            dict[C] += 1
        else: #thêm key mới là C với value=1
            dict[C] = 1
    return dict
    
Str='good morning'           
mydict=char_frequency(Str)
print('Các ký tự xuất hiện trong chuỗi:')
for k,v in mydict.items():
    print(k,'=',v,'lần')
