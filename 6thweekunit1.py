from abc import ABC, abstractmethod

class GiaKhongHopLe(Exception):
    pass

class MaHangTrungLap(Exception):
    pass


class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang
        self._ten_hang = ten_hang
        self.gia = gia 

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe("Giá không hợp lệ, phải >= 0")
        self._gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def inTTin(self):
        pass

    def __str__(self):
        return f"[{self.ma_hang}] {self.ten_hang} - {self.gia} VND"

    def __eq__(self, other):
        return self.ma_hang == other.ma_hang

    def __lt__(self, other):
        return self.gia < other.gia

    def __hash__(self):
        return hash(self.ma_hang)


class HangDienMay(HangHoa):
    def loai_hang(self):
        return "Điện Máy"

    def inTTin(self):
        return f"{self.loai_hang()} | {super().__str__()}"


class HangSanhSu(HangHoa):
    def loai_hang(self):
        return "Sành Sứ"

    def inTTin(self):
        return f"{self.loai_hang()} | {super().__str__()}"


class HangThucPham(HangHoa):
    def loai_hang(self):
        return "Thực Phẩm"

    def inTTin(self):
        return f"{self.loai_hang()} | {super().__str__()}"


class QuanLyHangHoa:
    def __init__(self):
        self.ds = {}

    def them_hang(self, sp: HangHoa):
        if sp.ma_hang in self.ds:
            raise MaHangTrungLap("Mã hàng đã tồn tại")
        self.ds[sp.ma_hang] = sp

    def in_danh_sach(self):
        for sp in self.ds.values():
            print(sp.inTTin())

    def luu_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for sp in self.ds.values():
                f.write(sp.inTTin() + "\n")

    def doc_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()


if __name__ == "__main__":
    ql = QuanLyHangHoa()
    try:
        ql.them_hang(HangDienMay("DM01", "Tivi Samsung", 12000000))
        ql.them_hang(HangSanhSu("SS01", "Bát gốm", 50000))
        ql.them_hang(HangThucPham("TP01", "Gạo ST25", 20000))
    except (GiaKhongHopLe, MaHangTrungLap) as e:
        print("Lỗi:", e)

    print("=== Danh sách hàng hóa ===")
    ql.in_danh_sach()

    print("\n=== Sắp xếp theo giá ===")
    for sp in sorted(ql.ds.values()):
        print(sp)

    ql.luu_file("hanghoa.txt")
    print("\n=== Nội dung file ===")
    print(ql.doc_file("hanghoa.txt"))
