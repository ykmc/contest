# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
N = 100010
primes = []
is_prime = [True]*N
for i in range(2,N):
    if is_prime[i]:
        primes.append(i)
        j = 2
        while i*j < N:
            is_prime[i*j] = False
            j += 1


# -------------------------------------------------------------
# main
# -------------------------------------------------------------

Q = int(input())
LR = [tuple(map(int,input().split())) for _ in range(Q)]

# 2017数の判定リストを作る
Ans = [0]*N
for p in primes:
    if p==2:
        continue
    # pは素数であるので、(p+1)//2が素数であれば 2017数
    if (p+1)//2 in primes:
        Ans[p] = 1

# 範囲計算なので累積和
for i in range(1,N):
    Ans[i] += Ans[i-1]

# クエリを処理
for l,r in LR:
    print(Ans[r] - Ans[l-1])

