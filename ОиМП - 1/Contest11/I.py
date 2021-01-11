from itertools import permutations
print(*map(
    lambda x: x.strip('()').replace(',', '').replace(' ', ''),
    map(str, permutations(range(1, int(input()) + 1)))
), sep='\n')
