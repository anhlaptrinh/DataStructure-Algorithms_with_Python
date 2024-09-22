class SinhVien:
    def __init__(self, maSV, tenSV, diemToan, diemVan, diemHoa):
        self.maSV = maSV
        self.tenSV = tenSV
        self.diemToan = diemToan
        self.diemVan = diemVan
        self.diemHoa = diemHoa

    def tinhDiemTrungBinh(self):
        return (self.diemToan + self.diemVan + self.diemHoa) / 3

    def __str__(self):
        return f"MaSV: {self.maSV}, TenSV: {self.tenSV}, DiemToan: {self.diemToan}, DiemVan: {self.diemVan}, DiemHoa: {self.diemHoa}, DiemTB: {self.tinhDiemTrungBinh()}"


# Function to input students
def input_students(taoThuCong):
    students = []
    

    if taoThuCong.lower() == "y":
         number_of_students = int(input("Enter the number of students: "))
         for _ in range(number_of_students):
            maSV = input("Enter student ID (maSV): ")
            tenSV = input("Enter student name (tenSV): ")
            diemToan = float(input("Enter Math score (diemToan): "))
            diemVan = float(input("Enter Literature score (diemVan): "))
            diemHoa = float(input("Enter Chemistry score (diemHoa): "))

            student = SinhVien(maSV, tenSV, diemToan, diemVan, diemHoa)
            students.append(student)
    else: students=[
        SinhVien("SV001", "Nguyễn Văn A", 8, 9, 7),
        SinhVien("SV002", "Nguyễn Văn B", 9, 8, 6),
        SinhVien("SV003", "Nguyễn Thị C", 5, 7, 4),
        SinhVien("SV004", "Trần Văn D", 6, 4, 3),
        SinhVien("SV005", "Lê Thị E", 7, 6, 5),
    ]
   

    return students


# Function to print students with average score greater than 5
def print_students_above_average(students):
    print("\nStudents with average score greater than 5:")
    for student in students:
        if student.tinhDiemTrungBinh() > 5:
            print(student)


# Function to print students with chemistry score below 5
def print_students_chemistry_below_5(students):
    print("\nStudents with chemistry score below 5:")
    for student in students:
        if student.diemHoa < 5:
            print(student)


# Main program
if __name__ == "__main__":
    taodanhsach=input("Bạn có muốn tạo danh sách thủ công? Y/N: ")
    students = input_students(taodanhsach)

    # Print all students for reference
    print("\nAll students:")
    for student in students:
        print(student)

    # Call functions to print required students
    print_students_above_average(students)
    print_students_chemistry_below_5(students)
