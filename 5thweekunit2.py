class NhanVien:
    LUONG_MAX = 50000  

    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._nam_sinh = nam_sinh
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi
        self._he_so_luong = he_so_luong
        self._luong_co_ban = luong_co_ban

    def tinhLuong(self):
        luong = self._luong_co_ban * self._he_so_luong
        return min(luong, NhanVien.LUONG_MAX)

    def inTTin(self):
        print(f"Mã NV: {self._ma_nv}")
        print(f"Họ tên: {self._ho_ten}")
        print(f"Năm sinh: {self._nam_sinh}")
        print(f"Giới tính: {self._gioi_tinh}")
        print(f"Địa chỉ: {self._dia_chi}")
        print(f"Hệ số lương: {self._he_so_luong}")
        print(f"Lương: {self.tinhLuong()}")


class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban, thoi_han_hd, phu_cap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban)
        self._thoi_han_hd = thoi_han_hd
        self._phu_cap = phu_cap

    def tinhLuong(self):
        return min(super().tinhLuong() + self._phu_cap, NhanVien.LUONG_MAX)

    def inTTin(self):
        super().inTTin()
        print(f"Thời hạn hợp đồng: {self._thoi_han_hd}")
        print(f"Phụ cấp lao động: {self._phu_cap}")


class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban, vi_tri):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban)
        self._vi_tri = vi_tri

    def inTTin(self):
        super().inTTin()
        print(f"Vị trí công việc: {self._vi_tri}")


class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban, ngay_batdau, phu_cap_ql):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_co_ban)
        self._ngay_batdau = ngay_batdau
        self._phu_cap_ql = phu_cap_ql

    def tinhLuong(self):
        return min(super().tinhLuong() + self._phu_cap_ql, NhanVien.LUONG_MAX)

    def inTTin(self):
        super().inTTin()
        print(f"Ngày bắt đầu quản lý: {self._ngay_batdau}")
        print(f"Phụ cấp quản lý: {self._phu_cap_ql}")


print("=== Cộng tác viên ===")
ctv = CongTacVien("CTV01", "Nguyễn Văn A", 1995, "Nam", "Hà Nội", 2.0, 6000, "6 tháng", 1000)
ctv.inTTin()

print("\n=== Nhân viên chính thức ===")
nvct = NhanVienChinhThuc("NV01", "Trần Thị B", 1990, "Nữ", "Hà Nội", 3.0, 7000, "Kế toán")
nvct.inTTin()

print("\n=== Trưởng phòng ===")
tp = TruongPhong("TP01", "Lê Văn C", 1985, "Nam", "Hà Nội", 4.0, 8000, "01/01/2020", 5000)
tp.inTTin()
