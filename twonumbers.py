num1 = int(input("Enter your 1st number:"))
operation = int(input("1 for addition, 2 for subtraction, 3 for multiplication, 4 for division:")) 
num2 = int(input("Enter your 2nd number:"))
    
def sum():
    add = num1 + num2
    print(f"The result: {add}")

def sub():
    subt = num1-num2
    print(f"The result:{subt}")

def mul():
    multiply = num1*num2
    print(f"The result: {multiply}")
    
    
def div():
     division = num1/num2
     print(f"The result:{division}")

if operation==1:
 sum()
elif operation==2:
 sub()
elif operation==3:
 mul()
elif operation==4:
 div()
else:
    print("Cannot solve, wrong operator!")


    

    