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

lenN = len(str(N))

Ans = 0
for i in range(lenN):
    d = 10**(i+1)
    q = N//d
    r = N%d
    # ループ分
    Ans += (10**i)*q
    # 余り分
    if r >= 2*(10**i):
        Ans += 10**i
    elif r >= (10**i):
        Ans += r-10**i+1

print(Ans)
