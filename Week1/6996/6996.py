# [입력] 테스트 케이스의 개수
N = int(input())
test_case = list() # 입력한 테스트케이스를 튜플로 리스트에 -> [(단어1, 단어2), (단어1, 단어2)]
test_res = list() # anagram -> 1, not anagram -> 0

for i in range(N):
    # [입력] 테스트 케이스 입력 - 한 줄에 두 단어씩
    a, b = input().split(' ')
    tup = (a,b)
    test_case.append(tup)
    # a, b를 알파벳 순으로 정렬해서 넣음
    sorted_tc_1 = list(sorted(a))
    sorted_tc_2 = list(sorted(b))
    # 길이부터 다르면 비교할 필요없이 not anagram
    if len(sorted_tc_1) != len(sorted_tc_2):
        test_res.append(0)
        continue
    # 비교 결과 다르면 not anagram 저장 후 종료, 안 걸러지고 다 같으면 anagram 저장
    flag = 0
    for j in range(0, len(a)):
        # 걸러졌으면 not anagram(0)이라고 저장
        if sorted_tc_1[j] != sorted_tc_2[j]:
            test_res.append(0)
            flag = 1
            break
    # 안 걸러졌으면 anagram(1)이라고 저장 
    if flag == 0:
        test_res.append(1)

idx = 0
for x,y in test_case:
    if test_res[idx] == 1: 
        print("%s & %s are anagrams." % (x,y))
    else:
        print("%s & %s are NOT anagrams." % (x,y))
    idx += 1
