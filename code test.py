
#import os
#import pygame

values = [["user", 1.4, 2.0], ["user2", 2.4, 3.6], ["user3", 3.1, 4.6]]
string = "dawson, hoyle"
user_in = 1

for i, j in enumerate(string):
    if "," in j:
        print(i)
    

#for i in list:
#    print(i)

#sum = 0
#count = 0
#for i in values:
#    for j in i:
#        if isinstance(j, float):
#            sum += j
#            count += 1    
#            avg = sum/count
#print(avg)

#base = os.path.dirname(os.path.realpath("student_list.bin"))
#print(base + "/2D_Array/student_list.bin")
#input()

#list = ["test", "testess", "testes", "tessst"]
    
#def selectionSort(array):
#    for i in range(len(array)):
#        min_index = min(range(i, len(array)), key=array.__getitem__) #
##        array[i], array[min_index] = array[min_index], array[i]
#    return array

#def binary_search(arr, low, high, x):
 #   if high >= low:
  #      mid = (high + low) // 2
   #     if arr[mid] == x:
    #        return mid
     #   elif arr[mid] > x:
      #      return binary_search(arr, low, mid - 1, x)
#
 #       else:
  #          return binary_search(arr, mid + 1, high, x)
   # else:
    #    return -1

#def selectionSort(array, size):
 #   for ind in range(size):
  #      min_index = ind
   #     for j in range(ind + 1, size):
    #        if array[j] < array[min_index]:
     #          min_index = j    
      #  (array[ind], array[min_index]) = (array[min_index], array[ind])
    #return array

#list = selectionSort(list)
#print(list)

#i = 1
#values.remove(i) - no work
#del values[i] - yes work
#print(values)


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