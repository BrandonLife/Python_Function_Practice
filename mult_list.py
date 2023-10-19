def mult_list(n, args):
    mult = 1
    for arg in args:
        mult *= arg * n
    return mult


print(mult_list(3, [3, 7, 4, 8]))
