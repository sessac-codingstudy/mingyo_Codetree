num1 = list(map(int,input().split()))
arr = num1
for i in range(2,10):

    arr.append((arr[i-2]+arr[i-1])%10)
print(*arr)

   