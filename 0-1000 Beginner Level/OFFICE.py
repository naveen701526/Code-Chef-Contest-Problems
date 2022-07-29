def solve():
    x, y = [int(x) for x in input().split()]
    print(x*4 + y)



test_cases = int(input())

while test_cases:
    test_cases -= 1
    solve()