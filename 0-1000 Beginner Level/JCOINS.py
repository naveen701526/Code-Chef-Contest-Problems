def answer_finder():
    x,y = [int(x) for x in input().split()]
    print(x*10+5*y)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()