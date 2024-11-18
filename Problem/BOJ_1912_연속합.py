#S2_1912_연속합

def cont(n,a):
  dp=[0]*n
  dp[0]=a[0]

  for i in range(1,n):
    dp[i] = max(dp[i-1]+a[i],a[i])

  return max(dp)


n=int(input())
a=list(map(int,input().split()))

print(cont(n,a))
