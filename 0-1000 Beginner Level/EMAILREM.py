def answer_finder():
    n,u = [int(x) for x in input().split()]
    print(n-u)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()