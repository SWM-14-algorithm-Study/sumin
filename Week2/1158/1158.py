# [입력]
N, K = map(int, input().split())
# 1 ~ N번까지의 사람 리스트 생성 (처음에 앉아있는 순서대로)
people_list = [i for i in range(1, N+1)]
result = list()

idx = 0
for i in range(N):
    # 더했을 때 idx값이 people_list보다 더 큰 수가 나오지 않게 % 해줌
    idx = (idx + K - 1) % len(people_list)
    # idx 인덱스인 사람 people_list에서는 없애고, result에 추가
    result.append(people_list.pop(idx))
    # print(people_list)

print("<", end="")
for i in result:
    # 마지막 원소라면 괄호 닫고 끝내기
    if i==result[-1]:
        print(i, end=">")
    # 마지막 원소 아니면 출력하고 뒤에 쉼표
    else:
        print(i, end=", ")
