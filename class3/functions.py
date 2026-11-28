# functions

# def calc_sum():
#     a = 10
#     b = 10
#     print(a + b)

# def calc_sum(val1, val2): #parameters
#     a = val1
#     b = val2
#     print(a + b)
#     return a + b

# calc_sum(20, 30) # arguments
# calc_sum(10, 20)
# calc_sum(5, 7)

# def mult(val):
#     print(5 * val)

# sum = calc_sum(10, 20)
# mult(sum)

# # function ka syntax, parameter, argument, return statement, default parameters
# def calc_sum(val1 = 10, val2 = 20): #parameters
#     a = val1
#     b = val2
#     print(a + b)
#     return a + b

# calc_sum()
# calc_sum(5, 7)
# #positional params, default param

# # unlimited args
# def take_orders(*args):
#     print(type(args))
#     #print(args)
#     for item in args:
#         print(item)

# take_orders("Biryani", "Korma", "Haleem", "Daal")


# def std_data(**kwargs):
#     print(kwargs)
#     print(type(kwargs))


# std_data(name="akrima", age=30, inst="Jawan Pak", gender="Male")


def get_orders(val1, val2=2, *args, **kwargs):
    print(val1)
    print(val2)
    print(args)
    print(kwargs)

get_orders(10, 20, "Biryani", "Tikka", name="Akrima", amount=900)