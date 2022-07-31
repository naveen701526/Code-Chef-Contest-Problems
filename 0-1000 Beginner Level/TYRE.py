def answer_finder():
    b,c = [int(x) for x in input().split()]
    print(b*2+c*4)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()