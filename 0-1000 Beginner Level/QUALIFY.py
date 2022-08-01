def answer_finder():
    x,a,b = [int(x) for x in input().split()]
    a1 = 1*a
    b1 = 2*b
    if x <= a1+b1:
        print('QUALIFY')
    else:
        print('NOTQUALIFY')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()