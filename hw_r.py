def input(name):  
  s = ""
  for i in range(len(name)):
	if (i%2)==0:
	   s+=name[i]
  return s
name=raw_input("Enter name : ")
print("altenate characters are : ")
print(input(name))

