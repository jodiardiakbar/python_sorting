def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"selection sort: {arr}")

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort(l)
