def answer_finder():
    n = int(input())
    val = n*50
    ans = val - (0.7*val)
    ans = int(ans)
    print(ans)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()