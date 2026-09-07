#simple Calculator
print("*-*"*20)
print("Simple Calculator")
print("*-*"*20)
while True:
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()
    choice=int(input("Enter your choice(1/2/3/4): "))
    print()
    if choice in (1,2,3,4):
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        print()
        if choice==1:
            print(num1,"+",num2,"=",num1+num2)
        elif choice==2:
            print(num1,"-",num2,"=",num1-num2)      
        elif choice==3:
            print(num1,"*",num2,"=",num1*num2)          
        elif choice==4:
            if num2==0:
                print("Enter division by zero not possible")
            else:
                print(num1,"/",num2,"=",num1/num2)
        elif choice==5:
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
                    
