import sys
input = sys.stdin.readline
# 조합 이용
from itertools import combinations

N, S = map(int, input().split())
num_list = [int(x) for x in input().split()]

cnt = 0

for i in range(1,N+1):
    # 부분집합의 원소의 개수가 1개 ~ N개일 때까지 반복
    # num_list에서 i개의 원소를 가지는 조합
    comb = combinations(num_list, i)
    for j in list(comb):
        if sum(j) == S:
            cnt += 1

print(cnt)
