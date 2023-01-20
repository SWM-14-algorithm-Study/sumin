import math

N = int(input())
cnt = 0
for B in range(1,501):
    for A in range(B, 501):
        if math.pow(A,2) == math.pow(B,2) + N:
            cnt+=1
print(cnt)
