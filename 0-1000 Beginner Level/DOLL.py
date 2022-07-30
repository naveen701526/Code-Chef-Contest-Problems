def answer_finder():
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    count = 0
    for a in arr:
        if a > k:
            count+=1
    print(count)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()