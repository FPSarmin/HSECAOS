from functools import reduce
print(*reduce(
    lambda x, y: map(
        lambda a: a[0] ^ a[1],
        zip(x, y)),
    map(
        lambda line: map(int, line.split()),
        map(
            lambda lines: input(),
            range(int(input()))
        )
    )
)
      )