
values = [["test", "test2"], ["check", "check2"], ["final", "final2"]]
string = "test 1space  2paces   3spaces"


for i in values:
    print(i[0])


#for sublist in values:
#    if "check2" in sublist:
#      print("it works")


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