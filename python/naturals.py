n=int(input("enter any number"))
def sum(n):
    if n==0 or n==1:
        return 1
    else:
        return n+sum(n-1)


add= sum(n)
print(f"The sum of {n} is {add}")