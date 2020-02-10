import random
import time


def radix_sort(alist, base=10):
    if alist == []:
        return

    def key_factory(digit, base):
        def key(alist, index):
            return ((alist[index]//(base**digit)) % base)
        return key
    largest = max(alist)
    exp = 0
    while base**exp <= largest:
        alist = counting_sort(alist, base - 1, key_factory(exp, base))
        exp = exp + 1
    return alist


def counting_sort(alist, largest, key):
    c = [0]*(largest + 1)
    for i in range(len(alist)):
        c[key(alist, i)] = c[key(alist, i)] + 1

    # Find the last index for each element
    c[0] = c[0] - 1  # to decrement each element for zero-based indexing
    for i in range(1, largest + 1):
        c[i] = c[i] + c[i - 1]

    result = [None]*len(alist)
    for i in range(len(alist) - 1, -1, -1):
        result[c[key(alist, i)]] = alist[i]
        c[key(alist, i)] = c[key(alist, i)] - 1

    return result


# A = [201, 12, 1323, 32, 58, 91, 2, 1, 13, 13314, 21230, 1000, 1200]
# A = random.sample(range(1, 10**8), 10**6)

# print("Unsorted list: ")
# print(A)

# start = time.time()
# radix_sort(A)
# end = time.time()

# print("Sorted list: ")
# print(A)
# print("Time Taken: ")
# print(str(end - start) + "ms")


def key_factory2(digit, base):
    def key(alist, index):
        return ((alist[index]//(base**digit)) % base)
    return key


print(key_factory2(2, 6))
