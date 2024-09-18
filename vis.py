import matplotlib.pyplot as plt

color_labels = {
            0: ("void", "#000000"), 1: ("dirt", "#6c4014"), 3: ("grass", "#006600"), 4: ("trees", "#00ff00"),
            5: ("pole", "#009999"), 6: ("water", "#0080ff"), 7: ("sky", "#0000ff"), 8: ("vehicle", "#ffff00"),
            9: ("object", "#ff007f"), 10: ("asphalt", "#404040"), 12: ("building", "#ff0000"), 15: ("log", "#660000"),
            17: ("person", "#cc99ff"), 18: ("fence", "#6600cc"), 19: ("bush", "#ff99cc"), 23: ("concrete", "#aaaaaa"),
            27: ("barrier", "#2979FF"), 31: ("puddle", "#86ffef"), 33: ("mud", "#634222"), 34: ('rubble','#6e168a'),
            35: ("mulch", "#8000ff"), 36: ("gravel", "#808080")}

qt = [2,11,13,14,16,20,21,22,24,25,26,28,29,30,32][::-1]
classes = [color_labels[i][0] for i in range(37) if i not in qt]
colors = [color_labels[i][1] for i in range(37) if i not in qt]
id = [i for i in range(37) if i not in qt]

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create squares with text inside in 4 rows
rows = 4
cols = 6  # 6 classes per row

for i in range(len(classes)):
    row = i // cols
    col = i % cols
    square = plt.Rectangle((col, -row), 1, 1, color=colors[i])
    ax.add_patch(square)
    ax.text(col + 0.5, -row + 0.5, classes[i]+'('+str(id[i])+')', ha='center', va='center', fontsize=16, color='white')

# Set limits and remove axes
ax.set_xlim(0, cols)
ax.set_ylim(-rows, 1)
ax.axis('off')

# Show the plot
plt.title('Class Ontology')
plt.show()