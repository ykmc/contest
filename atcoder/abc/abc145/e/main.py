#!/usr/bin/env pypy

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def main():
    N,T = map(int,input().split())        
    AB = [(0,0)] + [tuple(map(int,input().split())) for _ in range(N)]

    # 最後に食べるものを全探索し, それ以外でDPしたくなる
    # 普通にやると TLE だが, 左から,右から で事前にDPしておくことで計算量を落とせる

    # このとき, 配列添字を 1〜N にしておくと楽
    #   1番目の料理を最後に食べるとき : dp1[0][] + b + dp2[2][], このときに index out of range しないのが嬉しい
    #   2番目の料理を最後に食べるとき : dp1[1][] + b + dp2[3][]
    #   ...
    #   N番目の料理を最後に食べるとき : dp1[N-1][] + b + dp2[N+1][], dp2 は N+2 の長さがあると良さそう

    # dp1[i][j] : 1〜i 番目の料理から選んで T 分以内に食べるときの美味しさの和の最大値
    dp1 = [[0 for _ in range(T+1)] for _ in range(N+1)]
    for i in range(1,N+1):
        a,b = AB[i]
        for j in range(T+1):
            # 食べる
            if j >= a:
                dp1[i][j] = max(dp1[i-1][j], dp1[i-1][j-a] + b)
            # 食べない
            else:
                dp1[i][j] = dp1[i-1][j]

    # dp2[i][j] : i〜N 番目の料理から選んで T 分以内に食べるときの美味しさの和の最大値
    dp2 = [[0 for _ in range(T+1)] for _ in range(N+2)]
    for i in range(N,0,-1):
        a,b = AB[i]
        for j in range(T+1):
            # 食べる
            if j >= a:
                dp2[i][j] = max(dp2[i+1][j], dp2[i+1][j-a] + b)
            # 食べない
            else:
                dp2[i][j] = dp2[i+1][j]
    
    # 最後に食べる料理で全探索
    ans = 0
    for i in range(1,N+1):
        a,b = AB[i]
        for j in range(T):
            ans = max(ans, dp1[i-1][j] + b + dp2[i+1][T-1-j])
    
    print(ans)

if __name__ == "__main__":
    main()