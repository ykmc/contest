# python 3.4.3
import sys
input = sys.stdin.readline

# -------------------------------------------------------------
# library
# -------------------------------------------------------------



# -------------------------------------------------------------
# main
# -------------------------------------------------------------
A,B = map(int,input().split())

print("Odd" if (A*B)%2==1 else "Even")