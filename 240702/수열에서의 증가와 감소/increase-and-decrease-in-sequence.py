n = int(input())
numbers = list(map(int, input().split()))
length = 1
max_length = 0
asc = True

for index, num in enumerate(numbers[:-1]):
    if asc and num <= numbers[index+1]:
        length += 1
    elif asc and num > numbers[index+1]:
        length = 2
        asc = False
    elif not asc and num <= numbers[index+1]:
        length = 2
        asc = True
    elif not asc and num > numbers[index+1]:
        length += 1
    
    max_length = max(length, max_length)

print(max_length)