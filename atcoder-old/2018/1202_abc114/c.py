# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------

# s で始まる七五三数
def dfs(s):
    if int(s) > N:
        return 0
    if s.count("3") > 0 and s.count("5") > 0 and s.count("7") > 0:
        cnt = 1
    else:
        cnt = 0
    for c in "753":
        cnt += dfs(s + c)
    return cnt
    

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())

print(dfs("0"))