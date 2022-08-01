def answer_finder():
    c,x,y = [int(x) for x in input().split()]
    val = c -x
    if val == 0:
        print(0)
    else:
        print(y*val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()