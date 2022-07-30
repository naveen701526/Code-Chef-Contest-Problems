def answer_finder():
    n, k = [int(x) for x in input().split()]
    if k >n :
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()