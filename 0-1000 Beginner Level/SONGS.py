def answer_finder():
    n,x= [int(x) for x in input().split()]
    val = x*3
    print(n//val)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()