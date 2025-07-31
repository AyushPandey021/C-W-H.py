# loops
# for loop 

for i in range(0,1):
  print(i)
# while loop 
list = ["Ayush", "Akanksha", "Sakshi", "Dimple", "Aditi"]

while(i<len(list)):


  print(list[i])



  i += 1

  """ 
  output: 
  """
  # loop tuple
a = (9,1,7,4,1,9,4,4,8,0)


for i in a:

  print(i,"OK")




# loop  string
s = "SABKA MALIK EK H "

for i in s:
  print(i)




l  = [1,3,4,5,6,7,8,9]
for item in l:

  print(l)
  break

else:
  print("done") # this is printing exhausts


# breake and continue
for i in range(100):
  if i==35:
   break
  print(i)
print("break")
# continue
for i in range(100):
  if i==35:
   continue
  print(i)
print("Continue")



# pass statement 
# if you are working many project to you i not write code corrently 
# so use pass its ignore you incomplete funtion 

for i in range(42,345):
  pass

i = 34
while(i<45):
  print("Radhe Radhe ")
  