def answer_finder():
    a,b,c = [int(x) for x in input().split()]
    if a > (b+c):
        print('YES')
    elif b > (a+c):
        print('YES')
    elif c > (a+b):
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()