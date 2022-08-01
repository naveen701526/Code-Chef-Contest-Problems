def answer_finder():
    n,m,k=[int(x) for x in input().split()]
    if n<=m-k:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()