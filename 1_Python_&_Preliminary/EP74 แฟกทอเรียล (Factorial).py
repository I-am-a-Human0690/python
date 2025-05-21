#factorial
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
f=factorial(5)
print(f)
'''
5! = 5x4x3x2x1
3! = 3x2x1
'''

       