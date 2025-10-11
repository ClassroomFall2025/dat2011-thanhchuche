class Sinhvien:
    def __init__(self, ho_ten, diem):
        self.ho_ten = ho_ten
        self.diem = diem 

    def get_hoc_luc(self):
        if self.diem >= 9:
            return "Học lực giỏi"
        elif self.diem >= 6.5:
            return "Học lực khá"
        elif self.diem >= 5:
            return "Học lực trung bình"
        else:
            return "Học lực yếu"
        
    def xuat(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm: {self.diem}")
        print(f"Học lực: {self.get_hoc_luc()}")

ds_sinhvien = []

def nhap_danh_sach():
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"-- sinh vien {i+1} --")
        ho_ten = input("Họ tên: ")
        while True:
            try:
                diem = float(input("Điểm (0-10): "))
                if 0 <= diem <= 10:
                    break
                else:
                    print("Điểm nằm trong khoảng 0 đến 10. Vui lòng nhập lại")
            except ValueError:
                print("Vui lòng nhập số hợp lệ ")
        ds_sinhvien.append(Sinhvien(ho_ten, diem))

def xuat_danh_sach():
    if not ds_sinhvien:
        print("chưa có sinh viên nào được nhập")
        return
    for sv in ds_sinhvien:
        sv.xuat()

def xuat_sv_gioi():
    print("--- Danh sách sinh viên giỏi ---")
    found = False 
    for sv in ds_sinhvien:
        if sv.get_hoc_luc() == "Học lực giỏi":
            sv.xuat()
            found = True 
    if not found:
        print("Không có sinh viên giỏi")
        
def sap_xep_theo_diem():
    ds_sinhvien.sort(key=lambda x: x.diem, reverse = True)
    print("--- Danh sách sau khi xếp ---")
    xuat_danh_sach()