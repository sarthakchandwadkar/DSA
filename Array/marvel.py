heros=['spider man','thor','hulk','iron man','captain america']\

#1. Length of list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("Black Panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

heros.remove("Black Panther")
heros[3] = "Black Panther"

print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros[1:3] = ["Doctor Strange"]
print(heros)

# 5. Sort the list in alphabetical order
heros.sort()
print(heros)