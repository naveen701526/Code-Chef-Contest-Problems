def answer_finder():
    n,m,k=[int(x) for x in input().split()]
    if n/m > k:
        print('No')
    else:
        print('Yes')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()