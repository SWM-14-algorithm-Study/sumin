from collections import Counter
# 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 most_common() 메소드 (dict 형태)
import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for i in range(N)]
numbers.sort()

# 산술평균
avg = round(sum(numbers) / N)
# 중앙값
median = numbers[int(N/2)]
# 최빈값
freq = Counter(numbers).most_common()
# 최빈값 2개 이상 
# (freq[i][j] - i: 가장 많이 나온 원소, j: 해당 원소의 개수)
if len(freq) > 1 and freq[0][1] == freq[1][1]:
    res_freq = freq[1][0]
else:
    res_freq = freq[0][0]

# 범위
range = abs(numbers[-1] - numbers[0])

print(avg)
print(median)
print(res_freq)
print(range)
