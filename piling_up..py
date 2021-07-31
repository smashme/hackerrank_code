from collections import deque
testcases = int(input())
for x in range(testcases):
    n = int(input())
    row = deque(map(lambda x: int(x), input().split(' ')))
    stack = None
    isStackable= True
    while isStackable and len(row) > 0:
        if row[0] > row[-1]:
            value = row.popleft()
        else:
            value = row.pop()
            if stack is None or stack >= value:
                stack = value
            else:
                isStackable = False
    if isStackable:
        print('Yes')
    else:
        print('No')

