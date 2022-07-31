def answer_finder():
    x = int(input())
    if x in [1,2,3,4]:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()