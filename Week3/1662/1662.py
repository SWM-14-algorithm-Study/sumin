import sys
input = sys.stdin.readline

S = input()
# 압축 푼 문자열 저장하는 리스트 stack
stack = list()

idx = -1
for i in S:
    idx += 1
    # 반복 횟수 (따로 지정되지 않았다면 1번 반복)
    repeat_num = 1
    if i == "(":
        stack.append("(")
    elif i == ")":
        string = 0
        while True:
            str = stack.pop()
            # 여는 괄호 앞에 반복 횟수가 나오니까 그때까지 반복
            if str == "(":
                repeat_num = int(stack.pop())
                break
            string += str  
        stack.append(repeat_num * string)
    # i가 반복횟수인 경우 ( 여는 괄호 바로 앞에 나온 숫자인 경우 )
    elif i.isdigit() and S[idx+1] == "(":
        repeat_num = int(i)
        stack.append(repeat_num)
    else:
        stack.append(repeat_num)

stack.pop()

sum_ = 0
for i in stack:
    sum_ += i
print(sum_)
