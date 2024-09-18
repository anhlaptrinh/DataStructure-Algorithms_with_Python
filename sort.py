#Selection sort
def selection_sort(arr):
    leng=len(arr)
    for i in range(leng):
        min_index=i
        for j in range(i+1,leng):
            if arr[min_index]>arr[j]:
                min_index=j
                arr[i],arr[min_index]=arr[min_index],arr[i]
                print(arr)
                return arr
#Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
            print(arr)
            return arr
#Quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # Choose the first element as the pivot
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


