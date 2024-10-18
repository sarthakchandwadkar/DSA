#Updated

monthly_expence = [2200,2350,2600,2130,2190]


#1. In feb,How many $ spent extra compared to jan
print('Extra spending : ',monthly_expence[1]-monthly_expence[0])

#2. Find out your total expense in first quarter (first three months) of the year.
print("Total Expence in 1st quarter is: ",monthly_expence[0]+monthly_expence[1]+monthly_expence[2])

#3. Find out if you spent exactly 2000 dollars in any month
print("Exactly 2000$ spent in month:" ,2000 in monthly_expence)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("Ading June month expense... ", monthly_expence.append(1980), "\nUpdated List",monthly_expence)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

monthly_expence[3] = monthly_expence[3] - 200
print(monthly_expence)