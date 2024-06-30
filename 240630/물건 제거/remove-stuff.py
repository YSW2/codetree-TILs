machine_n = int(input())
machines = list(map(int, input().split()))

box_n = int(input())
boxes = list(map(int, input().split()))

terminated = [0 for x in range(box_n)]
answer = 0

machines.sort(reverse=True)
boxes.sort(reverse=True)

if max(machines) < max(boxes):
    print(-1)

else:
    while sum(terminated) < box_n:
        for machine in machines:
            for index, box in enumerate(boxes):
                if box <= machine and terminated[index] == 0:
                    terminated[index] = 1
                    break
        answer += 1

    print(answer)