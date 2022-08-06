import math
import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')

def countInversions(arr,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                count+=1
    return count


def answer_finder():
    n,k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    inversions = countInversions(arr,n)
    answer = 0
    answer += inversions*k

    for i in range(n):
        rem_count = 0
        for j in range(n):
            if arr[i] > arr[j]:
                rem_count += 1
        answer += math.floor(k*(k-1)/2) * rem_count
    print(answer)

    
    

        
    
    

    

    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
