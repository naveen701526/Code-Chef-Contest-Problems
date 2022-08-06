
    
    


from collections import Counter
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n, w, w_r = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr_new = Counter(arr)
    count = w_r
    for a_new in arr_new.keys():

        if arr_new[a_new] > 1 and arr_new[a_new] % 2 == 0:
            count += int(a_new) * arr_new[a_new]
    if count >= w:
        print('YES')
    else:
        print('NO')


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
