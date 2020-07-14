#!/usr/bin/env python

import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10**6)

def main():
    S = input().decode().rstrip()
    print(S[0:3])

if __name__ == "__main__":
    main()