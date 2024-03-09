def roll(x, y, result):
    if x == 0:
        if sum(result) == y:
            for n in result:
                print(n, end=" ")
            print()
            return
    
    if sum(result) > y:
        return
        
    for i in range(1, 7):
        result.append(i)
        roll(x-1, y, result)
        result.pop()

x, y = map(int, input().split())

roll(x, y, [])