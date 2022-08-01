def answer_finder():
    a,b = [int(x) for x in input().split()]
    c,d = [int(x) for x in input().split()]
    if c-a>=0 and d-b>=0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()