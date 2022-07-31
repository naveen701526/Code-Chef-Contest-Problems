def answer_finder():
    n = int(input())
    n = [int(x) for x in str(n)]
    print(sum(n))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()