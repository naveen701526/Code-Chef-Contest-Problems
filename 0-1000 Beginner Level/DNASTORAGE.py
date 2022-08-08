import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    n = int(input())
    s = input()
    count = ''
    count1 = ''
    for i in range(n):
        if i % 2 == 0:
            count += s[i]
        else:
            count1 += s[i]
    for i in range(len(count)):
        temp = count[i] + count1[i]
        if temp == '00':
            print('A',end='')
        elif temp == '01':
            print('T',end='')
        elif temp == '10':
            print('C',end='')
        else:
            print('G',end='')
    print()
        
    


test_cases = int(input())
while test_cases:
    test_cases -= 1
    answer_finder()
