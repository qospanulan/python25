from collections.abc import Callable, Iterable

# def get_sum(x: int , y: int) -> int:
#     return x + y

# def get_mult(x: int, y: int) -> int:
#     return x * y


def get_result(
        op_function: Callable, 
        x: int, 
        y: int
) -> int:
    print(f"in function: {type(op_function)}")
    result = op_function(x, y)

    return result




res = get_result(
    op_function=lambda x, y: x + y,
    x=3,
    y=5
)

print(f"Result 1: {res}")

res = get_result(
    op_function=lambda x, y: x * y,
    x=3,
    y=5
)

print(f"Result 2: {res}")


