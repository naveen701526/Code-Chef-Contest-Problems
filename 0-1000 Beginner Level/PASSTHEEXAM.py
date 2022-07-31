def answer_finder():
    a,b,c = [int(x) for x in input().split()]
    if a+b+c >= 100:
        if a>=10 and b>=10 and c>=10:
            print('PASS')
        else:
            print('FAIL')
    else:
        print('FAIL')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()