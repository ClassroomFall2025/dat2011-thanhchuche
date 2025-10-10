class ChuNhat:
    def __init__(self, dai, rong):
        if dai < 0:
            print("Chiều dài lớn hơn hoặc bằng 0")
            dai = 0
        if rong < 0:
            print("Chiều rộng lớn hơn hoặc bằng 0")
            rong = 0
        self.dai = dai
        self.rong = rong

    def get_chu_vi(self):
        return 2 * (self.dai + self.rong)
    
    def get_dien_tich(self):
        return self.dai * self.rong 
    
    def xuat(self):
        print("------ Hình chữ nhật ------")
        print(f"Chiều rộng: {self.rong}")
        print(f"Chiều dài: {self.dai}")
        print(f"Chu tích: {self.get_chu_vi()}")
        print(f"Diện tích: {self.get_dien_tich()}")
        print("--------------------")



class Vuong(ChuNhat):
    def __init__(self, canh):
        if canh < 0:
            print("Cạnh lớn hơn hoặc bằng 0")
            canh = 0
        super().__init__(canh, canh)
        self.canh = canh 
   
    def xuat(self):
        print("------ Hình vuông ------")
        print(f"Cạnh: {self.dai}")
        print(f"Diện tích: {self.get_dien_tich()}") 
        print(f"Chu vi: {self.get_chu_vi()}")



