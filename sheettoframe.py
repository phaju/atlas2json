import cv2
import numpy
import json
import os

file = open("teen_atlas.json", "r")
json_data = file.read()
json_data = json.loads(json_data)

images = json_data["parts"]

sprite_sheet_data = cv2.imread(json_data["name"], cv2.IMREAD_UNCHANGED)

for image in images:
    x = int(image["xy"][0])
    y = int(image["xy"][1])
    w = int(image["size"][0])
    h = int(image["size"][1])

    if not os.path.exists("output"):
        os.mkdir("output")
    if "/" in image["name"]:
        dir = image["name"].split("/")[0]
        if not os.path.exists("output/" + dir):
            os.mkdir("output/" + dir)
    if image["rotate"] == "true":
        temp = h
        h = w
        w = temp
    img = sprite_sheet_data[y:y+h, x:x+w]

    cv2.imwrite("output/" + image["name"] + ".png", img)
    cv2.waitKey(0)
