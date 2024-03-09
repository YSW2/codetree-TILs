def roll(x, y, result):
    if x == 0:
        if sum(result) == 9:
            for n in result:
                print(n, end=" ")
            print()
            return

    for i in range(1, 7):
        result.append(i)
        if sum(result) <= 9:
            roll(x-1, y, result)
        result.pop()

x, y = map(int, input().split())

roll(x, y, [])