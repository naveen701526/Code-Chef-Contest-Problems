def answer_finder():
    x,y,z=[int(x) for x in input().split()]
    val = (z-y)//x
    print(val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()