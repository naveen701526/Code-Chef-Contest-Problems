def solve():
    l = []
    for _ in range(int(input())):
        l.append(list(map(int, input().split())))

    ans = l[-1]
    for i in range(len(l)-2, -1, -1):
        for j in range(i+1):

            ans[j] = max(ans[j], ans[j+1]) + l[i][j]
    print(ans[0])


t = int(input())
while t:
    t -= 1
    solve()
