import math

class PhanSo:
    def __init__(self, tu=0, mau=1) -> None:
        if mau == 0:
            raise ValueError("Mẫu số không thể bằng 0.")
        self.tu = tu
        self.mau = mau
        self.rutGon()

    def rutGon(self):
        ucln = math.gcd(self.tu, self.mau)  # Tính UCLN của tử và mẫu
        self.tu //= ucln  # Rút gọn tử
        self.mau //= ucln  # Rút gọn mẫu
        if self.mau < 0:  # Đảm bảo mẫu luôn dương
            self.tu = -self.tu
            self.mau = -self.mau

    def __add__(self, other):
        if isinstance(other, PhanSo):
            tu = self.tu * other.mau + other.tu * self.mau
            mau = self.mau * other.mau
            return PhanSo(tu, mau)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, PhanSo):
            tu = self.tu * other.mau - other.tu * self.mau
            mau = self.mau * other.mau
            return PhanSo(tu, mau)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, PhanSo):
            tu = self.tu * other.tu
            mau = self.mau * other.mau
            return PhanSo(tu, mau)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, PhanSo):
            if other.tu == 0:
                raise ValueError("Không thể chia cho phân số có tử số bằng 0.")
            tu = self.tu * other.mau
            mau = self.mau * other.tu
            return PhanSo(tu, mau)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, PhanSo):
            return self.tu == other.tu and self.mau == other.mau
        return False

    def __lt__(self, other):
        if isinstance(other, PhanSo):
            return self.tu * other.mau < other.tu * self.mau
        return NotImplemented

    def __str__(self):
        return f"{self.tu}/{self.mau}"

class DanhSachPhanSo:
    def __init__(self):
        self.ds = []

    def themPhanSo(self, phan_so):
        if isinstance(phan_so, PhanSo):
            self.ds.append(phan_so)

    def demPhanSoAm(self):
        return sum(1 for ps in self.ds if ps.tu * ps.mau < 0)

    def timPhanSoDuongNhoNhat(self):
        duong = [ps for ps in self.ds if ps.tu > 0 and ps.mau > 0]
        return min(duong, default=None)

    def timViTriPhanSo(self, x):
        return [i for i, ps in enumerate(self.ds) if ps == x]

    def tongPhanSoAm(self):
        tong = PhanSo(0, 1)
        for ps in self.ds:
            if ps.tu * ps.mau < 0:
                tong += ps
        return tong

    def xoaPhanSo(self, x):
        self.ds = [ps for ps in self.ds if ps != x]

    def xoaPhanSoCoTu(self, tu):
        self.ds = [ps for ps in self.ds if ps.tu != tu]

    def sapXepTang(self):
        self.ds.sort()

    def sapXepGiam(self):
        self.ds.sort(reverse=True)

    def sapXepTangTheoMau(self):
        self.ds.sort(key=lambda ps: ps.mau)

    def sapXepTangTheoTu(self):
        self.ds.sort(key=lambda ps: ps.tu)

    def sapXepGiamTheoMau(self):
        self.ds.sort(key=lambda ps: ps.mau, reverse=True)

    def sapXepGiamTheoTu(self):
        self.ds.sort(key=lambda ps: ps.tu, reverse=True)

# Kiểm tra
phanSo1 = PhanSo(1, 2)
phanSo2 = PhanSo(-3, 4)
phanSo3 = PhanSo(2, 3)
phanSo4 = PhanSo(5, 6)
phanSo5 = PhanSo(-1, 2)

ds = DanhSachPhanSo()
ds.themPhanSo(phanSo1)
ds.themPhanSo(phanSo2)
ds.themPhanSo(phanSo3)
ds.themPhanSo(phanSo4)
ds.themPhanSo(phanSo5)

print("Danh sách phân số:", [str(ps) for ps in ds.ds])
print("Số phân số âm:", ds.demPhanSoAm())
print("Phân số dương nhỏ nhất:", ds.timPhanSoDuongNhoNhat())
print("Vị trí phân số 1/2:", ds.timViTriPhanSo(PhanSo(1, 2)))
print("Tổng các phân số âm:", ds.tongPhanSoAm())
ds.xoaPhanSo(PhanSo(1, 2))
print("Danh sách sau khi xóa 1/2:", [str(ps) for ps in ds.ds])
ds.xoaPhanSoCoTu(-1)
print("Danh sách sau khi xóa tử là -1:", [str(ps) for ps in ds.ds])
ds.sapXepTang()
print("Danh sách sắp xếp tăng dần:", [str(ps) for ps in ds.ds])
