import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

# tree 생성 (인덱스가 1번부터니까 N+1) - 점 하나에 연결될 수 있는 게 많으니까 요소를 리스트로 생성
tree = [list() for i in range(N+1)]

# 트리(그래프) 점 입력받으면서 생성(무방향이니까 x,y 둘 다 연결)
for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

parent = [0 for i in range(N+1)]
visited = [False] * (N+1)

def DFS(n):
    visited[n] = True
    for i in tree[n]:
        if not visited[i]:
            DFS(i)
            parent[i] = n

DFS(1)

for i in range(2,N+1):
    print(parent[i])
