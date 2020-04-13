# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]

AB.sort()

ans = 0
cnt = 0
for a,b in AB:
    ans += a * min(b, M-cnt)
    cnt += b
    if cnt >= M:
        break

print(ans)