class SanPham:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia
        self.giam_gia = giam_gia

    def doc_giam_gia(self):
        return self.giam_gia
    def ghi_giam_gia(self, giam_gia_moi):
        self.giam_gia = giam_gia_moi 

    def thue_nhap_khau(self):
        return self.gia * 0.1
    
    def xuat_thong_tin(self):
        print(f"Sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau}")       
    def __str__(self):
        return f"Sản phẩm {self.ten_san_pham} có giá {self.gia} được giảm giá {self.giam_gia} và thuế nhập khẩu {self.thue_nhap_khau}"

