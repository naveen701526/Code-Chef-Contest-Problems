def answer_finder():
    x,y = [int(x) for x in input().split()]
    if x*10 < y:
        print('Disposable')
    else:
        print('Cloth')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()