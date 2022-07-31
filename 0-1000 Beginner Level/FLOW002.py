def answer_finder():
    a,b = [int(x) for x in input().split()]
    print(a%b)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()