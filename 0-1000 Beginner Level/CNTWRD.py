def answer_finder():
    n, m = [int(x) for x in input().split()]
    ans = 0
    for i in range(m):
        ans+=n
    print(ans)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()