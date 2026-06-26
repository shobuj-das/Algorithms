def word_count(sentence_list):
    counter = 0
    for sentence in sentence_list:
        temp = sentence.strip().split(" ")
        # print(temp)
        for x in temp:
            if x!="":
               counter += 1
    return counter

if __name__=="__main__":
    n = int(input())
    sentence_list = []
    for i in range(n):
        sentence  = input()
        sentence_list.append(sentence)
        
    print(word_count(sentence_list))