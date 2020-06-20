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
A = [input().rstrip() for _ in range(N)]
B = [input().rstrip() for _ in range(M)]

for dh in range(N-M+1):
    for dw in range(N-M+1):
        flg = True
        for h in range(M):
            for w in range(M):
                if B[h][w] != A[h+dh][w+dw]:
                    flg = False
                    break
        if flg:
            print("Yes")
            sys.exit()

print("No")
