def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    print(x*y*z)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()