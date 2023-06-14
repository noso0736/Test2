import glob

number1=[]
myfolder=glob.glob("./sample/*[13579]_kgu.txt")
for myfile in myfolder:
  with open(myfile,encoding='utf-8')as file:
     try:
      y=int(file.readline()) 
      number1.append(y)
     except ValueError:
      continue
    
print(sum(number1))
