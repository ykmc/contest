# Python3 (3.4.3)
import sys
input = sys.stdin.readline
from collections import Counter

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def is_ok(cntS, cntR, K):
    return sum((cntS-cntR).values()) <= K

def f(S, cntS, cntR, K):
    if len(S)==0:
        return ""
    cand = sorted(x for x,n in cntR.items() if n)
    for x in cand:
        cntS[S[0]] -= 1
        cntR[x] -= 1
        nextK = K if S[0]==x else K-1
        if is_ok(cntS,cntR,nextK):
            return x + f(S[1:],cntS,cntR,nextK)
        cntS[S[0]] += 1
        cntR[x] += 1


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K = map(int,input().split())
S = list(input().rstrip())

ans = f(S,Counter(S),Counter(S),K)
print(ans)