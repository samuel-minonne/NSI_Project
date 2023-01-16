list_wallHitboxes = [[0,0,8,8],[16,8,32,8]]


for h in list_wallHitboxes:
    x = list_wallHitboxes[h][0]
    y = list_wallHitboxes-[h][1]
    l = list_wallHitboxes[h][2]
    height = list_wallHitboxes[h][3]
    wallhitbox.appendHitbox(h[0],h[1],h[2],h[3])