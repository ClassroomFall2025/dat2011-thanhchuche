class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia
    def thue_nhap_khau(self):
        return self.gia * 0.1
    def xuat_thong_tin(self):
        print(f"Sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau}")       