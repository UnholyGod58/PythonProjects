
values = [["user", 1.4, 2.0], ["user2", 2.4, 3.6], ["user3", 3.1, 4.6]]
string = "test 1space  2paces   3spaces"
user_in = 1


sum = 0
count = 0
for i in values:
    for j in i:
        if isinstance(j, float):
            sum += j
            count += 1    
            avg = sum/count
print(avg)
    

#index = 0
#while index < len(values[user_in]):
#    if isinstance(values[user_in][index], float):
#        print(values[user_in][index])
#    index += 1 

#improved version 
#for value in values[user_in][1:]:
#    if isinstance(value, float):
#        print(value)
    
#if "user" in values:
#    print("it sees all") - not how sublists work

#for i in values:
#    if "user" in i:
#        print("works")

#sum = 0.0
#count = 0.0
#for i in values[1]:
#    if isinstance(i, float):
#       sum += i
#       count += 1
#print(sum/count)


#for sublist in values:
#    if "check2" in sublist:
#      print("it works")


#for i in values[1][1:]:
#        print(i)

#for i in values[1:]:
#    print(i[0])


#for index, sublist in enumerate(values):
#    if "final" in sublist:
#      i = index
#      break
#print(i)


#string = string.replace("  ", " ") #only works for double spaces, can't use + like in re.sub

#import re
#string = re.sub(' +',' ',string)

#print(string)



#test = False 
#def function1_test():
#    print("function 1")
#def function2_test():
#    print("function 2")
#def test_function(function1, function2):
#    if test == True:
#       function1()
#    else:
#        function2()    
#test_function(function1_test, function2_test)