class NhanVien:
    LUONG_MAX = 20000  

    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self._tenNhanVien = tenNhanVien
        self._luongCoBan = luongCoBan
        self._heSoLuong = heSoLuong

    def getTenNhanVien(self):
        return self._tenNhanVien

    def setTenNhanVien(self, tenNhanVien):
        self._tenNhanVien = tenNhanVien

    def getLuongCoBan(self):
        return self._luongCoBan

    def setLuongCoBan(self, luongCoBan):
        self._luongCoBan = luongCoBan

    def getHeSoLuong(self):
        return self._heSoLuong

    def setHeSoLuong(self, heSoLuong):
        self._heSoLuong = heSoLuong

    def tinhLuong(self):
        return self._luongCoBan * self._heSoLuong

    def tangLuong(self, delta):
        heSoMoi = self._heSoLuong + delta
        luongMoi = self._luongCoBan * heSoMoi
        if luongMoi > NhanVien.LUONG_MAX:
            print(" Lương mới vượt quá mức tối đa cho phép!")
            return False
        else:
            self._heSoLuong = heSoMoi
            return True

    def inTTin(self):
        print("Tên nhân viên:", self._tenNhanVien)
        print("Lương cơ bản:", self._luongCoBan)
        print("Hệ số lương:", self._heSoLuong)
        print("Lương hiện tại:", self.tinhLuong())


nv1 = NhanVien("Nguyễn Văn A", 5000, 2.5)
nv1.inTTin()

print("\n Tăng hệ số lương thêm 0.5:")
nv1.tangLuong(0.5)
nv1.inTTin()

print("\n Tăng hệ số lương thêm 3.0:")
nv1.tangLuong(3.0)
nv1.inTTin()
