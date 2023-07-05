import glob
import json
import tkinter as tk

root = tk.Tk()
root.state("zoomed")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

num1 = []
num2 = []
cnt = 0

connections = [
    (0, 1), (0, 15), (0, 16), (15, 17), (16, 18), #頭
    (2, 1), (2, 3), (3, 4), #右腕
    (1, 5), (5, 6), (6, 7), #左腕
    (8, 1), (8, 9), (8, 12), #腰・背骨
    (9, 10), (10, 11), (22, 11), (24, 11), (22, 23), #右足
    (12, 13), (14, 13), (21, 14), (19, 14), (20, 19) #左足
]

def move():
    global num1, cnt

    canvas.delete("all")
    
    if cnt < len(num1):
        keypoints1 = num1[cnt]
        keypoints2 = num2[cnt]
              
        for connection in connections:
            x1, y1 = keypoints1[connection[0] * 3], keypoints1[connection[0] * 3 + 1]
            x2, y2 = keypoints1[connection[1] * 3], keypoints1[connection[1] * 3 + 1]
            
            
            x3, y3 = keypoints2[connection[0] * 3], keypoints2[connection[0] * 3 + 1]
            x4, y4 = keypoints2[connection[1] * 3], keypoints2[connection[1] * 3 + 1]

            if x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0:
                canvas.create_line(x1, y1, x2, y2, fill="black", width=3)

            if x3 > 0 and x4 > 0 and y3 > 0 and y4 > 0:
                canvas.create_line(x3, y3, x4, y4, fill="black", width=3)

        cnt += 1

    canvas.after(100, move)


myfolder = glob.glob("./kabeposter/*")
for myfile in myfolder:
    with open(myfile, encoding='utf-8') as file:
        j = json.load(file)
        num1.append(j['people'][0]['pose_keypoints_2d'])
        num2.append(j['people'][1]['pose_keypoints_2d'])


move()
root.mainloop()