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

ans = 0
for i in range(1,N):
    l,r = set(),set()
    for s in S[:i]:
        l.add(s)
    for s in S[i:]:
        r.add(s)
    ans = max(ans,len(l&r))

print(ans)