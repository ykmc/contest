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
A = [int(input()) for _ in range(N)]

from collections import Counter
C = Counter(A).most_common()

ans = 0
for k,v in C:
    ans += v-1

print(ans)