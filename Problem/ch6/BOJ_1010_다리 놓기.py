#S5_1010_다리 놓기

def bridge(n,m):
  # DP 테이블 초기화: dp[i][j]는 동쪽에 i개의 사이트가 있을 때 서쪽의 j개의 다리를 놓는 경우의 수
  dp=[[0]*(n+1) for _ in range(m+1)]

  # Base case: 서쪽에 다리를 하나도 놓지 않는 경우
  # 동쪽의 i개의 사이트에서 서쪽에 0개의 다리를 놓는 경우는 항상 1가지 경우 (아무것도 놓지 않음)
  for i in range(m+1):
    dp[i][0]=1

  # DP 점화식을 이용해 테이블 채우기
  for i in range(1,m+1): # 동쪽 사이트의 개수 (행)
    for j in range(1,n+1): # 서쪽 사이트의 개수 (열)
      # dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
      # dp[i-1][j-1]: 현재 동쪽 사이트를 포함하여 다리를 놓는 경우
      # dp[i-1][j]: 현재 동쪽 사이트를 건너뛰고 다리를 놓는 경우
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

  # 결과 반환: 동쪽에 m개의 사이트가 있을 때 서쪽에 n개의 다리를 놓는 경우의 수
  return dp[m][n]

# 입력 및 출력 처리
for _ in range(int(input())): # 테스트 케이스의 개수를 입력받음
  n,m=map(int,input().split()) # 서쪽 사이트(n), 동쪽 사이트(m)의 개수를 입력받음
  print(bridge(n,m)) # 각 테스트 케이스에 대해 결과 출력
