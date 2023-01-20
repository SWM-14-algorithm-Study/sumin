def count_LOVE(name):
    cnt_L = 0
    cnt_O = 0
    cnt_V = 0
    cnt_E = 0

    for char in name:
        if char == 'L':
            cnt_L += 1
        elif char == 'O':
            cnt_O += 1
        elif char == 'V':
            cnt_V += 1
        elif char == 'E':
            cnt_E += 1

    return cnt_L, cnt_O, cnt_V, cnt_E

# 1. 연두의 영어 이름 입력받기, 계산
name_Y = list(input())

YL,YO, YV, YE = count_LOVE(name_Y)

# 2. 팀 이름 개수 입력받고, 계산
name_count = int(input())
res_list = list()
name_list = list()
most = 0

for i in range(name_count):
    team = list(input())
    name_list.append(team) # 팀명 입력 순서대로 리스트에 저장
    TL, TO, TV, TE = count_LOVE(team)
    L = TL + YL
    O = TO + YO
    V = TV + YV
    E = TE + YE
    res = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    res_list.append(res) # 계산 결과 res_list 리스트에 저장
    if (res >= most):
        idx = i
        most = res

# 1. 이름을 하나만 입력했을 때는 그 팀명 출력
if name_count==1:
    print(''.join(team))

# 2. 여러 이름 중 가장 큰 수가 1개일 때는 그 팀명 출력
elif res_list.count(most) == 1:
    print(''.join(name_list[idx]))

# 3. 가장 큰 수가 여러 개일 때는 그 중 알파벳순으로 가장 앞순서인 팀명 출력
else:
    idx_list = list()
    idx_name = list()
    for i in range(name_count):
        if most == res_list[i]:
            idx_name.append(name_list[i])
            
    idx_name = sorted(idx_name)
    print(''.join(idx_name[0]))
