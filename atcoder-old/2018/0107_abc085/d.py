# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,H = map(int,input().split())
AB = list(tuple(map(int,input().split())) for _ in range(N))

# 刀を振る攻撃は、最高威力のみを使うのが最善、よって最大値が分かれば良い
attack = 0
for a,b in AB:
    attack = max(attack, a)

# 刀を投げる攻撃は、刀を振る攻撃より高威力の場合のみ使えば良い
throw = list()
for a,b in AB:
    if b > attack:
        throw.append(b)

# 刀は高威力のものから投げる
throw.sort(reverse=True)

# 敵が死ぬか、高威力の刀がなくなるまで刀を投げる
ans = 0
for dam in throw:
    H -= dam
    ans += 1
    if H <= 0:
        break

# 敵が死んでいる場合
if H <= 0:
    print(ans)
# 敵がまだ生きている場合、通常攻撃を死ぬまで繰り返す
else:
    print(ans + (H-1)//attack + 1)