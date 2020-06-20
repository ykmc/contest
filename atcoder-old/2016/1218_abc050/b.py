# PyPy3 (2.4.0)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
T = list(map(int,input().split()))
M = int(input())
PX = [list(map(int,input().split())) for _ in range(M)]
 
total = sum(T)
 
Ans = []
for p,x in PX:
    Ans.append(total - T[p-1] + x)
 
for ans in Ans:
    print(ans)