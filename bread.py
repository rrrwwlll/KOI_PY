N=int(input())
answer = 0
for i in range(N):
    A,B=map(int,input().split())
    answer = [A,B]
    if A <= B:
        answer = min(B,answer)
        print(answer)
    elif A > B:
        answer = -1
    print(answer)
        
        #틀린거def Q():
        #if A == B:
            #print(A)
        #elif A > B:
            #print("-1")
        #elif A < B:
            #print(B)
    #def W():
        #print(min)
    #def D():
        #if A <= B:
            #print("10")
        #elif A > B:
            #print("-1")
    #if N == 1:
        #Q()
    #elif A == B:
        #W()
    #elif B == 10:
        #D()
    #elif A > B:
        #print("-1")
    #elif B <= A:
        #print(min(B))