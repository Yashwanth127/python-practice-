def sum_1_to_n(n: int) -> int:
    if n <= 0:
        return 0
    return n * (n + 1) // 2


print(sum_1_to_n(5))