def answer_finder():
    x,y = [int(x) for x in input().split()]
    val = int(y/2)
    print(val+ (x-y))


answer_finder()