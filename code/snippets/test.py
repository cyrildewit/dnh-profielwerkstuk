def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


def bubbleSort(array, size):
    temp = None
    for i in range(size - 1):
        for j in range(i):
            if array[j] > array[j+1]:
                (array[j], array[j + 1]) = (array[j + 1], array[j])


# def partition(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end

#     print("\nPivot: ", pivot, array[pivot])
#     print("Low: ", low, array[low])
#     print("High: ", high, array[high])
#     print("-----------------------")

#     while True:

#         while low <= high and array[high] >= pivot:
#             high = high - 1

#         break

#         # while low <= high and array[low] <= pivot:
#         #     low = low + 1

#         # if low <= high:
#         #     array[low], array[high] = array[high], array[low]
#         # else:
#         #     break

#     print("\nPivot: ", pivot, array[pivot])
#     print("Low: ", low, array[low])
#     print("High: ", high, array[high])
#     print("-----------------------")

#     array[start], array[high] = array[high], array[start]

#     return high

def quickSort(array, low, high):
    if low < high:
        # Partition index
        pi = partition(array, low, high)

        quickSort(array, low, pi - 1) # Before pi
        quickSort(array, pi + 1, high) # After pi

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(high - 1):
        if array[j] < pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

data = [1, 5, -3, -8, 4, 5, 6, 7]
size = len(data)

# selectionSort(data, size)
# bubbleSort(data, size)

print(data)

quickSort(data, 0, size - 1)

print("\n\nSorted array is")
print(data)
# for i in range(size):
#     print("%d" % data[i]),
