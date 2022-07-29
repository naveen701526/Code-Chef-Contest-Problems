import math


def solve():
    n = int(input())
    frequency = [0]*(n+1)
    input_array = [int(x) for x in input().split()]
    for input_element in input_array:
        frequency[input_element] += 1

    frequency.sort(reverse=True)

    high1 = math.floor((frequency[0] + 1) / 2)
    high2 = frequency[1]

    print(max(high1, high2))


test_cases = int(input())

while test_cases:
    test_cases -= 1
    solve()


# Approach
# find the number of occurences of each element in array
# sort based on highest number of occurences to lowest
# take highest and second highest number of frequency
# reduce the highest my half
# compare the highest and second highest ( now new highest is less than previous one)
