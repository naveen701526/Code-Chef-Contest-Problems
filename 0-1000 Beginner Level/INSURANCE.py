def solve():
    x, y = [int(x) for x in input().split()]
    print(min(x, y))


test_cases = int(input())

while test_cases:
    test_cases -= 1
    solve()
