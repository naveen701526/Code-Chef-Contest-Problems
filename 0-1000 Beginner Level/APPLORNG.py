def answer_finder():
    x = int(input())
    a, o = [int(x) for x in input().split()]
    if x >= a + o:
        print('YES')
    else:
        print('NO')

answer_finder()