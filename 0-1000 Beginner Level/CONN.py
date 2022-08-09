import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')

def solution(n,dp):
    if n == 0 or n == 2 or n==7 or n%2==0 or n%7==0:
        dp[n] = 'YES'
        return 'YES'
    if n < 0:
        dp[n] = 'NO'
        return 'NO'
    if dp.get(n):
        return dp[n]
    else:
        dp[n] = solution(n-2,dp) or solution(n-7,dp)
        return dp[n]

def answer_finder():
    n = int(input())
    dp = {}
    res = solution(n,dp)
    print(res)
    
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()

