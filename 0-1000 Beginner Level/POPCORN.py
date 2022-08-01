def answer_finder():
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    print(max(sum(a),sum(b),sum(c)))

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()