from sys import stdin

firstWord = stdin.readline().strip()
secondWord = stdin.readline().strip()
priceLetter = list(map(int, stdin.readline().split()))
dp = [[0 for _ in range(len(firstWord) + 1)]
      for __ in range(len(secondWord) + 1)]
for i in range(1, len(secondWord) + 1):
    for j in range(1, len(firstWord) + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if secondWord[i - 1] == firstWord[j - 1]:
            dp[i][j] = max(dp[i][j],
                           dp[i - 1][j - 1] + priceLetter[
                               ord(secondWord[i - 1]) - ord('a')])
print(dp[-1][-1])
