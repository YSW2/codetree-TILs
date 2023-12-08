import itertools

n = int(input())
arr = list(map(int, input().split()))

for answer in list(itertools.combinations(arr, 6)):
    for num in answer:
        print(num, end=" ")
    print()