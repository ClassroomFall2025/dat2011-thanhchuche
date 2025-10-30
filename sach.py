class Sach:
    def __init__(self, ma_sach, ten_sach, nha_xuat_ban, gia_goc,da_ban):
        self.__ma_sach = ma_sach
        self.__ten_sach = ten_sach
        self.__nha_xuat_ban = nha_xuat_ban
        self.__gia_goc = gia_goc
        self.__da_ban = da_ban

    def get_ma_sach(self):
        return self.__ma_sach
    def set_ma_sach(self, sach_moi):
        self.__ma_sach = sach_moi
    
    def get_ten_sach(self):
        return self.__ten_sach
    def set_ten_sach(self, ten_sach_moi):
        self.__ten_sach = ten_sach_moi

    def get_nha_xuat_ban(self):
        return self.__nha_xuat_ban
    def set_nha_xuat_ban(self, nha_xuat_ban):
        self.__nha_xuat_ban = nha_xuat_ban

    def get_gia_goc(self):
        return self.__gia_goc
    def set_nha_xuat_ban(self, gia_moi):
        self.__gia_goc = gia_moi

    def get_da_ban(self):
        return self.__da_ban
    def set_nha_xuat_ban(self, da_ban):
        self.__da_ban = da_ban

    def tinh_gia_ban(self):
        pass

    def danh_gia_pho_bien(self):
        if self.__da_ban() >= 5000:
            da_ban = "Bán chạy"
        elif self.__da_ban() >= 1000:
            da_ban = "Phổ biến"
        else:
            da_ban = "Ít phổ biến"
        return da_ban
      
    def xuat(self):
        print(f"{self.get_ma_sach:<10} | {self.get_ten_sach:<20} | {self.get_nha_xuat_ban:<15} | {self.get_gia_goc:<10,.0f} | {self.get_da_ban():<10} | {self.danh_gia_pho_bien():<12} | {self.tinh_gia_ban():<10,.0f}")


class SachKhoaHoc(Sach):
    def __init__(self, ma_sach, ten_sach, nha_xuat_ban, gia_goc, da_ban, linh_vuc):
        super().__init__(ma_sach, ten_sach, nha_xuat_ban, gia_goc, da_ban)
        self.__linh_vuc = linh_vuc

    def get_linh_vuc(self):
        return self.__linh_vuc

    def set_linh_vuc(self, linh_vuc):
        self.__linh_vuc = linh_vuc

    def tinh_gia_ban(self):
        return self.get_gia_goc() * 1.3
    
class SachTieuThuyet(Sach):
    def __init__(self, ma_sach, ten_sach, nha_xuat_ban, gia_goc, da_ban, ten_tac_gia):
        super().__init__(ma_sach, ten_sach, nha_xuat_ban, gia_goc, da_ban)
        self.__ten_tac_gia = ten_tac_gia

    def get_ten_tac_gia(self):
        return self.__ten_tac_gia

    def set_ten_tac_gia(self, ten_tac_gia):
        self.__ten_tac_gia = ten_tac_gia

    def tinh_gia_ban(self):
        return self.get_gia_goc() * 1.5