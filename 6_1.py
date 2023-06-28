import glob
import json

myfolder=glob.glob("./kabeposter/*000000000000_keypoints.json")
for myfile in myfolder:
 with open(myfile,encoding='utf-8')as file:
     number=json.load(file)
     print(number["people"][0]["pose_keypoints_2d"][0])
     print(number["people"][0]["pose_keypoints_2d"][1])
     print(number["people"][0]["pose_keypoints_2d"][2])
     print(number["people"][0]["pose_keypoints_2d"][3])
     print(number["people"][0]["pose_keypoints_2d"][4])
     print(number["people"][0]["pose_keypoints_2d"][5])
     print(number["people"][1]["pose_keypoints_2d"][0])
     print(number["people"][1]["pose_keypoints_2d"][1])
     print(number["people"][1]["pose_keypoints_2d"][2])
     print(number["people"][1]["pose_keypoints_2d"][3])
     print(number["people"][1]["pose_keypoints_2d"][4])
     print(number["people"][1]["pose_keypoints_2d"][5])
   

