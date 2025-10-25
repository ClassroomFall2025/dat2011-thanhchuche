class giaidoan1():
    def nhap_danh_sach_va_luu_file():
        print(" Y1. Nhập danh sách nhân viên từ bàn phím. Lưu thông tin nhân viên vào file.")
    def doc_va_xuat_danh_sach():
        print("Y2. Đọc thông tin nhân viên từ file và xuất danh sách nhân viên ra màn hình.")
    def tim_nhan_vien_theo_ma():
        print("Y3. Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.")
    def xoa_nhan_vien_theo_ma():
        print("Y4. Xóa nhân viên theo mã nhập từ bàn phím. Cập nhật file dữ liệu.")
    def cap_nhat_thong_tin_nhan_vien():
        print("Y5. Cập nhật thông tin nhân viên theo mã nhập từ bàn phím và ghi thay đổi vào file.") 
    def tim_nhan_vien_theo_khoang_luong():
        print("Y6. Tìm các nhân viên theo khoảng lương nhập từ bàn phím.")
    def sap_xep_theo_ho_ten():
        print("Y7. Sắp xếp nhân viên theo họ và tên.")
    def sap_xep_theo_thu_nhap():
        print("Y8. Sắp xếp nhân viên theo thu nhập.")
    def xuat_5_nhan_vien_thu_nhap_cao_nhat():
        print("Y9. Xuất 5 nhân viên có thu nhập cao nhất.")

#===================================================================================

class giaidoan2:
    class nhanvien:
        def __init__(self, ma, ho_ten, luong):
            self.ma = ma
            self.ho_ten = ho_ten
            self.luong = float(luong)
        
        def get_thu_nhap(self):
            return self.luong 
        
        def get_thue(self):
            thu_nhap = self.get_thu_nhap()
            if thu_nhap < 9000000:
                return 0
            elif thu_nhap <= 15000000:
                return thu_nhap * 0.1
            else:
                return thu_nhap * 0.12
            
        def __str__(self):
            return f"{self.ma:<8} | {self.ho_ten:<20} | {self.get_thu_nhap():12,.0f} | {self.get_thue():12,.0f}"

    class tiepthi(nhanvien):
        def __init__(self, ma, ho_ten, luong, doanh_so, hoa_hong):
            super().__init__(ma, ho_ten, luong)
            self.doanh_so = doanh_so
            self.hoa_hong = hoa_hong

        def get_thu_nhap(self):
            return self.luong + (self.doanh_so * self.hoa_hong / 100)
        
    class truongphong(nhanvien):
        def __init__(self, ma, ho_ten, luong, luong_trach_nhiem):
            super().__init__(ma, ho_ten, luong)
            self.luong_trach_nhiem = float(luong_trach_nhiem)

    def __init__(self):
        self.ds_nv = []
    
    def nhap_danh_sach(self):
        n = int(input("Nhập số lượng nhân viên: "))
        for i in range(n):
            print(f"\n --- Nhân viên thứ {i + 1} --- ")
            loai = input("Loại (1-Hành chính, 2-Tiếp thị, 3-Trưởng phòng): ")
            ma = input("Mã nhân viên: ")
            ho_ten = input("Họ tên nhân viên: ")
            luong = float(input("Lương cơ bản: "))

            if loai == "1":
                nv = self.nhanvien(ma, ho_ten, luong)
            elif loai == "2":
                doanh_so = float(input("Doanh số: "))
                hoa_hong = float(input("Tỉ lệ hoa hồng: "))
                nv = self.tiepthi(ma, ho_ten, luong, doanh_so, hoa_hong)
            elif loai == "3":
                luong_trach_nhiem = float(input("Lương trách nhiệm: "))
                nv = self.truongphong(ma, ho_ten, luong, luong_trach_nhiem)
            else:
                print("Loại Không hợp lệ bỏ qua")
                continue

            self.ds_nv.append(nv)
        print("\n Đã nhập danh sách nhân viên thành công.")

    def xuat_danh_sach(self):
        print("\n--- Danh sách nhân viên ---")
        for nv in self.ds_nv:
            print(nv)
    
    def tim_theo_ma(self):
        ma = input("Nhập mã nhân viên cần tìm: ")
        for nv in self.ds_nv:
            if nv.ma == ma:
                print("Tìm thấy nhân viên")
                print(nv)
                return 
            print("Không tìm thấy nhân viên có mã này.")

    def tim_theo_khoang_luong(self):
        min_1 = float(input("Nhập lương tối thiểu: "))
        max_1 = float(input("nhập lương tối đa: "))
        print(f"\n nhân có có lương trong khoảng {min_1} - {max_1}: ")
        for nv in self.ds_nv:
            if min_1 <= nv.get_thu_nhap() <= max_1:
                print(nv)
    
    def sap_xep_theo_ten(self):
        self.ds_nv.sort(key=lambda nv: nv.ho_ten.split()[-1])
        print("\n Đã sắp xếp theo họ tên.")

    def sap_xep_theo_thu_nhap(self):
        self.ds_nv.sort(key=lambda nv: nv.get_thu_nhap(), reverse = True)
        print("\n Đã sắp xếp theo thu nhập.")

    def top_5_thu_nhap(self):
        top5 = sorted(self.ds_nv, key=lambda nv: nv.get_thu_nhap(), reverse = True)[0:5]
        print("\n Top 5 nhân viên có thu nhập cao nhất.")
        for nv in top5:
            print(nv)


#=====================================================================

import csv 
import os 

file_name = "nhanvien.csv"
giai_doan = giaidoan2()

def luu_file():
    with open(file_name, mode = 'w', newline =' ', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ma", "ho_ten", "loai", "luong", "doanh_so", "hoa_hong", "luong_trach_nhiem"])
        for nv in giai_doan.ds_nv:
            if isinstance(nv, giaidoan2.tiepthi):
                writer.writerow([nv.ma, nv.ho_ten, "tiepthi", nv.luong, nv.doanh_so, nv.hoa_hong, ""])
            elif isinstance(nv, giaidoan2.truongphong):
                writer.writerow([nv.ma, nv.ho_ten, "truongphong", nv.luong, "", "", nv.luong_trach_nhiem])
            else:
                writer.writerow([nv.ma, nv.ho_ten, "hanhchinh", nv.luong, "", "", ""])
    print("Đã lưu danh sách nhân viên vào file.")

def doc_file():
    if not os.path.exists(file_name):
        print("file không tồn tại.")
        return
    giai_doan.ds_nv.clear()
    with open(file_name, mode = 'r', encoding = 'utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            loai = row["loai"]
            if loai == "tiepthi":
                nv = giaidoan2.tiepthi(row["ma"], row["ho_ten"], float(row["luong"]), float(row["doanh_so"]), float(row["hoa_hong"]))
            elif loai == "truongphong":
                nv = giaidoan2.truongphong(row["ma"], row["ho_ten"], float(row["luong"]), float(row["luong_trach_nhiem"]))
            else:
                nv = giaidoan2.nhanvien(row["ma"], row["ho_ten"], float(row["luong"]))
            giai_doan.ds_nv.append(nv)
        print("Xuất file thành công")

def xoa_nhan_vien():
    ma = input("Nhập mã nhân viên cần xóa: ")
    for nv in giai_doan.ds_nv:
        if nv.ma == ma:
            giai_doan.ds_nv.remove(nv)
            print("Đã xáo nhân viên.")
            luu_file()
            return
    print("Không tìm thấy nhân viên có mã bạn nhập.")

def cap_nhap_nhan_vien():
    ma = input("Nhập mã nhân viên cần cập nhật: ")
    for nv in giai_doan.ds_nv:
        if nv.ma == ma:
            nv.ho_ten = input("Nhập họ tên mới: ") or nv.ho_ten
            nv.luong = float(input("Nhập lương mới: ") or nv.luong)
            if isinstance(nv, giaidoan2.tiepthi):
                nv.doanh_so = float(input("Nhập doanh số mới: ") or nv.doanh_so)
                nv.hoa_hong = float(input("Nhập hoa hồng mới: ") or nv.hoa_hong)
            elif isinstance(nv, giaidoan2.truongphong):
                nv.luong_trach_nhiem = float(input("Nhập lương trách nhiệm mới: ") or nv.luong_trach_nhiem)
            print("Đã cập nhật thông tin nhân viên.")
            luu_file()
            return 
    print("Không tìm thấy nhân viên có mã bạn nhập.")
    