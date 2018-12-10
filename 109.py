def findK(m, n): 
    half = int((n + 1) / 2) 
    if m > n: 
        return (2 * (m - half)) 
    else: 
        return (2 * m- 1) 
m = 4
n = 2
print(findK(m, n)) 
