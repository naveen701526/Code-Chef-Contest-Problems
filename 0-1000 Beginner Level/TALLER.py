def answer_finder():
    a,b = [int(x) for x in input().split()]
    print('A' if a>b else 'B')

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()