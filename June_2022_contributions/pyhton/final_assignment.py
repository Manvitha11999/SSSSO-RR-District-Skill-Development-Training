import addition
import multiplication
num=input("enter 4 numbers with space")
n = list(map(int,num.split()))
if len(n)<4:
    print("you should enter exactly 4 numbers")
else:
    sum=[]
    for i in n:
        if(i%2==0):
            sum.append(i)
    print("Select operation.")
    print("1.Add")
    print("2.multiplication")
    while True:
        choice = int(input("Enter choice(1/2):"))
        if choice==1:
            print("sum:",addition.add(sum[0],sum[1])) 
        elif choice==2:
            print("mul:",multiplication.mul(sum[0],sum[1]))
        else:
            print("invalid input")

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break