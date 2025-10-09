class SanPham1:
    def __init__(self, ten_san_pham, gia, giam_gia):
        self.ten_san_pham = ten_san_pham
        self.gia = gia 
        self.giam_gia = giam_gia
    
    def tinh_thue_nhap_khau(self):
        return self.gia * 0.1    
    
    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.ten_san_pham}")
        print(f"Đơn giá: {self.gia:,.0f} VND")
        print(f"Giảm giá: {self.giam_gia:,.0f} VND")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau():,.0f} VND")
        print("===========================")   



class SanPham2:
    def __init__(self, ten_san_pham="", gia=0, giam_gia=0):
        self.ten_san_pham = ten_san_pham
        self.gia = gia 
        self.giam_gia = giam_gia

    def nhap(self):
        self.ten_san_pham = input("nhập tên sản phầm: ")
        self.gia = float(input("nhập đơn giá: "))
        self.giam_gia = float(input("nhập giảm giá: "))

    
    def tinh_thue_nhap_khau(self):
        return self.gia * 0.1    
    
    def xuat_thong_tin(self):
        print(f"Tên sản phẩm: {self.ten_san_pham}")
        print(f"Đơn giá: {self.gia:,.0f} VND")
        print(f"Giảm giá: {self.giam_gia:,.0f} VND")
        print(f"Thuế nhập khẩu: {self.tinh_thue_nhap_khau():,.0f} VND")
        print("===========================")   