def answer_finder():
    x,y = [int(x) for x in input().split()]
    if y in range(x,x+201):
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()