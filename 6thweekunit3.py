from math import gcd

class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0")
        self.__tu = tu
        self.__mau = mau

    @property
    def tu(self):
        return self.__tu

    @tu.setter
    def tu(self, value):
        self.__tu = value

    @property
    def mau(self):
        return self.__mau

    @mau.setter
    def mau(self, value):
        if value == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0")
        self.__mau = value

    def is_toi_gian(self):
        return gcd(self.__tu, self.__mau) == 1

    def toi_gian(self):
        ucln = gcd(self.__tu, self.__mau)
        return PhanSo(self.__tu // ucln, self.__mau // ucln)

    def __add__(self, other):
        return PhanSo(self.__tu * other.mau + other.tu * self.__mau,
                      self.__mau * other.mau).toi_gian()

    def __sub__(self, other):
        return PhanSo(self.__tu * other.mau - other.tu * self.__mau,
                      self.__mau * other.mau).toi_gian()

    def __mul__(self, other):
        return PhanSo(self.__tu * other.tu, self.__mau * other.mau).toi_gian()

    def __truediv__(self, other):
        return PhanSo(self.__tu * other.mau, self.__mau * other.tu).toi_gian()

    def __eq__(self, other):
        return self.__tu * other.mau == other.tu * self.__mau

    def __lt__(self, other):
        return self.__tu * other.mau < other.tu * self.__mau

    def __gt__(self, other):
        return self.__tu * other.mau > other.tu * self.__mau

    def __str__(self):
        ps = self.toi_gian()
        if ps.mau == 1:
            return str(ps.tu)
        return f"{ps.tu}/{ps.mau}"

    def __repr__(self):
        return f"PhanSo({self.__tu}, {self.__mau})"

    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps.tu, ps.mau))


ds = [PhanSo(2, 4), PhanSo(3, 9), PhanSo(5, 10), PhanSo(7, 2)]

print("Dạng tối giản:")
for ps in ds:
    print(ps)

print("\nSắp xếp tăng dần:")
for ps in sorted(ds):
    print(ps)
