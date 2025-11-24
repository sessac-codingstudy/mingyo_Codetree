N = int(input())
result = list(map(int,input().split()))
                #시작값 끝값 증가값
for i in range(N-1,-1,-1):

    if  result[i] % 2 == 0:
        print(result[i],end=" ")
