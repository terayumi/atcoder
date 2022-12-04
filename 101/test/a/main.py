#!/usr/bin/env python3

#N = map(int, open(0).read().split())
S = input()
ans=0

for i in range(4):
    if S[i]=="+":
        ans+=1
    elif S[i]=="-":
        ans-=1
print(ans)

