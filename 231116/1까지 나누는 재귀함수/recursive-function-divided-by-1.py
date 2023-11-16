n = int(input())

def recursive(n):
    if n == 1:
        return
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3
    print(n, end=" ")
    recursive(n)
    
print(n, end=" ")
recursive(n)