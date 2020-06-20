import sys
input = sys.stdin.readline

N,L = map(int,input().split())
S = list()
for i in range(N):
    s = input().rstrip()
    S.append(s)

S.sort()

print("".join(S))