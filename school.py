C=0
N,X=map(int,input().split())
rrrwwwlll = 0
for i in range(N):
    S,T=map(int,input().split())

    G = X / (S+T)
    if G <= 1:
        C = -1
    if G > 1:
        C = 0
        S = T+S
        C = max(rrrwwwlll,S)
        
print(C)
