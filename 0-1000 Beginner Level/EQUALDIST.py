def answer_finder():
    a,b = [int(x) for x in input().split()]
    if (a+b)%2==0:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()