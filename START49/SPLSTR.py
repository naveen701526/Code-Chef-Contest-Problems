

def solve():
    n, k = [int(x) for x in input().split()]
    s = input()

    ones = 0
    zeroes = 0

    for c in s:
        if c == '0':
            zeroes += 1
        else:
            ones += 1

    num = min(ones, zeroes)
    zeroes -= num
    ones -= num

    rem = max(zeroes, ones)
    ans = rem//k
    print(ans if (rem % k == 0) else ans+1)


test_cases = int(input())

while test_cases:
    test_cases -= 1
    solve()
