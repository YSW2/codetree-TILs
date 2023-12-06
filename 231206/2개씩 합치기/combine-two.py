import heapq

n = int(input())
arr = list(map(int, input().split()))
answer = 0

while len(arr) > 1:
    heapq.heapify(arr)
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)

    answer += num1 + num2
    heapq.heappush(arr, num1+num2)

print(answer)