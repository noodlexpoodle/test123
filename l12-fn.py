# def greet():
#     print('hello world')
#
# greet()
# greet()
# greet()
# greet()
def greet(a='sir',d='day'):
    print(f'Good {d}, {a}')
# f'text {variable}
# f is for formatting, the {} will be the variable
b=input("What's your name ")
c=input("What's the time ")
if b is not None and c is not None:
    greet(b,c)
    print(1)
elif b is not None and c is None:
    greet(c='day')
    print(2)
elif b is None:
    greet(b='sir')
    print(3)
else:
    greet()
    print(4)
    pass

# First define the function with def name (var)
# Then call function by name and input the variable
# SIMPLE!
# You can input a default value in case value is missing
