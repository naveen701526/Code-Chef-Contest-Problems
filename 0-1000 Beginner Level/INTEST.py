n, k = [int(x) for x in input().split()]
count=0
for _ in range(n):
    val = int(input())
    if val%k == 0:
        count+=1
print(count)