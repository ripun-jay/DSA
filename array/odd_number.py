max_limit = input("enter max limit of your odd number:  ")
max_limit = int(max_limit)
if max_limit % 2 == 0:
    series = [((2*i)+1) for i in range(max_limit//2)]
else:
    series =  [((2*i)+1) for i in range(((max_limit//2)+1))]
print(series)


# to check ascii value of char 
ord("5")
# why not ord(0)