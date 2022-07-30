def answer_finder():
    n,x, y = [int(x) for x in input().split()]
    if n >= (x+y*2):
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()