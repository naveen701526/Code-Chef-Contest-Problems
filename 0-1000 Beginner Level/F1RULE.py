def answer_finder():
    x,y = [int(x) for x in input().split()]
    x *= 1.07
    if y <= x:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()