def answer_finder():
    n, k = [int(x) for x in input().split()]
    if k==1:
        if n%4 ==0:
            print('On')
        else:
            print('Ambiguous')
    else:
        if n%4==0:
            print('Off')
        else:
            print('On')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()