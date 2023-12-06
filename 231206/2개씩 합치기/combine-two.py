import heapq

n = int(input())
arr = list(map(int, input().split()))
heapq.heapify(arr)
answer = 0

while len(arr) > 1:
    num1 = heapq.heappop(arr)
    num2 = heapq.heappop(arr)

    answer += num1 + num2
    heapq.heappush(arr, num1+num2)

print(answer)