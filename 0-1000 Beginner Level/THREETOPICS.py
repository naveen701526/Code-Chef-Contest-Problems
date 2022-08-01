def answer_finder():
    a,b,c,x = [int(x) for x in input().split()]
    if x in [a,b,c]:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()