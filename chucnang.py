#def nhap_danh_sach_va_luu_file():
#    print(" Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
#def doc_va_xuat_danh_sach():
#    print("Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.")
#def tim_nhan_vien_theo_ma():
#    print("Y3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.")
#def xoa_nhan_vien_theo_ma():
#    print("Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
#def cap_nhat_thong_tin_nhan_vien():
#    print("Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.") 
#def tim_nhan_vien_theo_khoang_luong():
#    print("Y6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.")
#def sap_xep_theo_ho_ten():
#    print("Y7. Sắp xếp nhân viên theo họ và tên.")
#def sap_xep_theo_thu_nhap():
#    print("Y8. Sắp xếp nhân viên theo thu nhập.")
#def xuat_5_nhan_vien_thu_nhap_cao_nhat():
#    print("Y9. Xuất 5 nhân viên có thu nhập cao nhất.")


class nhanvien:
    def __init__(self, ma, ho_ten, luong):
        self.ma = ma
        self.ho_ten = ho_ten
        self.luong = float(luong)

    def tinh_thu_nhap(self):
        return self.luong
    
    def tinh_thue(self):
        thu_nhap = self.tinh_thu_nhap()
        if thu_nhap < 9000000:
            return 0
        elif thu_nhap <= 15000000:
            return (thu_nhap - 9000000) * 0.1
        else:
            return (thu_nhap - 15000000) * 0.12 + (15000000 - 9000000) * 0.1
        

    def __str__(self):
        return f"{self.ma:10} | {self.ho_ten:25} | {self.luong:10,.0f} | {self.tinh_thu_nhap():12,.0f} | {self.tinh_thue():10,.0f}"

class nhanvientiepthi(nhanvien):
    def __init__(self, ma, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma, ho_ten, luong)
        self.doanh_so = float(doanh_so)
        self.hoa_hong = float(hoa_hong)

    def tinh_thu_nhap(self):
        return self.luong + self.doanh_so * self.hoa_hong
    

class truongphong(nhanvien):
    def __init__(self, ma, ho_ten, luong, luong_trach_nhiem):
        super().__init__(ma, ho_ten,luong)
        self.luong_trach_nhiem = float(luong_trach_nhiem)

    def tinh_thu_nhap(self):
        return self.luong + self.luong_trach_nhiem
    

def nhap_danh_sach():
    ds = []
    n = int(input("nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"\n--- Nhân viên {i+1} ---")
        loai = input("Loại (1-Hành chính, 2-Tiếp thị, 3-Trưởng phòng): ")
        ma = input("Mã nhân viên: ")
        ho_ten = input("Họ tên: ")
        luong = float(input("Lương cơ bản: "))

        if loai == "1":
            nv = nhanvien(ma, ho_ten, luong)
        elif loai == "2":
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Tỉ lệ hoa hồng: "))
            nv = nhanvientiepthi(ma, ho_ten, luong, doanh_so, hoa_hong)
        elif loai == "3":
            luong_trach_nhiem = float(input("Lương trách nhiệm: "))
            nv = truongphong(ma, ho_ten, luong, luong_trach_nhiem)
        else: 
            print("loại không hợp lệ")
            continue

        ds.append(nv)
    
    print("\n Đã nhập xong danh sách.")
    return ds

def xuat_danh_sach(ds):
    print("\n{:<10} | {:<25} | {:>10} | {:>12} | {:>10}".format("Mã", "Họ tên", "Lương", "Thu nhập", "Thuế"))
    print("-" * 80)
    for nv in ds:
        print(nv)
