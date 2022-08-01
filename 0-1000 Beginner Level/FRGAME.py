def answer_finder():
    a,b,c,d = [int(x) for x in input().split()]
    if a >= b:
        b+=c
    else:
        a+=c
    
    if a >= b:
        b+=d
    else:
        a+=d
    
    if a>=b:
        print('N')
    else:
        print('S')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()