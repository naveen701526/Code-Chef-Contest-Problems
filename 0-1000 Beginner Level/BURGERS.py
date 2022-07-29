def answer_finder():
    a,b = [int(x) for x in input().split()]
    val = min(a,b)
    print(val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()