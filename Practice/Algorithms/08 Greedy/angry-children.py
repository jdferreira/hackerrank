#!/usr/bin/env python3

def maxmin(ns, k):
    ns.sort()
    return min(j - i for i, j in zip(ns, ns[k-1:]))

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    ns = [int(input()) for _ in range(n)]
    
    print(maxmin(ns, k))
