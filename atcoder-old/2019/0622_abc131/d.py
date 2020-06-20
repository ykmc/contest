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
AB = [tuple(map(int,input().split())) for _ in range(N)]

AB.sort(key=lambda x:x[1]) 

ans = "Yes"
total = 0
for a,b in AB:
    total += a
    if total > b:
        ans = "No"
        break

print(ans)