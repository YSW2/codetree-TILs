n, m = map(int, input().split())

def throw(arr, n, m):
    if sum(arr) + (n-len(arr)) * 6 < m:
        return
        
    if sum(arr) > m:
        return
    
    if len(arr) == n and sum(arr) == m:
        for num in arr:
            print(num, end=" ")
        print()
        return
    
    for i in range(1, 7):
        arr.append(i)
        throw(arr, n, m)
        arr.pop()

throw([], n, m)