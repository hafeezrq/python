# Recursion in python

def rec_func(num):
    if num > 9:
        return num
    num += 1
    return rec_func(num)


total = rec_func(0)
print(total)
