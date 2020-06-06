# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def F(a,b):
    return max(len(str(a)), len(str(b)))

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())

ds = set()
dl = list()
for i in range(1,10**5+1):
    if N%i == 0:
        ds.add(i)
        dl.append(i)
for d in dl:
    ds.add(N//d)
D = sorted(list(ds))

ans = 100
for d in D:
    ans = min(ans,F(d,N//d))

print(ans)