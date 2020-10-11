# Array in Python

dit = ["Department", "Informatics", "Telecomunication"]

x = dit[0]
print (x)

dit[1] = "UOI"
y = dit[1]
print (y)

x = len(dit)   # Return the number of elements 

dit.append("department")     # Add one more element 
r = dit[3]
print (r)

dit.pop(3)    # You can use the pop() method to remove an element from the array

print("----------------------")
for q in dit:
    print (q)

dit.remove("UOI")  # You can also use the remove() method to remove an element from the array