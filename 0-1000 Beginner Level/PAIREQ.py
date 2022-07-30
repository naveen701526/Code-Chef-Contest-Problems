def answer_finder():
    n = int(input())
    arr = [int(x) for x in input().split()]
    dis = {}
    for i in range(n):
        if dis.get(arr[i]):
            dis[arr[i]] += 1
        else:
            dis[arr[i]] = 1
    count = 0
    ans = 0
    for d in dis:
        if dis[d] > count:
            count = dis[d]
            ans = d
    val = dis[ans]
    print(n-val)


test_cases = int(input())

while test_cases:
    test_cases -= 1
    answer_finder()
