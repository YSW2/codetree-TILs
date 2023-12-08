n = int(input())
answer = float("inf")

def search(n, count):
    global answer

    if n == 1:
        answer = min(answer, count)
        return
    
    if n % 2 == 0:
        search(n//2, count+1)
    
    if n % 3 == 0:
        search(n//3, count+1)
    
    search(n-1, count+1)


search(n, 0)
print(answer)