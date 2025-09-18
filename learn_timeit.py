import timeit,random

def list_generate_random(amount : int) -> list[float]:
    random_numbers : list[float] = []
    # You should use _ when:
    # 1.You don't need to use the loop variable inside the loop body.
    # 2.You want to avoid potential warnings from linters about unused variables.
    for _ in range(amount):
        random_numbers.append(random.random())
    return random_numbers
def comp_generate_random(amount : int) -> list[float]:
    return [random.random() for _ in range(amount)]
amount_n=20
# globals is an optional argument of timeit method, gives it access to the global scope.
# Without globals, the statements you pass won’t be able to access your globally defined variables and functions, leading to errors.
list_time : float = timeit.timeit(stmt = "list_generate_random(amount = amount_n)", 
                                  globals=globals())
comp_time : float = timeit.timeit(stmt = "comp_generate_random(amount = amount_n)",
                                  globals = globals())
print(f"list time is => {list_time}")
print(f"comp time is => {comp_time}")

# repeat(stmt, setup, timet, repeat, number, globals
import timeit

def test_function():
    return [i for i in range(1000)]

# Test multiple times, each executing the statement 10,000 times
multiple_test_times = timeit.repeat("test_function()", globals=globals(), number=10000, repeat=5)
print(min(multiple_test_times))

# Key Differences:
# timeit.timeit() runs once and gives a single time measurement.
# timeit.repeat() runs the code multiple times (as specified by repeat) and gives a list of multiple time measurements, 
# which you can analyze to account for fluctuations.