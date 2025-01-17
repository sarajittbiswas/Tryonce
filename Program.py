marks={}
marks1={23,45,67,78,0}
marks[0]=10
marks[1]=20
marks[2]=30
print(type(marks1))
print(type(marks))
marks2=[12,12,14,51,6,19]
marks3=(23,0,6,45,"chal",2.3)
marks[marks2[0]]=1000
marks[marks2[2]]="my name is python"
print(marks[12])
print(marks[14])
print(marks[0])
print(marks2[3])
print(marks3[4])
print("\n")
print("\n")
print("\n")
str1="Sarajit"
print(str1[2:])
marks2.append(20)  #append() is used for inserting element in the last index of a list
print(marks2)
print(marks2.sort())
print(marks2)
print(marks2.append(10)) 
marks2.sort()  #sort() is used for sorting in ascending order eg. 1 2 3 4 
print(marks2)
marks2.sort(reverse=True)  #sort(reverse=True) for sorting in descending order eg. 4 3 2 1 
print(marks2)
print(marks2.reverse())  #reverse() is used to reverse the elements of a list
print(marks2)
marks2.insert(2,99)  #insert() is used to insert element in a particular index eg. ele "99" is inserted in marks2[2] index in the list
print(marks2)
marks2.remove(12) #remove() is used to remove the occurence/ duplicate of element 
print(marks2)
marks2.pop(2) #pop() is used to delete element in a particular index
print(marks2)
print(marks2.index(12))  #index() is used to see the indexing of an element
marks2.append(12)
print(marks2)
print(marks2.count(12))  #count() is used for counting occurence of a particular element stored in a list,tuple, dict etc.

"""Write a program to take input from your friends of thier favorite movies and store themin a list the print the list"""

movies=[]
movies.append(input("enetr a movie:\n"))
movies.append(input("enetr a movie:\n"))
movies.append(input("enetr a movie:\n"))
print(movies)


'''TRY THE ABOVE PROGRAM IN DIFFERENT WAY USING LOOP'''

mov=[]
i=0 
for i in range(0,3):
  mov.append(input("enter a movie name:\n"))
  i=i+1
#print(mov)
for i in range(0,3):
  print(mov[i])
  i=i+1