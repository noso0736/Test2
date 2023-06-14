import json
stt=[]
with open ('catalog.json',encoding="utf-8") as file:
 number=json.load(file)
for  number1 in number:
        try:
         if number1["name"]=="jacket":
          number2=int(number1["price"])
          stt.append(number2)
        except ValueError:
         continue 
        
print(len(stt))       
print(max(stt))
print(min(stt))




