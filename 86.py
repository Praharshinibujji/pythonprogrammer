minimum= int(raw_input())
def smallest(arr,n):
    minimum= arr[0]
    for i in range(1, n):
        if arr[i] < min:
            minimum = arr[i]
    return minimum
arr = [1,2,3,4,5]
n = len(arr)
Ans = smallest(arr,n)
print (Ans)
