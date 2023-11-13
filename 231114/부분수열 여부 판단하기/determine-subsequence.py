n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))

j = 0
for i in range(n):
    if arr_n[i] == arr_m[j]:
        j += 1
    if j == m:
        break

if j == m:
    print("Yes")

else:
    print("No")