def answer_finder():
    a, b = [int(x) for x in input().split()]
    gcd_value = gcd(a, b)
    lcm_value = lcm(a, b)
    print(gcd_value, ' ', lcm_value)


def gcd(a, b):
    temp = min(a, b)
    ans = 1
    for i in range(2, temp+1):
        if a % i == 0 and b % i == 0:
            ans = i

    return ans


def lcm(a, b):
    temp = a*b
    ans = max(a, b)
    for i in range(ans+1, temp+1):
        if i % a == 0 and i % b == 0:
            ans = i
            break
    return ans


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()
