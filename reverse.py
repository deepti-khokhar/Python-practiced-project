num=int(input("enter any nummber"))
reverse=0
while num>0:
        digit=(num%10)
        reverse=(reverse*10)+digit
        num=num//10
print("the reverse of a number is",reverse)