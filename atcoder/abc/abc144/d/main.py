#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)
INF = float("inf")

import math

def main():
    A,B,X = map(int,input().split())

    # 2次元で考える
    X /= A

    # 水位が, 断面の対角線より上
    if X > A*B/2:
        ans = math.atan(2*(A*B-X)/(A**2))
    # 水位が, 断面の対角線より下
    else:
        ans = math.atan(B**2/(X*2))
    
    print(ans * 180 / math.pi)

if __name__ == "__main__":
    main()