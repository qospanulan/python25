
class ErrorWithDivision(Exception):
    def __init__(self, message, *args):
        super().__init__(message, *args)


def func1() -> int | None:

    try:
        a = 4 / 0

    except ZeroDivisionError as e:
        raise ErrorWithDivision(message="Попытка разделить на ноль.")

    return a


try:
    a = func1()

except ErrorWithDivision as e:
    print(f"ErrorWithDivision: {e}")
    a = None
except Exception as e:
    print(f"Error: {e}")
    a = None

print(f"a: {a}")

