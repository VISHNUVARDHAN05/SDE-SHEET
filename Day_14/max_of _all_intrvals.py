# An efficient Python3 program to find
# maximum of all minimums of windows of
# different sizes

def printMaxOfMin(arr, n):
    s = []  # Used to find previous
    # and next smaller

    # Arrays to store previous and next
    # smaller. Initialize elements of
    # left[] and right[]
    left = [-1] * (n + 1)
    right = [n] * (n + 1)

    # Fill elements of left[] using logic discussed on
    # https:#www.geeksforgeeks.org/next-greater-element
    for i in range(n):
        while (len(s) != 0 and
               arr[s[-1]] >= arr[i]):
            s.pop()

        if (len(s) != 0):
            left[i] = s[-1]

        s.append(i)
    # Empty the stack as stack is going
    # to be used for right[]
    print()
    while (len(s) != 0):
        s.pop()

    # Fill elements of right[] using same logic
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()

        if (len(s) != 0):
            right[i] = s[-1]

        s.append(i)


    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = 0

    for i in range(n):
        Len = right[i] - left[i] - 1
        ans[Len] = max(ans[Len], arr[i])
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])

    # Print the result
    for i in range(1, n + 1):
        print(ans[i], end=" ")


# Driver Code
if __name__ == '__main__':
    arr = [10, 20, 30, 50, 10, 70, 30]
    n = len(arr)
    print(arr)
    printMaxOfMin(arr, n)

# This code is contributed by PranchalK
