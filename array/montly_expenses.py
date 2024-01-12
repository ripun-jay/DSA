"""

Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this

"""

monthly_expencess = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(monthly_expencess[1], "is expense of Feb")

# 2. Find out your total expense in first quarter (first three months) of the year.
first_quarter_expense = sum(monthly_expencess[:3])
print(first_quarter_expense, "isexpense of first quarter")

# 3. Find out if you spent exactly 2000 dollars in any month
for i in range(len(monthly_expencess)):
    if i == 2000:
        print(f"there is no expense of 2000 in {i+1}th month")
else:
    print("there is no expense like 2000")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list  > O(n)
monthly_expencess.append(1980)
print("our monthly expenses is", monthly_expencess)

# You returned an item that you bought in a month of April andgot a refund of 200$. Make a correction to your monthly expense list based on this
monthly_expencess[3] = monthly_expencess[3] - 200
print("updated monthly expenses after getting refund of april month is", monthly_expencess)