def answer_finder():
    k, x = [int(x) for x in input().split()]
    k = k*7
    print(k-x)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()