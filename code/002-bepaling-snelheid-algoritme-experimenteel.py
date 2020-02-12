"""
|------------------------------------------------------------------------------|
|
|    Tijdsduur van een algoritme bepalen
|    002/
|
|------------------------------------------------------------------------------|
"""

import random
import time

def fetchList(file):
    f = open(file, "r")

    if f.mode == 'r':
        contents = f.read()
        contents = contents.rstrip("\n")
        contents = contents.split(',')
        return contents
    else:
        print("Something went wrong")
        return []

def generateListFile(file):
    f = open(file, "w+")

    A = random.sample(range(1, 10**6), 10**5)

    line = ','.join(str(v) for v in A)

    f.write(line)


""" -------------------------------------------------------------------------"""

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, l, r):
    if l < r:
        m = (l+(r-1)) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

""" -------------------------------------------------------------------------"""

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size

def heapSort(arr, n):
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# generateListFile("list-data-one.txt")

""" -------------------------------------------------------------------------"""

A = fetchList("list-data-one.txt")
nA = len(A)

print("\nTime Taken for " + str(nA) + " elements:")

""" Merge Sort """
""" ~3,2 ms """

start = time.time()
mergeSort(A, 0, nA - 1)
end = time.time()

print("\nMerge Sort:")
print(str(end - start) + "ms")

""" Heap Sort """
""" ~7,2 ms """

start = time.time()
heapSort(A, nA)
end = time.time()

print("\nHeap Sort: ")
print(str(end - start) + "ms")

""" -------------------------------------------------------------------------"""
