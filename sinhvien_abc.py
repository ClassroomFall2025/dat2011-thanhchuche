class Sinhvien:
    def __init__(self, ho_ten, ma_so_sv, nghanh_hoc):
        self.__ho_ten = ho_ten
        self.__ma_so_sv = ma_so_sv
        self.__nghanh_hoc = nghanh_hoc

    def get_ho_ten(self):
        return self.__ho_ten
    def set_ho_ten(self, ten_moi):
        self.__ho_ten = ten_moi
    
    def get_ma_so_sv(self):
        return self.__ma_so_sv
    def set_ma_so_sv(self, mssv_moi):
        self.__ma_so_sv = mssv_moi

    def get_nghanh_hoc(self):
        return self.__nghanh_hoc
    def set_nghang_hoc(self, nghanh_hoc_moi):
        self.__nghanh_hoc = nghanh_hoc_moi

    def get_diem(self):
        pass

    def get_hoc_luc(self):
        if self.get_diem() >= 9:
            ho_luc = "giỏi"
        elif self.get_diem() >= 6.5:
            ho_luc = "khá"
        elif self.get_diem() >= 5:
            ho_luc = "trung bình"
        else:
            ho_luc = "chưa đạt"
        return ho_luc
      
    def xuat(self):
        print(f'{self.get_ho_ten():<20} | {self.get_ma_so_sv():<10} | {self.get_nghanh_hoc():<20} | {self.get_diem():<10} | {self.get_hoc_luc():<15}')


class SinhVienCNTT(Sinhvien):
    def __init__(self, ho_ten, ma_so_sv, nghanh_hoc, diem_web, diem_css, diem_sql):
        super().__init__(ho_ten, ma_so_sv, nghanh_hoc)
        self.__web = diem_web
        self.__css = diem_css
        self.__sql = diem_sql

    def get_web(self):
        return self.__web
    def set_web(self, web_moi):
        self.__web = web_moi
    
    def get_css(self):
        return self.__css
    def set_css(self, css_moi):
        self.__css = css_moi

    def get_sql(self):
        return self.__sql
    def set_sql(self, sql_moi):
        self.__sql = sql_moi

    def get_diem(self):
        return (self.get_web() * 0.2 + self.get_css * 0.35 + self.get_sql * 0.45)
    
class SinhVienXLDL(Sinhvien):
    def __init__(self, ho_ten, ma_so_sv, nghanh_hoc, diem_python, diem_numpy, diem_pandas):
        super().__init__(ho_ten, ma_so_sv, nghanh_hoc)
        self.__python = diem_python
        self.__numpy = diem_numpy
        self.__pandas = diem_pandas

    def get_python(self):
        return self.__python
    def set_python(self, python_moi):
        self.__python = python_moi
    
    def get_numpy(self):
        return self.__numpy
    def set_numpy(self, numpy_moi):
        self.__numpy = numpy_moi

    def get_pandas(self):
        return self.__pandas
    def set_pandas(self, pandas_moi):
        self.__pandas = pandas_moi

    def get_diem(self):
        return (self.get_python() * 0.2 + self.get_numpy * 0.35 + self.get_pandas * 0.45)
    
    