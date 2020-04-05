# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
S = input().rstrip()

N = len(S)
ans = [-1,-1]

# 連続する2文字が同じ場合、アンバランスである
for i in range(N-1):
    if S[i] == S[i+1]:
        ans = [i+1,i+2]
        break

# 連続する3文字で、両端の文字が同じならアンバランスである
for i in range(N-2):
    if S[i] == S[i+2]:
        ans = [i+1, i+3]
        break

# 4文字以上においてある文字が過半数になる場合、上記の2条件を満たさずには実現不可能


print(ans[0], ans[1])