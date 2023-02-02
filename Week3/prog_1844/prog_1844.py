from collections import deque

def solution(maps):
    r = len(maps)
    c = len(maps[0])
    visited = [[0]*c for i in range(r)]
    visited[0][0]=True
    # 동서남북 이동 방향
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    answer = 1
    Q = deque()
    Q.append((0,0,answer))
    while Q:
        # 이전 좌표 i, j에 저장
        i, j, answer = Q.popleft()
        # cur_dir에 dir에서 뽑은 현재 방향 튜플 저장됨
        for cur_dir in dir:
            # x축 이동, y축 이동 후 다음 좌표 x, y에 저장
            x, y = i + cur_dir[0], j + cur_dir[1]
            # 게임 맵 안에 들어있는 경우
            if 0 <= x < r and 0 <= y < c:
                if visited[x][y] ==True:
                    continue
                if maps[x][y] == 1:
                    # 끝까지 도달했다면
                    if x == r-1 and y == c-1 :
                        return answer+1
                    else:
                        visited[x][y] = True
                        Q.append((x,y,answer+1))
    # 상대에게 도착할 수 없다면
    return -1
    
