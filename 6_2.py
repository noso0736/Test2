import glob
import json
import tkinter as tk

root=tk.Tk()
root.geometry("1500x1500")

canvas=tk.Canvas(root,bg="white")

canvas.pack(fill=tk.BOTH,expand=True)

myfolder=glob.glob("./kabeposter/*00_keypoints.json")
for myfile in myfolder:
 with open(myfile,encoding='utf-8')as file:
     number=json.load(file)
     l=float(number["people"][0]["pose_keypoints_2d"][3])
     l1=float(number["people"][0]["pose_keypoints_2d"][4])
     l2=float(number["people"][0]["pose_keypoints_2d"][6])
     l3=float(number["people"][0]["pose_keypoints_2d"][7])
     l4=float(number["people"][0]["pose_keypoints_2d"][15])
     l5=float(number["people"][0]["pose_keypoints_2d"][16])
     
     l6=float(number["people"][1]["pose_keypoints_2d"][3])
     l7=float(number["people"][1]["pose_keypoints_2d"][4])
     l8=float(number["people"][1]["pose_keypoints_2d"][6])
     l9=float(number["people"][1]["pose_keypoints_2d"][7])
     l10=float(number["people"][1]["pose_keypoints_2d"][15])
     l11=float(number["people"][1]["pose_keypoints_2d"][16])
     
     canvas.create_line(l,l1,l2,l3,width=3)
     canvas.create_line(l,l1,l4,l5,width=3)
     
     canvas.create_line(l6,l7,l8,l9,width=3)
     canvas.create_line(l6,l7,l10,l11,width=3)
     

root.mainloop()