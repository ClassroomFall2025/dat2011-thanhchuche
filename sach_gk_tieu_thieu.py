import sach as sv

class QuanLySach:
    def __init__(self):
        self.ds_sach = []

    def nhap_danh_sach(self):
        while True:
            loai = input("Nhập loại sách (KH và TT) (nhập 'exit' để thoát): ").strip().lower()
            if loai == "exit":
                print("Nhập thành công")
                break
            else: 
                ma_sach = input("Nhập mã sách: ")
                ten_sach = input("Nhập tên sách: ")
                nha_xuat_ban = input("Nhập nhà xuất bản: ")
                gia_goc = float(input("Nhập giá gốc: "))
                da_ban = int(input("Nhập số lượng bán: "))
                if loai.lower() == "kh":
                    linh_vuc = input("Nhập lĩnh vực nghiên cứu: ")
                    sach = sv.SachKhoaHoc(ma_sach, ten_sach, nha_xuat_ban, gia_goc, da_ban, linh_vuc)
                    self.ds_sach.append(sach)
                elif loai.lower() == "tt":
                    ten_tac_gia = input("Nhập tên tác giả: ")
                    sach = sv.SachTieuThuyet(ma_sach, ten_sach, nha_xuat_ban, gia_goc, da_ban, ten_tac_gia)
                    self.ds_sach.append(sach)
        return self.ds_sach
    def xuat_ds_sach(self):
        if not self.ds_sach:
            print("danh sách rỗng")
            return
        print(f'{"Mã sách":<10} | {"Tên sách":<25} | {"Nhà xuất bản":<15} | {"Giá gốc":<10} | {"SL bán":<10} | {"Giá bán":<10} | {"Đánh giá":<12}')
        for sach in self.ds_sach:
            sach.xuat()

    def xuat_sach_ban_chay(self):
        if not self.ds_sach:
            print("Danh sách rống")
            return
        ds_sach_ban_chay = [sach for sach in self.ds_sach if sach.danh_gia_pho_bien() == "Bán chạy"]

        print(f'{"Mã sách":<10} | {"Tên sách":<25} | {"Nhà xuất bản":<15} | {"Giá gốc":<10} | {"SL bán":<10} | {"Giá bán":<10} | {"Đánh giá":<12}')
        for sach in ds_sach_ban_chay:
            sach.xuat()
    def sap_xep_sach(self):
        ds_sach_sap_xep = sorted(self.ds_sach, key = lambda sv: sv.tinh_gia_ban(), reverse = True)
        if not self.ds_sach:
            print("danh sách rỗng")
            return 
        print(f'{"Mã sách":<10} | {"Tên sách":<25} | {"Nhà xuất bản":<15} | {"Giá gốc":<10} | {"SL bán":<10} | {"Giá bán":<10} | {"Đánh giá":<12}')
        for sach in ds_sach_sap_xep:
            sach.xuat()
            