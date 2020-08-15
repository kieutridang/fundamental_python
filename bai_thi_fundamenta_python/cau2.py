import csv
def print_CSV_file(filename):
    with open(filename,'r', encoding='utf8')as f:
        csvReaderObj = csv.reader(f)
        # Lấy dòng đầu tiên chứa các tên field ra
        lst=csvReaderObj.__next__()
        #In tiêu đề cột
        print('| %21s  | %20s | %15s | %13s |  %10s |' % (lst[0], lst[1], lst[2], lst[3], lst[4]))
        print('_' * 100)
        for row in csvReaderObj:
            print('| {: >21s}'.format(row[0]),'|', '{: <20s}'.format(row[1]), '| %15s | %13s | ' % (row[2], row[3]), '{: >14s}'.format(row[4]), '|')
            # print(f'Dữ liệu gồm {csvReaderObj.line_num-1}dòng')

def read_CSV_file(filename):
    danh_sach_ty_le_nam_nu_nho_hon_100 = []
    with open(filename,'r', encoding='utf8')as f:
        rows = csv.reader(f)
        # Lấy dòng đầu tiên chứa các tên field ra
        rows.__next__()
        for row in rows:
            ty_le_nam_nu = float(row[4])
            if (ty_le_nam_nu < 100):
                danh_sach_ty_le_nam_nu_nho_hon_100.append(row)
    return danh_sach_ty_le_nam_nu_nho_hon_100

def write_CSV_file(filename, my_list):
    with open(filename, mode = 'w+', encoding = 'utf-8') as file:
        for row in my_list:
            separator = ', '
            new_row = separator.join(row) + '\n'
            file.write(new_row)
    file.close()
            
# print_CSV_file('./VietNam_PopulationByAgeSex.csv')

danh_sach_ty_le_nam_nu_nho_hon_100 = read_CSV_file('./VietNam_PopulationByAgeSex.csv')

write_CSV_file('./Vietnam_population_male_female_rate_under_100.csv', danh_sach_ty_le_nam_nu_nho_hon_100)
