# [입력]
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

not_heard = set(input().strip() for i in range(N))
not_seen = set(input().strip() for i in range(M))
both = sorted(not_heard & not_seen)

print(len(both))

for i in both:
    print(i)
