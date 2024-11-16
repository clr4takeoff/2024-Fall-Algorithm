#S5_1010_다리 놓기

def bridge(n,m):
  dp=[[0]*(n+1) for _ in range(m+1)]

  for i in range(m+1):
    dp[i][0]=1

  for i in range(1,m+1):
    for j in range(1,n+1):
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

  return dp[m][n]

for _ in range(int(input())):
  n,m=map(int,input().split())

  print(bridge(n,m))
