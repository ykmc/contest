import sys
input = sys.stdin.readline

N,K = map(int,input().split())
S = input().rstrip()

sl = list(S)
sl[K-1] = sl[K-1].lower()
print("".join(sl))