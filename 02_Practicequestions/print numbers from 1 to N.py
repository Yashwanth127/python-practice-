#Use a simple loop from 1 to N. In interviews, clarify: inclusive/exclusive, handling invalid input, and printing format.
def print_numbers(n: int) -> None:
    if n <= 0:
        return
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

# Example
print_numbers(20)