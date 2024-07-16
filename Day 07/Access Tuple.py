#Print the second item in the tuple:
thistuple=('A','B','C','D','E')
print(thistuple[2])

# Print the last item of the tuple:
thistuple1=('A','B','C','D','E')
print(thistuple1[-4])

# Return the third, fourth, and fifth item:
thistuple2=('A','B','C','D','E')
print(thistuple2[2:5])

# Range of Negative Indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[-4:-1])

# Check if Item Exists
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "banana" in thistuple3:
    print('Yes, banana is in this list')