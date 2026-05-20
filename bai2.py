# khi nhập 0 thì có cảnh báo nhưng vẫn thực hiện các thao tác bên dưới như tính công có emial nhận thưởng

# lỗi là nhầm lẫn giữa continue khi nhập sai luồng vẫn ko bị ngắt mà thực hiện dẫn đến việc có email nhạna thông báo thưởng 0đ

#  sửa
print("--- hệ thống email thưởng tết ---")
for employee_number in range(1, 4):
    print("--- đang xử lý nhân viên số", employee_number, "---")
    working_days = int(input("nhập số ngày công trong tháng: "))
    
    if working_days == 0:
        print("cảnh báo: nhân viên nghỉ cả tháng không xét duyệt thưởng.")
    else:
        bonus_amount = working_days * 200000
        print(f"→ đã gửi email: Chúc mừng nhận được {bonus_amount:,} vnđ tiền thưởng!")
    print("--------------------------------------------------\n")

print("đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
