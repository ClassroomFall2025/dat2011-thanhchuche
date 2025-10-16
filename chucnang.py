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


import csv 
FILE_NAME = "nhanvien.csv"

class NhanVien:
    def __init__(self, ma_nv, ho_ten , luong):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong = float(luong)
    
    def tinh_thu_nhap(self):
        return self.luong 
    
    def tinh_thue_thu_nhap(self):
        thu_nhap = self.tinh_thu_nhap()
        if thu_nhap < 9000000:
            return 0
        elif thu_nhap <= 150000000:
            return thu_nhap * 0.1
        else:
            return thu_nhap * 0.12 
        
    def to_list(self):
        return [self.ma_nv, self.ho_ten, self.luong, "","","", self.tinh_thu_nhap(), self.tinh_thue_thu_nhap(), self.__class__.__name__]
    

class NhanVienHanhChinh(NhanVien):
    pass

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong, luong_trach_nhiem):
        super().__init__(ma_nv, ho_ten, luong)
        self.luong_trach_nhiem = float(luong_trach_nhiem)

    def tinh_thu_nhap(self):
        return self.luong + self.luong_trach_nhiem
    
    def to_list(self):
        return [self.ma_nv, self.ho_ten, self.luong, "","", self.luong_trach_nhiem, self.tinh_thu_nhap(), self.tinh_thue_thu_nhap(), self.__class__.__name__]

class NhanVienTiepThi(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong, doanh_so, hoa_hong):
        super().__init__(ma_nv, ho_ten, luong)
        self.doanh_so = float(doanh_so)
        self.hoa_hong = float(hoa_hong)

    def tinh_thu_nhap(self):
        return self.luong + self.doanh_so * self.hoa_hong / 100
    
    def to_list(self):
        return [self.ma_nv, self.ho_ten, self.luong, self.doanh_so, self.hoa_hong, "", self.tinh_thu_nhap(), self.tinh_thue_thu_nhap(), self.__class__.__name__]
    