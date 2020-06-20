# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
def dfs(list):
    # 部下がいなければ : 1
    if len(list) == 0:
        return 1
    # 部下がいれば
    else:
        # 部下の給料を全部調べてから
        salary = []
        for l in list:
            salary.append(dfs(B[l]))
        # 定義に従って計算
        return max(salary) + min(salary) + 1

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N = int(input())
B = [[] for i in range(N)]
for i in range(1,N):
    b = int(input())
    B[b-1].append(i)
 
print(dfs(B[0]))