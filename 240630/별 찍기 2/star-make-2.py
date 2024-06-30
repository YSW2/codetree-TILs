def case1(n):
    for i in range(n//2 + 1):
        print("*" * (i+1))
    
    for i in range(n//2, 0, -1):
        print("*" * (i))
    return

def case2(n):
    for i in range(n//2 + 1):
        print(" " * (n//2 - (i)) + "*" * (i+1))
    
    for i in range(n//2, 0, -1):
        print(" " * (n//2 - (i-1)) + "*" * (i))
    return

def case3(n):
    for i in range(n//2 + 1):
        print(" " * i + "*" * (n - (2*i)) + " " * i)
    
    for i in range(n//2, 0, -1):
        print(" " * (i-1) + "*" * (n - (2*(i-1))) + " " * (i-1))
    return

def case4(n):
    for i in range(n//2 + 1):
        print(" " * i + "*" * (n//2 - i + 1))
    
    for i in range(n//2, 0, -1):
        print(" " * (n//2) + "*" * (n//2 - i + 2))
    return

n, choose = map(int, input().split())
if choose == 1:
    case1(n)
elif choose == 2:
    case2(n)
elif choose == 3:
    case3(n)
elif choose == 4:
    case4(n)