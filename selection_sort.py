def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"selection sort: {arr}")

def selection_sort_excercise(arr):
    for outer in range(len(arr) - 1):
        print(f"selection sort: {arr}")
        for inner in range(len(arr) - 1):
            if arr[inner] > arr[inner + 1]:
                arr[inner], arr[inner + 1] = arr[inner + 1], arr[inner]

l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
selection_sort_excercise(l)
