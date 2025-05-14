name="kaivan"                      # k a i v a n
                                   # 0 1 2 3 4 5
                                   #-6-5-4-3-2-1

print(name[0:3]) #start from 0 and end at 3 (excluded 3)

print(name[-4:-1]) #start from -4 (positive index : 2) and end at -1 (positive index : 5)(excluded -1)
print(name[2:5]) #start from 2 and end at 5 (excluded 5) (same as name[-4:-1])

print(name[:4]) #if no starting index specified that means from 0 index 
print(name[3:]) #if no ending index specified that means till last index

print(name[1:6]) #this will give aivan
print(name[1:6:2]) #this will skip 2 character and than give the result (see below comment for better understanding)
#name[1:6] = aivan
#name[1:6:2] = so first consider only 1:6 that means aivan
#now 1:6:2 means start from 1 i.e. a than skip 2 i.e. ai 
#than v than again skip 2 i.e. va than n
#so final output will avn