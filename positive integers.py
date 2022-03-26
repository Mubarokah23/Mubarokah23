num = input("Enter a number: ")
num = int(num)
if num>0:
	print("The number is a positive integers")
else:
    print("It is not a positive integers")
    
sum = (num*(num+1))//2
print(f"The sum of all positive int  from 1 to num is : {sum} ")
