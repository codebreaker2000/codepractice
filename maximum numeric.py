str=input("enter a alphanumeric string")
i=0
numbers=0
numbersi=[]
while(i<=len(str)-1):
    numbers=0
    while(str[i].isdigit()):
        numbers=numbers*10+int(str[i])
        i=i+1
        if(i==len(str)):
            break
    i=i+1
    numbersi.append(numbers)
print(max(numbersi))
