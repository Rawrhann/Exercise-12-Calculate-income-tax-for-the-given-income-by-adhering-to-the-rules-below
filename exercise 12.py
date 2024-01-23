#Exercise 12: Calculate income tax for the given income by adhering to the rules below
#Taxable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20
#Expected Output:

#For example, suppose the taxable income is 45000, and the income tax payable is

#10000*0% + 10000*10%  + 25000*20% = $6000.

(number) = int(input("Enter an Integer: "))
print ("your number is", number)

if number <= 10000:
    print("your income tax is 0")
elif number <= 20000 and number > 10000:
    tax = (number - 10000)/10
    print("your income tax is", tax)
else: 
    first_tax = 1000
    second_tax = (number - 20000) * .2
    final_tax = first_tax + second_tax
    print("your income tax is ", final_tax)