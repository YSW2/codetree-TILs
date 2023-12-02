n = int(input())
arr = list(input())
string = ['a', 'b', 'c']
idx = 0
start = 0
str_idx = 0
answer = 0

while idx < len(arr):
    if arr[idx] != string[(str_idx+1)%3]:
        idx += 1
    else:
        answer += (idx-start) ** 2
        start = idx
        str_idx += 1

if answer:
    print(answer)
else:
    print(-1)