def answer_finder():
    x = int(input())
    if x + 3 <= 10:
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()