def answer_finder():
    pa,pb,qa,qb = [int(x) for x in input().split()]
    val1 = max(pa,pb)
    val2 = max(qa,qb)
    if val1 > val2:
        print('Q')
    elif val2 > val1:
        print('P')
    else:
        print('TIE')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()