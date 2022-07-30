# cook your dish here
a = [int(x) for x in input().split()]
val = 0

for i in range(len(a)):
    if a[i] >= 10:
        val+=1

print(val)