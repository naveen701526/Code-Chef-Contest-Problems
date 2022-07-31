def answer_finder():
    x,y = [int(x) for x in input().split()]
    if x<y:
        print('FIRST')
    elif y<x:
        print('SECOND')
    else:
        print('ANY')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()