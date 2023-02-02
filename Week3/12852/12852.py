import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
Q = deque()
Q.append([N])
path = list()

while Q:
    # print(Q)
    arr = Q.popleft()

    tmp = arr[0]
    # print(arr)
    # print(tmp)
    # print(Q)
    if tmp == 1:
        path = arr
        break

    if tmp % 3 == 0:
        tmp_3 = tmp / 3
        Q.append([tmp_3]+arr)

    if tmp % 2 == 0:
        tmp_2 = tmp / 2
        Q.append([tmp_2]+arr)

    arr.insert(0, tmp-1)
    Q.append(arr)

print(len(path)-1)
path.reverse()
for i in path:
    print(int(i), end=" ")
