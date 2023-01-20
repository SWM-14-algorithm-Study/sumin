import sys

# 카드의 개수 N
N = int(sys.stdin.readline())
# 카드 N개에 들어있는 정수가 공백(빈 칸)으로 구분되어 주어짐
card_list = [int(x) for x in sys.stdin.readline().split()]
max_count = 0

for i in range(N):
    if max_count >= N-i:
        # print("i : %d, N-i : %d, max_count : %d" % (i, N-i, max_count))
        break
    # 처음 뽑는 카드를 i번째 카드로
    selected_cards = [card_list[i]]
    # 뽑은 카드 리스트의 마지막 숫자가 전체 카드의 마지막 숫자와 같지 않다면
    while selected_cards[-1] != card_list[-1]:
        # 뽑은 카드 다음 카드부터 탐색
        start = card_list.index(selected_cards[-1])
        # 더이상 반복 안 해도 되는 경우 break (현재 선택한 카드(1) + 앞으로 남은 카드 개수 (len(card_list[start+1, N]))
        if len(card_list[start+1:N]) + 1 <= max_count:
            break
        for j in range(start+1, N):
            if card_list[j] > selected_cards[-1]:
                selected_cards.append(card_list[j])
        # print("%d번째 카드(%d)가 시작, %d개의 카드 선택됨"% (i, card_list[i], len(selected_cards)))
        if max_count < len(selected_cards) :
            max_count = len(selected_cards) 

print(max_count)
