# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
KS = [list(map(int,input().split())) for _ in range(M)]
P = list(map(int,input().split()))

ans = 0

i = 0
while i < 2**N:
    bit = bin(i)[2:].zfill(N)
    check = True
    for j in range(M):
        swlist = KS[j][1:]
        cnt = 0
        for sw in swlist:
            if bit[sw-1] == "1":
                cnt += 1
        if cnt%2 != P[j]:
            check = False
            break
    if check:
        ans += 1
    i += 1

print(ans)