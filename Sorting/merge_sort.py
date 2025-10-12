
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return  merge(left_half,right_half)
    
def merge(left_arr,right_arr):
    print("left ", left_arr, " and right :", right_arr)
    i=j=0
    sorted_arr = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sorted_arr.append(left_arr[i])
            i += 1
        else:
            sorted_arr.append(right_arr[j])
            j += 1            
    sorted_arr.extend(left_arr[i:])
    sorted_arr.extend(right_arr[j:])
    return sorted_arr
un_sorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(un_sorted_list)
print("Sorted list:", sorted_list)