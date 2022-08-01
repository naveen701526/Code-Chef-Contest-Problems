def answer_finder():
    n,a,b = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    val1 = arr.count(a)
    pro1 = val1/n
    val2 = arr.count(b)
    pro2 = val2/n
    print(pro1*pro2)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()