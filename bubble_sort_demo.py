# gunakan outer loop
# gunakan inner loop
# geser nilai terbesar ke index -1

def bubble_sort(arr):
    swap_happened = True
    while swap_happened:
        print(f"bubble sort status : {arr}")
        swap_happened = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                swap_happened = True
                arr[num], arr[num + 1] = arr[num + 1], arr[num]


l = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]
bubble_sort(l)