def answer_finder():
    n,x = [int(x) for x in input().split()]
    if n<=x and x%n==0:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()


