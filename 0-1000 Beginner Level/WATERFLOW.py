def answer_finder():
    w,x,y,z = [int(x) for x in input().split()]
    val = z*y + w
    if  val > x:
        print('overFlow')
    elif val == x:
        print('filled')
    else:
        print('Unfilled')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()