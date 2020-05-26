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
A = list(map(int,input().split()))

ans = set()

for a in A:
    while True:
        if a%2 == 0:
            a //= 2
        else:
            ans.add(a)
            break

print(len(ans))
