def calc_bills(grocries,gas,autozone,walmart2,current): # define your inputs
    # inside the pranthesis.
    bills = current - grocries - gas - autozone - walmart2  # write your operations here
    return bills # returns the value of bills

# grocries = 75
# gas = 36.17
# autozone = 6.88
# walmart2 = 1.78
# current = 1030.00
# bills = grocries - gas - autozone - walmart2 - current

bills = calc_bills(75,36.17,6.88,1.78,1030.00) # stores the value returned by your
# function into bills variable
print("This is how much money i have left"f'\n {bills}')


'''
Think of calc_bills as a regular mathematical function, where calc_bills can be
represented as f(x). In this case we have multiple variables, so a better
representation could be f(x,y,z,t,s). Now what does your function do? In this case
it calculates the bill. To do so, it subtracts everything from your current moneyself.
So we can simplify it as f(x,y,z,t,s) = x-y-z-t-s. The return statement just returns
the value of f(x,y,z,t,s), which is x-y-z-t-s. Therefore, you need to store it in
a new local variable if you need the value. The useful thing about functions is that
you can reuse them multiple times.

'''
