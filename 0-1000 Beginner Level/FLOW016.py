def answer_finder():
    a, b = [int(x) for x in input().split()]
    gcd_value = gcd(a, b)
    lcm_value = lcm(a, b, gcd_value)
    print(gcd_value, ' ', lcm_value)


def gcd(a, b):
    if a%b== 0:
        return b
    return gcd(b, a%b)


def lcm(a, b, gcd_value):
    return (a*b)//gcd_value


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()
