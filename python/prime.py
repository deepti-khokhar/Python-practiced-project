num=20
count=0
if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count==2:
            print("the num is prime")
    else:
            print("the num is not prime")