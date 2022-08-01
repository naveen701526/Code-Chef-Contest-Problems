import math


def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    val1 = x*y
    val2 = math.ceil(x/3) if x>3 else 0
    if val2 == 0:
        val2=0
    else:
        val2-=1
    val3 = val2*z
    print(val1+val3)



test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()