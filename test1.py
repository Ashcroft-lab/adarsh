from collections import deque
for _ in range(int(input())):
    _, queue = input(), deque(map(int, input().split()))

    for i in reversed(sorted(queue)):
        if queue[-1] == i :
            queue.pop()

        elif queue[0] == i :
            queue.popleft()
        else:
            print("No")
            break
    else: print('Yes')