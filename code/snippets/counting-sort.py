# # The main function that sort the given string arr[] in
# # alphabetical order


# def countSort(arr):

#     # The output character array that will have sorted arr
#     output = [0 for i in range(256)]

#     # Create a count array to store count of inidividul
#     # characters and initialize count array as 0
#     count = [0 for i in range(256)]

#     # For storing the resulting answer since the
#     # string is immutable
#     ans = ["" for _ in arr]

#     # Store count of each character
#     for i in arr:
#         count[ord(i)] += 1

#     # Change count[i] so that count[i] now contains actual
#     # position of this character in output array
#     for i in range(256):
#         count[i] += count[i-1]

#     # Build the output character array
#     for i in range(len(arr)):
#         output[count[ord(arr[i])]-1] = arr[i]
#         count[ord(arr[i])] -= 1

#     # Copy the output array to arr, so that arr now
#     # contains sorted characters
#     for i in range(len(arr)):
#         ans[i] = output[i]
#     return ans


# # # Driver program to test above function
# # arr = "geeksforgeeks"
# # ans = countSort(arr)
# # print "Sorted character array is %s" % ("".join(ans))

# # # This code is contributed by Nikhil Kumar Singh

# output = [0 for i in range(256)]

# print(output)


# =======================================================================
#  Author: Isai Damier
#  Title: Countingsort
#  Project: GeekViewpoint
#  Package: algorithms
#
#  Statement:
#  Given a disordered list of repeated integers, rearrange the
#  integers in natural order.
#
#  Sample Input: [4,3,2,1,4,3,2,4,3,4]
#
#  Sample Output: [1,2,2,3,3,3,4,4,4,4]
#
#  Time Complexity of Solution:
#  Best Case O(n+k); Average Case O(n+k); Worst Case O(n+k),
#  where n is the size of the input array and k means the
#  values range from 0 to k.
#
#  Approach:
#  Counting sort, like radix sort and bucket sort,
#  is an integer based algorithm (i.e. the values of the input
#  array are assumed to be integers). Hence counting sort is
#  among the fastest sorting algorithms around, in theory. The
#  particular distinction for counting sort is that it creates
#  a bucket for each value and keep a counter in each bucket.
#  Then each time a value is encountered in the input collection,
#  the appropriate counter is incremented. Because counting sort
#  creates a bucket for each value, an imposing restriction is
#  that the maximum value in the input array be known beforehand.
#
#  There is a great number of counting sort code on the Internet,
#  including on university websites, that erroneously claim to be
#  bucket sort. Bucket sort uses a hash function to distribute
#  values; counting sort, on the other hand, creates a counter for
#  each value -- hence the name.
#
#  Implementation notes:
#
#  1] Since the values range from 0 to k, create k+1 buckets.
#  2] To fill the buckets, iterate through the input list and
#  each time a value appears, increment the counter in its
#  bucket.
#  3] Now fill the input list with the compressed data in the
#  buckets. Each bucket's key represents a value in the
#  array. So for each bucket, from smallest key to largest,
#  add the index of the bucket to the input array and
#  decrease the counter in said bucket by one; until the
#  counter is zero.
# =======================================================================
def countingsort(aList, k):
    counter = [0] * (k + 1)
    for i in aList:
        counter[i] += 1

    ndx = 0
    print(len(counter))
    for i in range(len(counter)):
        print("i: " + str(i))
        while 0 < counter[i]:
            print("counter[i]: " + str(i))
            print("ndx: " + str(ndx))
            print("aList[ndx]: " + str(aList[ndx]))
            aList[ndx] = i
            print("aList[i]: " + str(aList[ndx]))
            ndx += 1
            print("ndx: " + str(ndx))
            counter[i] -= 1
            print("counter[i]: " + str(i))
            print("###########")


A = [6, 4, 3, 2, 1, 4, 3, 6, 6, 2, 4, 3, 4]
k = 6

countingsort(A, k)
print(A)

# k = 6
# counter = [0] * (k + 1)
# print(counter)

# for i in A:
#     counter[i] += 1

# print(counter)
