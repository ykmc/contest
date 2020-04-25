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
A = map(int,input().split())

# 6で割った余りが 1 or 3ならok
# 6で割って余りがiの時にむしる必要がある枚数
r = [3,0,1,0,1,2]

ans = 0
for a in A:
    ans += r[a%6]

print(ans)