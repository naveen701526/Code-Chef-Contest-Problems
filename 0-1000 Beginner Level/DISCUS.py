def answer_finder():
    a,b,c = [int(x) for x in input().split()]
    print(max(a,b,c))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()