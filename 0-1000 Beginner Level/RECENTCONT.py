def answer_finder():
    n = int(input())
    arr = [str(x) for x in input().split()]
    
    start38 = 0
    ltime108 = 0
    for a in arr:
        if a == 'START38':
            start38+=1
        if a == 'LTIME108':
            ltime108+=1
    print(start38, end=" ")
    print(ltime108)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()