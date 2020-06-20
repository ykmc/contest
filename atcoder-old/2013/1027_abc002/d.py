# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,M = map(int,input().split())
A = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    A[x-1][y-1] = 1
    A[y-1][x-1] = 1
for i in range(N):
    A[i][i] = 1

ans = 0

i = 0
while i < 2**N:
    # 初期化
    is_clique = True
    # bit全探索
    bit = bin(i)[2:].zfill(N)
    # 今回探索するメンバーを列挙
    G = list()
    for j in range(N):
        if bit[j]=="1":
            G.append(j)
    # 関係がないメンバーがいないか？
    for g1 in G:
        for g2 in G:
            if A[g1][g2] == 0:
                is_clique = False
    # クリークの場合、答えを更新
    if is_clique:
        ans = max(ans, bit.count("1"))
    # increment
    i += 1

print(ans)