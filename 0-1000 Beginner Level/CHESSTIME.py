def answer_finder():
    t = [int(x) for x in input().split()]
    t *= 60
    print(t//20)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()