def answer_finder():
    t1,t2,r1,r2 = [int(x) for x in input().split()]
    if pow(t1,2)/pow(r1,3) == pow(t2,2)/pow(r2,3):
        print('YES')
    else:
        print('NO')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()