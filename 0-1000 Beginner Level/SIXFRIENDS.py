def answer_finder():
    x,y = [int(x) for x in input().split()]
    val1 = 3*x
    val2 = y*2
    print(min(val1,val2))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()