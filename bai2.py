# khi nhập 0 thì có cảnh báo nhưng vẫn thực hiện các thao tác bên dưới như tính công có emial nhận thưởng

# lỗi là nhầm lẫn giữa continue khi nhập sai luồng vẫn ko bị ngắt mà thực hiện dẫn đến việc có email nhạna thông báo thưởng 0đ

#  sửa
print('----- Hệ thống email thưởng tết ')

for employee_number in range (1,4):
    print('Đang xử lí nhân viên số', employee_number)

    working_days = int(input('Nhập số ngày công: '))

    if working_days == 0: 
        print('Nhân viên nghỉ cả tháng, không được xét duyệt')
        continue
    
    bonus_amount =working_days * 200000
    print(f'-> Đã gửi email: Chúc mừng nhận được {bonus_amount} VNĐ tiền thưởng')
    print('-------------------------------------------------------------')

print('Đã thành công in mức lương cho 3 nhân viên')
