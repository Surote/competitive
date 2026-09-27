t = int(input())
for i in range(t):
    c = int(input())
    x,y,z = map(int,input().split())
    print(c-min(x,y,z))