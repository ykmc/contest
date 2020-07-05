#!/usr/bin/env pypy

import sys
input = sys.stdin.buffer.readline
INF = float("inf")

def main():
    N,M = map(int,input().split())

    # dp[i][j] : i番目の鍵までを使い, j の組み合わせの箱を開けるのに必要な最小費用
    dp = [[INF for _ in range(2**N)] for _ in range(M+1)]
    dp[0][0] = 0

    for i in range(M):
        a,b =map(int,input().split())
        c = list(map(int,input().split()))

        # 開錠可能な箱をbitで表現する
        bit = 0
        for x in c:
            bit |= 1 << (x-1)
        
        for j in range(2**N):
            # 鍵を使う場合
            dp[i+1][j | bit] = min(dp[i+1][j | bit], dp[i][j] + a)
            # 鍵を使わない場合
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    
    if dp[-1][-1] == INF:
        print(-1)
    else:
        print(dp[-1][-1])

if __name__ == "__main__":
    main()