import sys
input = sys.stdin.readline

N, M = map(int, input().split())
yes = True

for cnt in range(M):
    #  첫 번째 줄에는 더미에 쌓인 교과서의 수 i가 주어짐
    i = int(input())
    # 두번째 줄에는 i개의 정수가 공백으로 나뉘어 입력됨
    k = list(map(int, input().split()))
    if yes == True:
        # 아래에 있는 책의 번호가 더 작다면 False, break
        for j in range(i-1):
            if k[j] < k[j+1]:
                yes = False
                break

if yes == True:
    print("Yes")
else:
    print("No")
