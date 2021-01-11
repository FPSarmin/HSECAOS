n = int(input())
results = list(map(int, input().split()))

ord_results = sorted(results, reverse=True)
ranks = {ord_results[0]: 1}

for i in range(1, len(results)):
    if ord_results[i] != ord_results[i - 1]:
        ranks[ord_results[i]] = i + 1
    else:
        ranks[ord_results[i]] = ranks[ord_results[i - 1]]

best_rank = len(results) + 1
start = results.index(max(results)) + 1

for i in range(start, len(results) - 1):
    if results[i] % 5 == 0 and results[i] % 10 != 0 and \
            results[i] > results[i + 1]:

        best_rank = min(best_rank, ranks[results[i]])

print(0) if best_rank == n + 1 else print(best_rank)
