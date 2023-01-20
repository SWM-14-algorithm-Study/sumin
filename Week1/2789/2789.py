word = list(input())
cambridge = list("CAMBRIDGE")

new_word = [i for i in word if i not in cambridge]

print(''.join(new_word))
