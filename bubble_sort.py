def bubble_sort(arr):
    for i in range(len(arr) - 1):
        print(f"bubble sort: {arr}")
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_excercise(arr):
    for outer in range(len(arr) - 1):
        print(f"bubble sort: {arr}")
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                arr[num], arr[num + 1] = arr[num + 1], arr[num]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort_excercise(l)
