class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self._nha_sx = nha_sx
        self._gia = gia

    def getMaHang(self):
        return self._ma_hang

    def setMaHang(self, ma_hang):
        self._ma_hang = ma_hang

    def getTenHang(self):
        return self._ten_hang

    def setTenHang(self, ten_hang):
        self._ten_hang = ten_hang

    def getNhaSX(self):
        return self._nha_sx

    def setNhaSX(self, nha_sx):
        self._nha_sx = nha_sx

    def getGia(self):
        return self._gia

    def setGia(self, gia):
        self._gia = gia

    def inTTin(self):
        print(f"Mã hàng: {self._ma_hang}")
        print(f"Tên hàng: {self._ten_hang}")
        print(f"Nhà sản xuất: {self._nha_sx}")
        print(f"Giá: {self._gia}")


class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._tg_baohanh = tg_baohanh
        self._dien_ap = dien_ap
        self._cong_suat = cong_suat

    def inTTin(self):
        super().inTTin()
        print(f"Thời gian bảo hành: {self._tg_baohanh} tháng")
        print(f"Điện áp: {self._dien_ap} V")
        print(f"Công suất: {self._cong_suat} W")


class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyenlieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._loai_nguyenlieu = loai_nguyenlieu

    def inTTin(self):
        super().inTTin()
        print(f"Loại nguyên liệu: {self._loai_nguyenlieu}")


class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self._ngay_sx = ngay_sx
        self._ngay_hethan = ngay_hethan

    def inTTin(self):
        super().inTTin()
        print(f"Ngày sản xuất: {self._ngay_sx}")
        print(f"Ngày hết hạn: {self._ngay_hethan}")


print("=== Hàng điện máy ===")
dm = HangDienMay("DM01", "Máy giặt", "LG", 8000000, 24, 220, 500)
dm.inTTin()

print("\n=== Hàng sành sứ ===")
ss = HangSanhSu("SS01", "Bộ ấm chén", "Bát Tràng", 1500000, "Gốm sứ cao cấp")
ss.inTTin()

print("\n=== Hàng thực phẩm ===")
tp = HangThucPham("TP01", "Sữa tươi", "Vinamilk", 35000, "01/04/2026", "15/04/2026")
tp.inTTin()
