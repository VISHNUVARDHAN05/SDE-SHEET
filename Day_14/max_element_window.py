from _collections import deque
def max_element_window(arr,n,k):
    q=deque()
    for i in range(k):
        while q and arr[i]>arr[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k,n):
        print(arr[q[0]])
        while q and q[0]<=i-k:
            q.popleft()

        while q and arr[i]>arr[q[-1]]:
            q.pop()
        q.append(i)

    print(arr[q[0]])



arr = [12, 1, 78, 90, 57, 89, 56]
k = 3
max_element_window(arr, len(arr), k)