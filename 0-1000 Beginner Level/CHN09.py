

from collections import Counter


def answer_finder():
    string = input()
    dis = Counter(string)
    val1 = [x for x in dis.values()]
    temp = max(val1)
    
    print(len(string)-temp)
    # print(val2)


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()
