# Python3 (3.4.3)
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------


# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,A,B,C = map(int,input().split())
L = [int(input()) for _ in range(N)]
 
from itertools import product
ans = float("inf")

# 全パターン試す
# 0 : 使わない
# 1,2,3 : A,B,Cとして使う
for p in product(range(4),repeat=N):
    a = [L[i] for i in range(N) if p[i]==1]
    b = [L[i] for i in range(N) if p[i]==2]
    c = [L[i] for i in range(N) if p[i]==3]
 
    if a==[] or b==[] or c==[]:
        continue
    
    t = 0
    for x in [a,b,c]:
        # 複数要素あるなら合成魔法を使って1つに
        if len(x)>=2:
            t += (len(x)-1)*10
    sumA = sum(a)
    sumB = sum(b)
    sumC = sum(c)
    # 目標との差分を 延長魔法or短縮魔法 で埋める
    t += abs(A-sumA) + abs(B-sumB) + abs(C-sumC)
 
    ans = min(ans,t)
 
print(ans)