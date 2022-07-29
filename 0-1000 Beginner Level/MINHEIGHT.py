def answer_finder():
    x,h = [int(x) for x in input().split()]
    if x<h:
        print('NO')
    else:
        print('YES')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()