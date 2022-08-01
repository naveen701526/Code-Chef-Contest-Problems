def answer_finder():
    n = int(input())
    val = max(0.1*n, 100)
    print(val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()