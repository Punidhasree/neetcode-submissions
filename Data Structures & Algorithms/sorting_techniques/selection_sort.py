def selection_sort(arr):
    for i in range(len(arr) - 1):
        mini = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j

        arr[mini], arr[i] = arr[i], arr[mini]

    return arr


arr = [6, 3, 5, 9, 13, 54, 2]

print(selection_sort(arr))