def heepify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heepify(arr, n, largest)


def heep_sort(arr):
    n = len(arr)
    # Build max-heep
    # Start form last non-leaf node and move backward to the root node
    # This ensure that when you heapify a node, it's children are already valid heaps
    for i in range(n//2-1, -1,-1):
        heepify(arr, n, i)


    print(f"Extraction : ", arr)
    # Now one by one extract elements from the heap
    for end in range(n-1, 0, -1):
        # Mode current root to the end
        arr[0], arr[end] = arr[end], arr[0]
        print("current a[0]", arr[0])
        heepify(arr, end, 0)
        print(f"Extraction : ", arr)

    print("Max Heep : ", arr)












lst = [3, 1, 4, 1, 5, 9, 2, 6]
print("Before : ", lst)
print("After : ", heep_sort(lst.copy()))  