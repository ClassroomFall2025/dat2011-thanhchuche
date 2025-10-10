from abc import ABC, abstractmethod 

class SinhVienPoly(ABC):
    def __init__(self, ho_ten, nganh):
        self.ho_ten = ho_ten
        self.nganh = nganh 

    @abstractmethod 
    def get_diem(self):
        pass

    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem < 5:
            return "Yếu"
        elif diem < 7:
            return "Trung bình"
        elif diem < 8:
            return "Khá"
        elif diem < 9:
            return "Giỏi"
        else: 
            return "Xuất sắc"
        
    def xuat(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Nghành: {self.nganh}")
        print(f"Điểm: {self.get_diem():.2f}")
        print(f"Học lực: {self.get_hoc_luc()}")

        

class SinhVienIT(SinhVienPoly):
    def __init__(self, ho_ten, diem_java, diem_html, diem_css):
        super().__init__(ho_ten, "Công nghệ thông tin")
        self.diem_java = diem_java
        self.diem_html = diem_html
        self.diem_css = diem_css

    def get_diem(self):
        return (2* self.diem_java + self.diem_html + self.diem_css) / 4
    
    class SinhVienBiz(SinhVienPoly):
        def __init__(self, ho_ten, diem_marketing, diem_sales):
            super().__init__(ho_ten, "Kinh doanh")
            self.diem_marketing = diem_marketing
            self.diem_sales = diem_sales

        def get_diem(self):
            return (2 * self.diem_marketing + self.diem_sales) / 3
        
        