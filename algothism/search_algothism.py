listNum = [7, 12, 543, 5556, 78, 454, 443, 23, 4, 565, 891, 25, 14]
# listNum.sort()

# nhap 1 so => tim so trong mang
# co tra ve vi tri cua so do
#khong co tra ve tru 1

#LINEAR SEARCH
# def linear_search(num):
#     for i in range(len(listNum)):
#         if num == listNum[i]:
#             print("Co so can tim trong mang")
#             return i + 1
#     return -1
    
# num=int(input("Nhap vao 1 so: "))
# result=linear_search(num)
# print(f"so can tim co vi tri la {result}"if result!=-1 else "Khong co so can tim")

#BINARY SEARCH
# def binary_search(number):
#     left = 0
#     right = len(listNum) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if listNum[mid] == number:
#             return mid   # 1-based index
#         elif listNum[mid] < number:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# binary = int(input("Nhap vao 1 so: "))
# result = binary_search(binary)
# print(f"so can tim co vi tri la {result}" if result != -1 else "Khong co so can tim")

#BUBBLE SORT
def bubble_sort(number):
    for i in range(len(number)):
        # Flag to track if a swap happened
        swapped = False
        for j in range(len(number) - 1 - i):
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]
                swapped = True
        # If no swaps happened, the list is already sorted
        if not swapped:
            break
    return number
        
print(bubble_sort(listNum))