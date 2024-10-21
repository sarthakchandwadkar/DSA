#1. Create a variable 'minVal' and set it equal to the first value of the array.
#2. Go through every element in the array.
#3. If the current element has a lower value than 'minVal', update 'minVal' to this value.
#4. After looking at all the elements in the array, the 'minVal' variable now contains the lowest value.

#Variable 'minVal' = array[0]
#   For each element in the array
#    If current element < minVal

my_array = [7, 12, 9, 4, 11]
minVal = my_array[0]  # Step 1
for i in my_array:  # Step 2
    if i < minVal:  # Step 3
        minVal = i
print('Lowest value: ', minVal)  # Step 4