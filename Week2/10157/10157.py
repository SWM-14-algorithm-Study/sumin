import sys
input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())

# 실제 행렬이랑 문제에서 제시하는 좌표의 인덱스가 다르니까 행, 열을 R개, C개로 둠
arr = [[0 for col in range(R)] for row in range(C)]


if K > C*R:
    print("0")
    exit()

# 위, 오른쪽, 아래, 왼쪽 순서로 방향 저장
dir = [(0,1), (1,0), (0,-1), (-1,0)]
# 현재 위치를 r,c에 저장
r,c = (0,0)
# 처음 값은 1 (첫번째 사람부터 저장)
arr[r][c] = 1
# i에 방향 인덱스 저장(순서대로 위, 오른쪽, 아래, 왼쪽)
i=0
# 2번부터 K번까지 사람들 배치
for j in range(2, K+1):
    # 다음 위치를 저장해서 방향을 바꿔야하는지 판단 -> 방향을 바꿔야한다면 if문에서 다음 위치 수정
    mover, movec = dir[i]
    next_r, next_c = (r+mover, c+movec)
    if next_r < 0 or next_c < 0 or next_r >= C or next_c >= R or arr[next_r][next_c] != 0:
        i = (i+1)%4
        mover, movec = dir[i]
        next_r, next_c = (r+mover, c+movec)
    r,c = (next_r, next_c)
    arr[r][c] = j
    
print("{0} {1}".format(r+1,c+1))
