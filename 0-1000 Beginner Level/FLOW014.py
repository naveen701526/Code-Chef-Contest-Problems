import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    hardness, carbon_content, tensile_strength = [float(x) for x in input().split()]
    condition_1 = hardness > 50
    condition_2 = carbon_content < 0.7
    condition_3 = tensile_strength > 5600
    if condition_1 and condition_2 and condition_3:
        print(10)
    elif condition_1 and condition_2:
        print(9)
    elif condition_2 and condition_3:
        print(8)
    elif condition_1 and condition_3:
        print(7)
    elif condition_1 or condition_2 or condition_3:
        print(6)
    else:
        print(5)
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
