import sys
input = sys.stdin.readline

N,K = map(int,input().split())
D = set(input().split())

for i in range(N,N*10+1):
    if not D & set(str(i)):
        break
 
print(i)