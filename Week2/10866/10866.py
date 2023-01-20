from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
command_q= deque()
cmd_list = list()
for i in range(N):
    cmd_list.append(input())

for cmd in cmd_list:
    cmd = list(cmd.split())
    if cmd[0] == "push_front":
        command_q.appendleft(cmd[1])

    elif cmd[0] == "push_back":
        command_q.append(cmd[1])

    elif cmd[0] == "pop_front":
        if command_q:
            print(command_q.popleft())
        else:
            print(-1)

    elif cmd[0] == "pop_back":
        if command_q:
            print(command_q.pop())
        else:
            print(-1)
    
    elif cmd[0] == "size":
        print(len(command_q))

    elif cmd[0] == "empty":
        if command_q:
            print(0)
        else:
            print(1)

    elif cmd[0] == "front":
        if command_q:
            print(command_q[0])
        else:
            print(-1)
    
    elif cmd[0] == "back":
        if command_q:
            print(command_q[-1])
        else:
            print(-1)

