N, M = map(int, input().split())
card_list = list(map(int, input().split()))

res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            is_max = card_list[i] + card_list[j] + card_list[k]
            if is_max > M:
                continue
            elif is_max > res:
                res = is_max
print(res)
