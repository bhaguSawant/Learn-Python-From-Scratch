# 1. Union() Join
# -----Union () are return a new set with all item from both set
# Ex:1
set1={'Apple','Banana','Cherry'}
set2={1,2,3}
set3= set1.union(set2)
print(set3)

# Ex:2
set_1={'Apple','Banana','Cherry'}
set_2={4,5,6}
set_3 = set_1 | set_2
print(set_3)

# 2. intersection() join
# ---------intersection() keeps only duplicates items
# Ex:1
set_5={'Apple','Banana','Cherry'}
set_6={'Apple','Papaya'}
set_7= set_5.intersection(set_6)
print(set_7)

# Ex:2
set_My={'Apple','Banana','Cherry'}
set_Hi={'Apple','Papaya'}
set_8= set_My & set_Hi
print(set_8)

# 3. Difference
# Difference it's mean first set1 item that are not present in other means set2
# Ex:1
myset1={'W','Q','R','T'}
myset2={'u','Q','A'}
myset3 = myset1.difference(myset2)
print(myset3)

# Ex:2
myset1={'W','Q','R','T'}
myset2={'u','Q','A'}
myset3 = myset1 - myset2
print(myset3)

# Symmetric Difference
# The symmetric difference will keep only the element that are not present in both sets
# Ex:1
set={"Two","Three","Four"}
set9={"Two","Six","One"}
set10=set.symmetric_difference(set9)
print(set10)