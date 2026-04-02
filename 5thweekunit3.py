class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self._ho_ten = ho_ten
        self._tuoi = tuoi
        self._gioi_tinh = gioi_tinh
        self._dia_chi = dia_chi

    def inTTin(self):
        print(f"Họ tên: {self._ho_ten}")
        print(f"Tuổi: {self._tuoi}")
        print(f"Giới tính: {self._gioi_tinh}")
        print(f"Địa chỉ: {self._dia_chi}")


class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._bac = bac

    def inTTin(self):
        super().inTTin()
        print(f"Bậc công nhân: {self._bac}")


class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh_dt):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._nganh_dt = nganh_dt

    def inTTin(self):
        super().inTTin()
        print(f"Ngành đào tạo: {self._nganh_dt}")


class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self._cong_viec = cong_viec

    def inTTin(self):
        super().inTTin()
        print(f"Công việc: {self._cong_viec}")


class QLCB:
    def __init__(self):
        self.ds_canbo = []

    def themCanBo(self, canbo):
        self.ds_canbo.append(canbo)

    def timKiemTheoTen(self, ten):
        ket_qua = [cb for cb in self.ds_canbo if cb._ho_ten == ten]
        return ket_qua

    def hienThiDS(self):
        for cb in self.ds_canbo:
            cb.inTTin()
            print("-" * 30)


ql = QLCB()

cn = CongNhan("Nguyễn Văn A", 30, "Nam", "Hà Nội", 5)
ks = KySu("Hồ Thị B", 28, "Nữ", "Hải Phòng", "Công nghệ thông tin")
nv = NhanVien("Đỗ Văn C", 35, "Nam", "Đà Nẵng", "Kế toán")

ql.themCanBo(cn)
ql.themCanBo(ks)
ql.themCanBo(nv)

print("=== Danh sách cán bộ ===")
ql.hienThiDS()

print("\n=== Tìm kiếm theo tên ===")
ket_qua = ql.timKiemTheoTen("Trần Thị B")
for cb in ket_qua:
    cb.inTTin()
