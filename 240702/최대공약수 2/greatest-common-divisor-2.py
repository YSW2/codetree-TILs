n = int(input())
number = map(int, input().split())
number_divisor = [[] for _ in range(n)]
answer = 0

for index, num in enumerate(number):
    for n in range(1, int(num**0.5 + 1)):
        if num % n == 0:
            number_divisor[index].append(n)
            if num // n != n:
                number_divisor[index].append(num // n)

for index, divisor in enumerate(number_divisor[:-1]):
    for comp in number_divisor[index+1:]:
        GCD = [div for div in divisor if div in comp]
        answer += max(GCD)

print(answer)