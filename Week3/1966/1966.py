import sys
from collections import deque
input = sys.stdin.readline

ans = list()
tc = int(input())

for i in range(tc):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    # 출력되는 숫자가 있을 때마다 1씩 증가 -> M이 몇 번째로 출력되는지 찾기
    cnt = 0
    while True:
        # maxi에 현재 Q의 최댓값 저장
        maxi = max(Q)
        # tmp에 큐 가장 앞 숫자 하나 뽑아서 저장
        tmp = Q.popleft()
        # 숫자 하나 뽑았으니까 찾아야하는 수 (M번째)의 인덱스도 하나 감소
        M -= 1
        # 만약 뒤에 더 큰 수가 없다면 (뽑은 수가 가장 큰 수라면) 그대로 출력해버리기 (뒤에 다시 안 붙이)
        if tmp == maxi:
            cnt += 1
            # M 이 -1이면 찾고자하던 숫자가 tmp
            if M == -1:
                ans.append(cnt)
                break
        # 뽑은 수보다 더 큰 수가 뒤에 있으면 큐의 가장 뒤에 tmp 넣기
        else:
            Q.append(tmp)
            # 만약 뽑은 수(tmp)가 M이었다면 M을 tmp의 위치로 변경
            if M == -1:
                M = len(Q) - 1

for i in ans:
    print(i)
