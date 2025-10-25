import sinhvien_abc as sv

class QuanLYSV:
    def __init__(self):
        self.ds_sv = []

    def nhap_ds_sv(self):
        while True:
            nghanh_hoc = input("nghành học")
            if nghanh_hoc == "exit":
                print("thoát nhập")
                break
            else: 
                ho_ten = input("nhập họ tên: ")
                ma_so_sv = input("mã số sinh viên: ")
                if nghanh_hoc.lower() == "it":
                    diem_web = float(input("nhập điểm web: "))
                    diem_css = float(input("nhập điểm css: "))
                    diem_sql = float(input("nhập điểm sql: "))
                    sinh_vien = sv.SinhVienCNTT(ho_ten, ma_so_sv, nghanh_hoc, diem_web, diem_css, diem_sql)
                    self.ds_sv(sinh_vien)
                elif nghanh_hoc.lower() == "XLDL":
                    diem_python = float(input("nhập điểm python: "))
                    diem_numpy = float(input("nhập điểm numpy: "))
                    diem_pandas = float(input("nhập điểm pandas: "))
                    sinh_vien = sv.SinhVienCNTT(ho_ten, ma_so_sv, nghanh_hoc, diem_python, diem_numpy, diem_pandas)
                    self.ds_sv(sinh_vien)
        return self.ds_sv
    def xuat_dssv(self):
        if not self.ds_sv:
            print("danh sách rỗng")
            return
        print(f'{"Họ tên":<20} | {"Mã số sinh viên":<10} | {"nghành học":<20} | {"điểm":<10} | {"học lực":<15}')
        for sinh_vien in self.ds_sv:
            sv.xuat()               