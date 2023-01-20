# return 1 or 0
def cont(word):
    # 길이가 2보다 짧으면 검사할 필요없이 그룹단어(1)
    if len(word) < 2:
        return 1
    for i in range(len(word)):
        # 인덱스(i)가 0,1인 경우는 같은지 다른지 체크할 필요없으니까 그 이후부터 체크
        if i>1:
            for j in range(0,i-1):
                # j가 i 전전 알파벳과 같을 때, j~i가 모두 연속된 알파벳이라면 그 뒤도 체크, ex. nnaaaaa
                # 만약 중간에 다른 알파벳이 있다면 (연속되지 않았다면) 그룹단어 아님(0) ex. nnaxa
                if word[i] == word[j]:
                    for k in range(j,i):
                        if word[k] != word[j]:
                            return 0
    return 1

N = int(input())
wordlist=list()
for i in range(N):
    wordlist.append(input())

cnt = 0 #init
for word in wordlist:
    cnt += cont(word)
print(cnt)
