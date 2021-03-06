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

from collections import Counter
L = len(Counter(A))

# 全体枚数が奇数で, カードの種類が偶数 
#  -> 重複カードは奇数
#  -> どれか1種類は全て捨てないと重複カードは処分不可能
if L%2==0:
    print(L-1)
# 重複カードが偶数, ペアを作って全て処分可能
else:
    print(L)