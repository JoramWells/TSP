def foo(x,y,z):
    return 6*x**3 + 9*y**2 + 90*z -25
print(foo(1,1,3))

def fitness(x,y,z):
    ans = foo(x,y,z)

    if ans == 0:
        return 99999
    else:
        return abs(1/ans)