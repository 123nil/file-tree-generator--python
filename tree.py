import os
path = r"C:\xampp\htdocs\treepy"
l = os.listdir(path)
print(l)
for root, dirs, files in os.walk(path):
    for f in files:
        print(os.path.join(root, f))

