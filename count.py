import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
files = os.listdir('/media/usl/NV/GOD/00000/pylon_camera_node_label_id')
count = np.zeros(37, dtype=int)
color_labels = {
            0: ("void", "#000000"), 1: ("dirt", "#6c4014"), 3: ("grass", "#006600"), 4: ("trees", "#00ff00"),
            5: ("pole", "#009999"), 6: ("water", "#0080ff"), 7: ("sky", "#0000ff"), 8: ("vehicle", "#ffff00"),
            9: ("object", "#ff007f"), 10: ("asphalt", "#404040"), 12: ("build", "#ff0000"), 15: ("log", "#660000"),
            17: ("person", "#cc99ff"), 18: ("fence", "#6600cc"), 19: ("bush", "#ff99cc"), 23: ("concrete", "#aaaaaa"),
            27: ("barrier", "#2979FF"), 31: ("puddle", "#86ffef"), 33: ("mud", "#634222"), 34: ('rubble','#6e168a'),
            35: ("mulch", "#8000ff"), 36: ("gravel", "#808080")}
for i in tqdm(files, total=len(files)):
    file = cv2.imread('/media/usl/NV/GOD/00000/pylon_camera_node_label_id/'+i,0)
    unique, counts = np.unique(file, return_counts=True)
    for i in range(len(unique)):
        count[unique[i]] += counts[i]
qt = [2,11,13,14,16,20,21,22,24,25,26,28,29,30,32][::-1]


count = list(count)
for i in qt:
    count.pop(i)

color=[color_labels[i][1] for i in range(37) if i not in qt]
label=[color_labels[i][0] for i in range(37) if i not in qt]
pair_list = list(zip(count,color,label))
pair_list.sort(reverse=True)
count = [i[0] for i in pair_list]
color = [i[1] for i in pair_list]
label = [i[2] for i in pair_list]
plt.bar(label,count,color=color)
plt.show()