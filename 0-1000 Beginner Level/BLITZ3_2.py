def answer_finder():
    n,a,b = [int(x) for x in input().split()]
    val1 = 2*(180+n)
    val2 = a+b
    print(val1-val2)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()