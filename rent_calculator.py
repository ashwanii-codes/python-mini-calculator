Total_rent = int(input("Enter Total Rent = "))
person =int(input("Enter the person living in room = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))

#output
total_bill = electricity_spend * charge_per_unit
output = (Total_rent + food + total_bill) // person

print(f"Each person will pay {output}")