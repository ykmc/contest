# Python3 (3.8.2)
import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())
MOD = 10**9+7

print(((A*B)%MOD * C)%MOD)