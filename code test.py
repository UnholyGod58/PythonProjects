
#import os
import pygame

values = [["user", 1.4, 2.0], ["user2", 2.4, 3.6], ["user3", 3.1, 4.6]]
list = ["test11", "test223", "test3"]
string = "test 1space  2paces   3spaces"
user_in = 1

pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("test")


screen.fill((255, 255, 255))
test1 = pygame.rect.Rect(100, 100, 100, 100)
test2 = pygame.rect.Rect(200, 100, 100, 100)

pygame.display.update()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        if pygame.sprite.spritecollide(test1, test2, False):
            

#def binary_search(list, low, high, x):
#
#    if high >= low:
#
#        mid = (high + low) // 2
#
#        if list[mid] == x:
#            return mid
#
#        elif list[mid] > x:
#            return binary_search(list, low, mid - 1, x)
#
#        else:
#            return binary_search(list, mid + 1, high, x)
#
#    else:
#        return -1


#def selection_sort():
#    global list
#    for i in range(len(list)):
#        min_index = min(range(i, len(list)), key = list.__getitem__)
#        list[i], list[min_index] = list[min_index], list[i]

#print(list)

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