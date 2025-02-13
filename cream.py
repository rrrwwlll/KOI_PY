N,K,P=map(int,input().split())
a=list(map(int,input().split()))
result = 0
for i in range(N):
    count=0
    for j in range(K):
        if a[i*K+j] == 0:
            count = count + 1
    
    if P > count :
        result = result + 1
   
print(result)