# Định nghĩa lại lớp và thêm menu điều khiển với các yêu cầu từ hình ảnh
import random

# Định nghĩa lớp KhoaHoc


class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        return f"Mã Khóa Học: {self.maKhoaHoc}, Tên Khóa Học: {self.tenKhoaHoc}, Hình Thức: {self.hinhThuc}, Học Phí: {self.hocPhi} VND"

# Định nghĩa lớp HocVien


class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        if not self.khoaHoc:
            return f"Học viên {self.tenHV} chưa đăng ký khóa học nào."
        else:
            return f"Học viên {self.tenHV} đã đăng ký các khóa học: " + ", ".join([khoaHoc.tenKhoaHoc for khoaHoc in self.khoaHoc])


# Danh sách học viên và khóa học
hocViens = []
khoaHocs = []

# Hàm thêm học viên


def themHocVien():
    maHV = input("Nhập mã học viên: ")
    tenHV = input("Nhập tên học viên: ")
    ngaySinh = input("Nhập ngày sinh (DD/MM/YYYY): ")
    hocVien = HocVien(maHV, tenHV, ngaySinh)
    hocViens.append(hocVien)
    print(f"Đã thêm học viên: {tenHV}")

# Hàm thêm khóa học


def themKhoaHoc():
    maKhoaHoc = input("Nhập mã khóa học: ")
    tenKhoaHoc = input("Nhập tên khóa học: ")
    hinhThuc = input("Nhập hình thức học: ")
    hocPhi = float(input("Nhập học phí: "))
    khoaHoc = KhoaHoc(maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi)
    khoaHocs.append(khoaHoc)
    print(f"Đã thêm khóa học: {tenKhoaHoc}")

# Hàm đăng ký khóa học cho học viên


def dangKyKhoaHoc():
    maHV = input("Nhập mã học viên: ")
    maKhoaHoc = input("Nhập mã khóa học: ")

    hocVien = next((hv for hv in hocViens if hv.maHV == maHV), None)
    khoaHoc = next((kh for kh in khoaHocs if kh.maKhoaHoc == maKhoaHoc), None)

    if hocVien and khoaHoc:
        hocVien.dangKyKhoaHoc(khoaHoc)
        print(
            f"Học viên {hocVien.tenHV} đã đăng ký khóa học {khoaHoc.tenKhoaHoc}")
    else:
        print("Không tìm thấy học viên hoặc khóa học.")

# Hàm hiển thị khóa học của học viên


def hienThiKhoaHoc():
    maHV = input("Nhập mã học viên: ")
    hocVien = next((hv for hv in hocViens if hv.maHV == maHV), None)
    if hocVien:
        print(hocVien.hienThiKhoaHoc())
    else:
        print("Không tìm thấy học viên.")

# Hàm hiển thị thông tin khóa học


def thongTinKhoaHoc():
    if not khoaHocs:
        print("Hiện không có khóa học nào.")
    else:
        for khoaHoc in khoaHocs:
            print(khoaHoc.thongTinKhoaHoc())


# Hàm tạo dữ liệu học viên giả
def taoHocVienFake(soLuong):
    danhSachHocVienFake = []
    for i in range(1, soLuong + 1):
        maHV = f"HV{str(i).zfill(3)}"
        tenHV = f"Học Viên {i}"
        ngaySinh = f"{random.randint(1, 28)}/{random.randint(1, 12)}/199{random.randint(0, 9)}"
        hocVien = HocVien(maHV, tenHV, ngaySinh)
        danhSachHocVienFake.append(hocVien)
    return danhSachHocVienFake

# Hàm tạo dữ liệu khóa học giả


def taoKhoaHocFake(soLuong):
    danhSachKhoaHocFake = []
    for i in range(1, soLuong + 1):
        maKhoaHoc = f"KH{str(i).zfill(3)}"
        tenKhoaHoc = f"Khóa Học {i}"
        hinhThuc = random.choice(["Online", "Offline"])
        hocPhi = random.randint(1000000, 5000000)
        khoaHoc = KhoaHoc(maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi)
        danhSachKhoaHocFake.append(khoaHoc)
    return danhSachKhoaHocFake


def menu():
    while True:
        print("\nNhập yêu cầu:")
        print("1/ Thêm học viên (thủ công hoặc tự động)")
        print("2/ Đăng ký khóa học")
        print("3/ Hiển thị khóa học")
        print("4/ Thêm khóa học")
        print("5/ Thông tin khóa học")
        print("6/ Hiển thị thông tin học viên")
        print("0/ Thoát")

        luaChon = input("Lựa chọn của bạn: ")

        if luaChon == '1':
            auto_or_manual = input(
                "Bạn muốn nhập thủ công hay tạo nhanh dữ liệu? (nhập/tạo): ").strip().lower()
            if auto_or_manual == "tạo":
                soLuong = int(input("Nhập số lượng học viên muốn tạo: "))
                hocViens.extend(taoHocVienFake(soLuong))
                print(f"Đã tạo {soLuong} học viên giả.")
            else:
                themHocVien()
        elif luaChon == '2':
            dangKyKhoaHoc()
        elif luaChon == '3':
            hienThiKhoaHoc()
        elif luaChon == '4':
            auto_or_manual = input(
                "Bạn muốn nhập thủ công hay tạo nhanh dữ liệu? (nhập/tạo): ").strip().lower()
            if auto_or_manual == "tạo":
                soLuong = int(input("Nhập số lượng khóa học muốn tạo: "))
                khoaHocs.extend(taoKhoaHocFake(soLuong))
                print(f"Đã tạo {soLuong} khóa học giả.")
            else:
                themKhoaHoc()
        elif luaChon == '5':
            thongTinKhoaHoc()
        elif luaChon == '6':
            if not hocViens:
                print("Hiện không có học viên nào.")
            else:
                for hocVien in hocViens:
                    print(f"Mã Học Viên: {hocVien.maHV}, Tên Học Viên: {hocVien.tenHV}, Ngày Sinh: {hocVien.ngaySinh}")
        elif luaChon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


# Chạy chương trình
menu()
