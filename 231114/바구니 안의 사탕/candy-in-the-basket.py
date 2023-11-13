n, k = map(int, input().split())
arr = [0 for x in range(1000001)]
candy_num = 0
max_basket = 0
answer = 0

for i in range(n):
    candy, basket = map(int, input().split())
    arr[basket] += candy
    max_basket = max(basket, max_basket)

candy_num = sum(arr[:k*2])

j = 0
for i in range(k*2+1, max_basket-k):
    answer = max(answer, candy_num)
    candy_num += arr[i]
    candy_num -= arr[j]
    j += 1

print(answer)