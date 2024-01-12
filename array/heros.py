"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

"""

heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(f"Im fan of {len(heros)} super heros from marvel")

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print("my updates superheros are", heros)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
for i in range(len(heros)):
    if heros[i] == "hulk":
        heros.insert(i+1, "black panther")
print("my crnological ordered super heros are", heros)

# 4. Now you don't like thor and hulk because they get angry easily :) 
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.

heros[1:3]=['doctor strange']
print("my cool heros are", heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print("alphabetical oreded heros are", heros)
    
