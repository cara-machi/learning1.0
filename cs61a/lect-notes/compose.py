def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def square(x):
    return mul(x,x)

def make_adder(n):
    def adder(x):
        return x+n
    return adder

if __name="__main__":
    add2=make_adder(2)
    f=compose1(square,make_adder(2))
    print(f(3))
