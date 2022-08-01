def answer_finder():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a_new = [0]*n
    a_new[0] = a[0]
    for i in range(1,n):
        a_new[i] = a[i] - a[i-1]
    
    # print(a_new)
    count = 0
    for i in range(n):
        if b[i]<=a_new[i]:
            count+=1
    print(count)

test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()