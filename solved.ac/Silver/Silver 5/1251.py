# 단어 나누기

word = str(input())

best_word = None

for i in range(1,len(word)):
    for j in range(i+1, len(word)):
        w1 = word[0:i][::-1]
        w2 = word[i:j][::-1]
        w3 = word[j:len(word)][::-1]

        n_word = w1+w2+w3
        
        if best_word == None:
            best_word = n_word

        elif n_word < best_word:
            best_word = n_word

print(best_word)