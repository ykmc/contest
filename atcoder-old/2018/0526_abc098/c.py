# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
S = input().rstrip()

# l[i] : i番目からみて, 左側にいる W の人数
# r[i] : i番目からみて, 右側にいる E の人数
l = [0]*N
r = [0]*N

cnt = 0
for i in range(N-1):
    if S[i]=="W":
        cnt += 1
    l[i+1] = cnt
cnt = 0
for i in range(N-1):
    if S[N-1-i]=="E":
        cnt += 1
    r[N-1-i-1] = cnt

ans = N
for i in range(N):
    ans = min(ans, l[i]+r[i])

print(ans)