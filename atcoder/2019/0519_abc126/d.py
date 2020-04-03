import sys
input = sys.stdin.readline

N = int(input())
A = [[] for _ in range(N)] 
for i in range(N-1):
    u,v,w = map(int,input().split())
    A[u-1].append((v-1,w))
    A[v-1].append((u-1,w))

color = [-1]*N
color[0] = 0
stack = [0]

while stack:
    u = stack.pop()
    for v,w in A[u]:
        if color[v] != -1:
            continue
        color[v] = color[u]^(w&1)
        stack.append(v)

for c in color:
    print(c)