import json

with open("./testroom.json") as json_file:
    testroom = dict(json.load(json_file))

x =[0,0]
y =[0,0]
tuples =[x,y]
texturesID = [tuples]
for i in range(1023):
    x[0] += 8
    if x[0] == 256:
        x[0] = 0
        x[1] += 8
    
for j in range(3):
    if j == 1:
        y[0] -= 1
    if j == 2:
        y[1] -= 1
    if j == 3:
        y[0] -= 1
        y[1] -= 1

print(texturesID)

