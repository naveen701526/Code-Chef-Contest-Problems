def answer_finder():
    x, y = [int(x) for x in input().split()]
    if x -y >= 0:
        print(x-y)
    else:
        print(0)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()