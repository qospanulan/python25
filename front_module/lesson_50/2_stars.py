
def get_sum(
    x: int, 
    y: int, 
    z: int
) -> int:
    print(
        f"x: {x} \n"
        f"y: {y} \n"
        f"z: {z}"
    )

    return x + y + z



# arr = [1, 3, 4, 8]
arr = {
    "x": 1,
    "y": 3,
    "z": 4
}

res = get_sum(**arr)  # source
# res = get_sum(x=1, y=3, z=4)  # like

# res = get_sum(*arr)  # source
# res = get_sum(1, 3, 4)  # like
print(res)





# множественное присвоение

# a, b, c = (1, 3, 5)

# print(a)
# print(b)
# print(c)


# a = 2
# b = 5

# c = a
# a = b
# b = c

# a, b = b, a

# print(f"a = {a}, b = {b}")