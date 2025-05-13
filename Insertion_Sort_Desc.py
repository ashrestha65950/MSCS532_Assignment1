# This function sorts an array in descending order using insertion sort

def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    data = [5, 2, 4, 6, 1, 3]
    print("Original array:", data)
    sorted_data = insertion_sort_desc(data)
    print("Sorted in decreasing order:", sorted_data)
