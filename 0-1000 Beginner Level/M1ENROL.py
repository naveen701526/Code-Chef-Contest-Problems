def answer_finder():
    x,y=[int(x) for x in input().split()]
    if x-y>0:
        print(0)
    else:
        print(abs(x-y))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()