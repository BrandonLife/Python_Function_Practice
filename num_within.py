def num_within(n, beg_of_range, end_of_range):
    if n >= beg_of_range and n <= end_of_range:
        return True
    else:
        return False


print(num_within(3, 2, 4))
print(num_within(10, 2, 4))
