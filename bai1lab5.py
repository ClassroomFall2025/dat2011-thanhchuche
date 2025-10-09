class Sanpham1:
    def __init__(self, ten, gia, giam_gia):
        self.ten = ten 
        self.gia = gia 
        self.giam_gia = giam_gia
    
    def tinh_thue_nhap_khau(self):
        return self.gia * 0.1    
    
    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.ten}")
        print(f"Đơn giá: {self.gia:,.0f} VND")
        print(f"Giảm giá: {self.giam_gia:,.0f} VND")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau():,.0f} VND")
        print("===========================")   