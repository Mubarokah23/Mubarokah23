rating= input("enter the employee performance")
rating= float(rating)
fee = 2400
amount= fee*rating
print(f"The amount employee raise is {amount} ")
if rating==0.0:
	print("the performance is unacceptable")
elif rating==0.4:
	print("the performance is acceptable")
elif rating>=0.6:
	print("the performance is meritorious")
else:
	print("invalid performance")