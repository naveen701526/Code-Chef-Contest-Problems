def answer_finder():
    x,y, z = [int(x) for x in input().split()]
    if z%x==0 and z%y==0:
        print('ANY')
    elif z % x == 0:
        print('CHICKEN')
    elif z%y == 0:
        print('DUCK')
    else:
        print('NONE')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()