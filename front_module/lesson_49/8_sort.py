
def get_length(x):
    return len(x)

a = ["Ulan", "German", "Alua", "Almas"]
#      4         6       4        5

sorted_a = sorted(a, key=get_length)
# sorted_a = sorted(a)

# print(sorted_a)


b = [1, 6, 7]

# res = []
# def mult2(x):
#     return x * 2
# def is_even(x):
#     return x % 2 == 0
# for elem in b:
#     res.append(mult2(elem))

# for elem in b:
#     if is_even(elem):
#         res.append(elem)

# res = list(map(lambda x: x * 2, b))
res = list(filter(lambda x: x % 2 == 0, b))

print(res)









