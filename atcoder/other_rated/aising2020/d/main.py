#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

def popcount(n):
    ret = 0
    for i in range(18):
        if n>>i & 1:
            ret += 1
    return ret

def main():
    N = int(input())
    X = input().decode().rstrip()

    # X に含まれる "1" の数
    x_cnt = X.count("1")

    # i 桁目が 0 : x_cnt += 1
    # i 桁目が 1 : x_cnt -= 1
    # より, X mod x_cnt +1, X mod x_cnt-1 を事前計算しておく
    x_mod_pl,x_mod_mi = 0,0
    d_pl,d_mi = 1,1
    mod_pl,mod_mi = x_cnt+1,max(1,x_cnt-1)
    for i in range(N-1,-1,-1):
        if X[i]=="1":
            x_mod_pl = (x_mod_pl + d_pl) % mod_pl
            x_mod_mi = (x_mod_mi + d_mi) % mod_mi
        d_pl = (d_pl*2) % mod_pl
        d_mi = (d_mi*2) % mod_mi
    
    for i in range(N):
        ans = 1
        if X[i] == "1":
            # 1 -> 0 に変換した結果, １が全く存在しない場合
            if x_cnt == 1:
                print(0)
                continue
            a = (x_mod_mi - pow(2,(N-1-i), mod_mi)) % mod_mi
        else:
            a = (x_mod_pl + pow(2,(N-1-i), mod_pl)) % mod_pl

        while a > 0:
            pop_cnt = popcount(a)
            a %= pop_cnt
            ans += 1

        print(ans)

if __name__ == "__main__":
    main()