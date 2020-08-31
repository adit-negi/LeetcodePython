def removeDuplicates(arr, n):
    if n == 0 or n == 1:
        return n

    # To store index of next
    # unique element
    j = 0

    # Doing same as done
    # in Method 1 Just
    # maintaining another
    # updated index i.e. j
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1

    arr[j] = arr[n-1]
    j += 1
    return j


# Driver code
arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = len(arr)

# removeDuplicates() returns
# new size of array.
n = removeDuplicates(arr, n)
print(n)
# Print updated array
for i in range(0, n):
    # print(i)
    #print(" %d " % (arr[i]), end=" ")
    pass
