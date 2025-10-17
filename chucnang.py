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
        elif thu_nhap <= 15000000:
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
    

def ghi_file_csv(ds_nv):
    with open(FILE_NAME, mode = 'w', newline = '', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Mã NV", "Họ Tên ", "Lương", "Doanh số", "Hoa Hồng", "Lương TN", "Thu Nhập", "Thuế", "Loại NV"])
        for nv in ds_nv:
            writer.writerow(nv.to_list())

def doc_file_csv():
    ds_nv = []
    try:
        with open(FILE_NAME, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                loai = row["Loại NV"]
                ma = row["Mã NV"]
                ho_ten = row["Họ Tên"]  # đã chuẩn hóa
                luong = row["Lương"]

                if loai == "NhanVienHanhChinh":
                    nv = NhanVienHanhChinh(ma, ho_ten, luong)
                elif loai == "TruongPhong":
                    nv = TruongPhong(ma, ho_ten, luong, row["Lương TN"])
                elif loai == "NhanVienTiepThi":
                    nv = NhanVienTiepThi(ma, ho_ten, luong, row["Doanh số"], row["Hoa Hồng"])
                ds_nv.append(nv)
    except FileNotFoundError:
        pass
    return ds_nv


def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số lượng nhân viên: "))
    for i in range(n):
        print(f"\n --- Nhân viên {i+1} ---")
        loai = input("Loại (1-HC, 2-TT, 3-TP): ")
        ma = input("Mã NV: ")
        ten = input("Họ tên: ")
        luong = float(input("Lương: "))

        if loai == "1":
            nv = NhanVienHanhChinh(ma, ten, luong)
        elif loai == "2":
            doanh_so = float(input("Doanh số: "))
            hoa_hong = float(input("Tỉ lệ Hoa Hồng (%): "))
            nv = NhanVienTiepThi(ma, ten, luong, doanh_so, hoa_hong)
        else: 
            luong_tn = float(input("Lương trách nhiệm: "))
            nv = TruongPhong(ma, ten, luong, luong_tn)
        ds.append(nv)

    ghi_file_csv(ds)
    print("Đã lưu danh sách vào file csv.")

def xuat_danh_sach(ds):
    if not ds:
        print("Danh sách trống.")
        return 
    print(f"\n {'Mã NV':<10}")
    print(f"\n{'Họ Tên':<20}")
    print(f"\n{'Thu Nhập':>15}")
    print(f"\n{'Thuế':>15}")
    for nv in ds:
        print(f"{nv.ma_nv:<10}{nv.ho_ten:<20}{nv.tinh_thu_nhap():>15,.0f}{nv.tinh_thue_thu_nhap():>15,.0f}")
    
def tim_theo_ma(ds):
    ma = input("Nhập mã nhân viên cần tìm: ")
    for nv in ds:
        if nv.ma_nv == ma:
            print(f"Tìm thấy: {nv.ho_ten} - Thu nhập: {nv.tinh_thu_nhap():,.0f}")
            return
        print("Không tìm thấy nhân viên nào trong danh sách.")

def xoa_thoe_ma(ds):
    ma = input("Nhập mã nhân viên cần xóa: ")
    ds_moi = [nv for nv in ds if nv.ma_nv != ma]
    ghi_file_csv(ds_moi)
    print("đã cập nhật file sau khi xóa.")

def cap_nhap_thong_tin(ds):
    ma = input("Nhập mã nhân viên cần cập nhật: ")
    for nv in ds:
        if nv.ma_nv == ma:
            nv.ho_ten = input("Nhập họ tên mới: ") or nv.ho_ten
            nv.luong = float(input("Nhập lương mới: ")) or nv.luong
            print("Đã cập nhật thông tin.")
            break
    ghi_file_csv(ds)

def tim_theo_khoang_luong(ds):
    min_1 = float(input("Nhập Lương tối thiểu: "))
    max_1 = float(input("nhập lương tối đa: "))
    kq = [nv for nv in ds if min_1 <= nv.tinh_thu_nhap() <= max_1]
    xuat_danh_sach(kq)

def sap_xep_theo_ten(ds):
    ds.sort(key = lambda nv: nv.ho_ten.split()[-1])
    xuat_danh_sach(ds)

def sap_xep_theo_thu_nhap(ds):
    ds.sort(key = lambda nv: nv.tinh_thu_nhap(), reverse = True)
    xuat_danh_sach(ds)

def top_5(ds):
    ds_top = sorted(ds, key = lambda nv: nv.tinh_thu_nhap(), reverse = True)[:5]
    xuat_danh_sach(ds)