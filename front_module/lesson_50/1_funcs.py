# positional args / keyword args
# default params
# ...


# def get_sum(
#     x: int = 0, 
#     y: int = 0, 
#     z: int = 0,
#     p: int = 0
# ):
#     print(f"{x=}")
#     print(f"{y=}")
#     print(f"{z=}")
#     print(f"{p=}")
#     return x + y + z + p

# def get_sum(
#     number1: int,
#     number2: int,
#     *args
# ) -> int:
#     print(f"{number1=}")
#     print(f"{number2=}")
#     print(f"{args=}")

#     res = number1 + number2

#     for number in args:
#         res += number

#     return res



# def get_as_dict(
#     name: str,
#     **kwargs,
# ) -> dict:

#     res = {
#         "name": name
#     }

#     res.update(kwargs)

#     print(f"{kwargs=}")
#     print(f"type: {type(kwargs)}")

#     return res




def get_as_dict(
    *numbers,
    **kwargs,
) -> int:
    
    print(f"{numbers=}")
    print(f"type: {type(numbers)}")

    print(f"{kwargs=}")
    print(f"type: {type(kwargs)}")


    return 0



res = get_as_dict("Harry", age=11)
print(f"res: {res}")








# positional / kw args
# res = get_sum(2, 7, 5)
# res = get_sum(z=2, y=7, x=5)

