n, m = map(int, input().split())
num_list = list(map(int, input().split()))
sum_result = {}

init = sum(num_list[:m])
sum_result[init] = 1

for i in range(m, n):
    init += num_list[i]
    init -= num_list[i-m]
    
    if init in sum_result:
        sum_result[init] += 1
    else:
        sum_result[init] = 1

sum_result = sorted(sum_result.items(), key=lambda x:x[0])

print(sum_result[0][0])
if sum_result[0][0] != 0:
    print(sum_result[0][1])