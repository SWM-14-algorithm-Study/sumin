# 1. 입력받은 단어를 전부 소문자로 변환 후 리스트에 넣음
word = input()
lower_word = list(word.lower())

# 2. 알파벳 개수만큼 count_list를 만들어 0으로 모두 초기화 후
#    문자열을 전부 돌면서 count_list의 인덱스에 아스키코드값을 넣고 추가
# 파이썬에서는 char -> int로 변환할 때 ord(char), chr(int)로 해야함
count_list = [0 for i in range(26)]
max_ = 0
for char in lower_word:
    idx = ord(char)-ord('a')
    count_list[idx] += 1
    if count_list[idx] > max_:
        most_used_idx = char
        max_ = count_list[idx]

# 리스트 최대, 최솟값 구하기
max_num = max(count_list)
min_num = min(count_list)
# 알파벳 하나만 입력한 경우, 그 알파벳 대문자 그대로 출력
if max_num==1 and min_num==0:
    print(word.upper())
# 가장 많이 쓰인 알파벳이 하나만 있는 경우, 그 알파벳 대문자 그대로 출력
elif count_list.count(max_num) == 1:
    print(most_used_idx.upper())
# 나머지 경우는 ? 출력
else:
    print("?")
