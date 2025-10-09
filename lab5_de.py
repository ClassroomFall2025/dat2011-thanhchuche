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



class SanPham3:
    def __init__(self, ten_san_pham="", gia=0, giam_gia=0):
        self.ten_san_pham = ten_san_pham
        self.gia = gia 
        self.giam_gia = giam_gia
    def nhap(self):
        self.ten_san_pham = input("nhập tên sản phầm: ")
        self.gia = float(input("nhập đơn giá: "))
        self.giam_gia = float(input("nhập giảm giá: "))
    
    def get_ten_san_pham(self):
        return self.__ten_san_pham
    def set_ten_san_pham(self, ten_san_pham):
        self.__ten_san_pham = ten_san_pham

    def get_gia(self):
        return self.__gia 
    def set_gia(self, gia):
        self.__gia = gia

    def get_giam_gia(self):
        return self.__giam_gia
    def set_giam_gia(self, giam_gia):
        if giam_gia < 0:
            print("giảm giá không hợp lệ! phải >= 0.")
        else:
            self.__giam_gia = giam_gia

    def tinh_thue_nhap_khau(self):
        self.__ten_san_pham = input("Nhập tên sản phẩm: ")
        self.__gia = float(input("Nhập giá sản phẩm: "))
        self.__giam_gia = float(input("Nhập giảm giá"))

    def xuat(self):
        print("Tên sản phẩm: {self.__ten_san_pham}")
        print(f"Đơn giá: {self.__gia:,.0f} VND")
        print(f"Giảm giá: {self.__giam_gia:,.0f} VND")
        print(f"Thuế nhập khẩu: {self.__tinh_thue_nhap_khau():,.0f} VND")
        print("==================")

    

    