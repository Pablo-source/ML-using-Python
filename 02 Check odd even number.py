# ### 2. Check when value is odd or even number
def isodd(value):
    if value % 2 == 1:
        print(f"{value} is an odd number")
    elif value % 2 == 0:
        print(f"{value} is an even number")

isodd(4)
isodd(7)