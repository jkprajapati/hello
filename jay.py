# jay=634
# rutik=5444
# subham=90
# dipen=9999

# test1=jay>rutik and jay>subham and jay>dipen
# test2=rutik>subham and rutik>dipen
# test3=subham>dipen

# test1=jay>rutik and jay>subham and jay>dipen
# test2=rutik>subham and rutik>dipen
# test3=subham>dipen

# test1=jay>rutik and jay>subham and jay>dipen
# test2=rutik>subham and rutik>dipen
# test3=subham>dipen

# test1=jay>rutik and jay>subham and jay>dipen
# test2=rutik>subham and rutik>dipen
# test3=subham>dipen

# if jay>rutik and jay>subham:
#     print("jay")
# elif rutik>subham and rutik>dipen:
#     print("rut")
# elif subham>dipen:
#     print("subham")
# else:
#     print("dipen")
# if test1 == True:
#     print("jay")
# elif test2==True:
#     print("rutvik")
# elif test3==True:
#     print("shubham")
# else:
#     print("deepen")
# else:
#     if rutik>subham and rutik>dipen:
#         print("rut")
    
#     elif subham>dipen:
#         print("subham")
#     else:
#         print("dipen")

# if jay>rutik:
#     if jay>subham:
#         if jay>dipen:
#             print("jay")
#         else:
#             print("dipen")
#     else:
#         print("shubham")

# elif rutik>subham:
#     if rutik>dipen:
#       print("rutik")
#     else:
#         print("dipen")
# elif subham>rutik :
#     if subham>dipen:
#         print("shubham")
#     else:
#         print("dipen")



y1=input("enter the string:")#heart
y2=input("enter the string")#earth
l1=[[i for i in y1]
,[i for i in y2]]
l1[0].sort()
l1[1].sort()

if l1[0]==l1[1]:
    print("anagram")
else:
    print("not anagram")
# c1=0
# c2=0
# if len(y1)==len(y2):
#     for i in y1:
#         if i in y2:
#             c1+=1
        
#     for i in y2:
#         if i in y1:
#             c2+=1
    
#     if c1==c2:
#         print("both strings are anagrams")
#     else:
#         print("both strings are not anagrams")
        
# else:
#         print("both strings are not anagrams")
