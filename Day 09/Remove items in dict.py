#Remove items by using pop() method
thisdict={'name':'Anjana',
          'College':'Shivaji mahavidayala',
          'City':'Udgir'}
thisdict.pop('City')
print(thisdict)

# #Remove items by using popitem() method
thisdict={'name':'Anjana',
          'College':'Shivaji mahavidayala',
          'City':'Udgir',
          'Study':'MCA'}
thisdict.popitem()
print(thisdict)

# # #Remove items by using del() method
thisdict={'name':'Anjana',
          'College':'Shivaji mahavidayala',
          'City':'Udgir',
          'Study':'MCA'}
del thisdict['Study']
print(thisdict)

# The clear() method empties the dictionary:
thisdict_1={'name':'Anjana',
          'College':'Shivaji mahavidayala',
          'City':'Udgir',
          'Study':'MCA'}
thisdict_1.clear()
print(thisdict_1)
