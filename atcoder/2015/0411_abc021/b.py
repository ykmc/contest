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
A,B = map(int,input().split())
K = int(input())
P = list(map(int,input().split()))

# start, goalが不明, 途中がPで寄り道なし
#  => P + [start, goal] の各要素が1つずつなら ok

P += [A,B]
from collections import Counter
C = Counter(P).most_common()

print("YES" if C[0][1] == 1 else "NO")