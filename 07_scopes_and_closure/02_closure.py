# closure(factory functions) in python
# Example 1

x = 99
def f1():
    x = 88
    def f2():
        print(x)   
    return f2   # returning the reference of f2 - we are packing definition along with all associated var
    # also called bag theory
result = f1()
result()   # executing f2

# output: 88

# Example 2

def clfunc(num):
    def actual(x):
        return x ** num
    return actual

f = clfunc(2)   # f storing the refernce of actual along with associated var num which is 2
g = clfunc(3)   # g storing the refernce of actual along with associated var num which is 3

print(f)
print(g)

# <function clfunc.<locals>.actual at 0x0000023AC2F078A0>
# <function clfunc.<locals>.actual at 0x0000023AC2F07950>

print(f(3))  # Output: 9
print(g(3))  # Output: 27

# Example 3

def fu1(num1):
    def fu2(num2):
        print(f"num1 = {num1}")
        print(f"num12 = {num2}")
        # fu2 returns None
    return fu2

m = fu1(3)
n = fu1(4)

print(m(10))  # it also store the value returned by associated ref function
print(n(10))

# Output:

# num1 = 3
# num12 = 10
# None
# num1 = 4
# num12 = 10
# None