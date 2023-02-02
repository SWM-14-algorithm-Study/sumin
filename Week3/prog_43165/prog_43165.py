from collections import deque

def solution(numbers, target):
    answer = 0  
    test_target = list()
    test_target.append(0)
    
    # numbers에 있는 값을 더하거나 빼서 구할 수 있는 모든 숫자를 test_target 리스트에 저장
    for i in numbers:
        tmp = list()  
        for j in test_target:
            tmp.append(j + i)
            tmp.append(j - i)
        test_target = tmp  
        
    # 모든 계산된 값 중 target과 같은 값의 개수 세기
    for i in test_target:
        if i == target:  
            answer += 1
    
    return answer
