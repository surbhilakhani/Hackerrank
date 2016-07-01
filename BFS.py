def short_paths(cost, nodes):
    for k in range(1, nodes):
        for i in range(1, nodes):
            for j in range(1, nodes):
                if cost[i][j] > cost[i][k]+cost[k][j]:
                cost[i][j] = cost[i][k]+cost[k][j]
return cost

tests = int(input())
while tests:
  x = input().split(" ")
  nodes, edges = int(x[0]), int(x[1])
  #initialize everything with infinity
  dp = [[1<<31 for i in range(nodes+1)] for i in range(nodes+1)]
  #distance between self is 0
  for i in range(nodes+1):
    dp[i][i] = 0
  while edges:
    p = input().split(" ")
    x, y = int(p[0]), int(p[1])
    #undirected graph
    dp[x][y] = 6
    dp[y][x] = 6
    edges -= 1
  src = int(input())
  dp = short_paths(dp, nodes+1)
  result = []
  for i in range(1, nodes+1):
    if src != i:
      if dp[src][i] == 1<<31:
        result.append("-1")
      else:
        result.append(dp[src][i])
  print(" ".join(str(e) for e in result))
  tests -= 1
