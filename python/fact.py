num=5
factorial=1
if num<0:
    print("the factorial of zero is doesnt exit")
elif num==0:
    print("the factorial of 0 is one")
else:
    if num>0:
        for i in range (1,num+1):
            factorial=factorial*i
        print("the factorial of a ",num,"is",factorial) 