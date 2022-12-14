# Write here the code challenge solution
from collections import Counter
 
def firstRepeat(input):
    words = input.split(' ')
    dict = Counter(words)
    # print(dict)
    for word in words:
        if dict[word]>1:
            # print (word)
            return word
 
# Driver program
if __name__ == "__main__":
    input = 'ASAC is a department at LTUC. ASAC teaches programming in LTUC.'
    print(firstRepeat(input))