def answer_finder():
    x, n = [int(x) for x in input().split()]
    num = x//10
    print(num*n)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()