#You can loop through a dictionary by using a for loop.
# ex:1
thisdict_1={'name':'Anjana',
          'College':'Shivaji mahavidayala',
          'City':'Udgir',
          'Study':'MCA'}
for x in thisdict_1:
    print(x)


# ex:2
for x in thisdict_1.keys():    # Print keys
    print(x)

# ex:3
for x in thisdict_1.values():  #Print values
    print(x)

# ex:4
for x,y in thisdict_1.items():   #Print items
    print(x,y)