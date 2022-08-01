def answer_finder():
    x,y,z = [int(x) for x in input().split()]
    if z >= x+y:
        print(2)
    elif z >= x:
        print(1)
    else:
        print(0)
test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()