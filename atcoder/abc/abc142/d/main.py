#!/usr/bin/env python3

import sys

input = sys.stdin.buffer.readline

def gcd(a,b):
    return a if b == 0 else gcd(b,a%b)

def lcm(a,b):
    return a*b // gcd(a,b)

def prime_factorize(n):
    pf={}
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            pf[i] = pf.get(i, 0) + 1
            n //= i
    if n > 1: pf[n] = 1
    return pf

A,B = map(int,input().split())

pf = prime_factorize(gcd(A,B))
print(len(pf) + 1)