# #Ex:1. Get the value of the "model" key:
# thislist={'name':'verna','model':'v24',}
# x=thislist['model']
# print(x)
#
# #      OR( get() method also use for item )
# x=thislist.get('name')
# print(x)
#
# # Get keys
# x=thislist.keys()
# print(x)
#
# #Get Values
# x=thislist.values()
# print(x)
#
# # Add a new item to the original dictionary, and see that the keys list gets updated as well:
# thislist={'name':'verna','model':'v24',}
# thislist['city']='Mumbai'
# print(thislist)
#
# # Get Items
# x=thislist.items()
# print(x)

########### Check if Key Exists ##############
# Check if "model" is present in the dictionary:
thislist={'name':'verna',
          'model':'v24',
          'City':'Mumbai'}
if 'City' in thislist:
    print("Yes,'Mumbai' city is present in dictonary")