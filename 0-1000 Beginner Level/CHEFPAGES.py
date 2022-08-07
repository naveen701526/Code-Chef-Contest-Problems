import sys
sys.stdout = open('./output.txt', 'w')
sys.stdin = open('./input.txt', 'r')


def answer_finder():
    a,b = [int(x) for x in input().split()]
    if a == 0 and b == 1:
        print('''https://www.codechef.com/practice''')
    elif a == 0 and b == 0:
        print('''https://www.codechef.com/practice''')
    elif a == 1 and b == 0:
        print('''https://www.codechef.com/contests''')
    else:
        print('''https://discuss.codechef.com''')
    


answer_finder()