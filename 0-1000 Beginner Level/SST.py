def answer_finder():
    a,b = [int(x) for x in input().split()]
    val1 = 10*a
    val2 = 5*b
    if val1 == val2:
        print('ANY')
    elif val1 > val2:
        print('FIRST')
    else:
        print('SECOND')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()