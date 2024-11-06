def cube(n):
    return n*n*n
print("Cube of n is ",cube(6))
def check(n):
    if n%3==0:
        return cube(n)
    else:
        return False
print("Checking whether the number is divisible by 3 and cube of it is:", check(9))