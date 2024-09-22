#Tính giai thừa của số nguyên
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n - 1)
k=int(input("Nhập vào số nguyên: "))
print(f"giai thừa của {k}: {giai_thua(k)}")
#Tính tổng chữ số của một số nguyên
def tong_chu_so(n):
   if n==0:
       return 0
   return n % 10 + tong_chu_so(n//10)
k=int(input("Nhập vào số nguyên: "))
print(f"Tổng các chữ số: {tong_chu_so(k)}")
#Đảo ngược chuỗi
def dao_nguoc_chuoi(s):
    return s[::-1]
#Tìm số lớn nhất trong mảng
def tim_son_luong_nhat(mang):
    return max(mang)