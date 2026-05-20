# khi nhập 0 thì có cảnh báo nhưng vẫn thực hiện các thao tác bên dưới như tính công có emial nhận thưởng

# lỗi là nhầm lẫn giữa continue khi nhập sai luồng vẫn ko bị ngắt mà thực hiện dẫn đến việc có email nhạna thông báo thưởng 0đ

#  sửa
for i in range(3):
    ten = input(f"\nNhập tên nhân viên thứ {i + 1}: ")
    
    try:
        so_ngay_cong = int(input("Nhập số ngày công: "))
    except ValueError:
        print("Số ngày công không hợp lệ!")
        continue

    if so_ngay_cong <= 0:
        print(f"Cảnh báo: Nhân viên {ten} nghỉ không lương cả tháng (0 ngày công)!")
        continue

    tien_thuong = so_ngay_cong * 200000
    print(f"Tính thưởng thành công cho {ten}: {tien_thuong:,.0f} VNĐ")
    print(f"Hệ thống: Đã gửi email chúc mừng nhận thưởng đến {ten}.")