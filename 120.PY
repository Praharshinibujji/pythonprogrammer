def kthSmallest(array, n, k): 
    array.sort() 
    return array[k-1] 
if __name__=='__main__': 
    array = [1,2,3,4,5] 
    n = len(array) 
    k = 3
print(kthSmallest(array, n, k))
