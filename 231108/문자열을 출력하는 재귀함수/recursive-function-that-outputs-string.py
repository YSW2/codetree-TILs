n = int(input())

def recursion(n):
    if n == 0:
        return
    print("Coding is my favorite hobby!")
    recursion(n-1)

recursion(n)