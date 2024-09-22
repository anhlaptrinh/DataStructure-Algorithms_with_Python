class NhanVien:
    def __init__(self, maNV, tenNV,chucVu, luong,heSo):
        self.maNV = maNV
        self.tenNV = tenNV
        self.chucVu=chucVu
        self.luong=luong
        self.heSo=heSo
    def tinhluong(self):
        return  self.heSo * self.luong

class QuanLy(NhanVien):
    def __init__(self, maNV, tenNV,chucVu, luong,heSo,bonus):
        super().__init__(maNV, tenNV,chucVu, luong,heSo)
        self.bonus=bonus
    def tinhluong(self):
        return super().tinhluong() + self.bonus


class GiamDoc(NhanVien):
    def __init__(self, maNV, tenNV,chucVu, luong,heSo):
        super().__init__(maNV, tenNV,chucVu, luong,heSo)

giamdoc=QuanLy(1,'giams 1','GD',5,10,1)
print(giamdoc.tinhluong())