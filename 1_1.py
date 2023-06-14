
number1=[]
with open('data.txt',encoding='utf-8') as file:
  for number2 in file.readlines():
   try:
    y=int(number2)
   except ValueError:
    continue
    
   number1.append(y)
    
print(sum(number1))