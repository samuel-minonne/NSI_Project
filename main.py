import pyxel
import hitboxes
import gameobjects
import json

class Room:
    """A room, handles the running of the actual game"""
    def __init__(self) -> None:
        """Creates a Room"""
        self.walls_hitboxes = [] #All the hitboxes of the walls
        self.walls_hitboxes.append(hitboxes.Hitbox(8,80,72,8))
        self.walls_hitboxes.append(hitboxes.Hitbox(64,72,8,8))
        self.walls_hitboxes.append(hitboxes.Hitbox(88,72,8,8))
        self.walls_hitboxes.append(hitboxes.Hitbox(8,64,8,8))
        self.walls_hitboxes.append(hitboxes.Hitbox(0,56,8,8))
        self.walls_hitboxes.append(hitboxes.Hitbox(32,64,8,8))
        
        self.player = gameobjects.Player(0,0,self.walls_hitboxes)#The player
        
        
room = Room()
pyxel.init(128, 128, title="Protoknight", fps= 60)

def update():
    room.player.update()
    room.player.movement()
    
def draw():
    pyxel.cls(0)
    pyxel.rect(room.player.xpos,room.player.ypos,room.player.length,room.player.height,3)
    if room.player.is_attacking:
        pyxel.rect(room.player.attack.xpos,room.player.attack.ypos,room.player.attack.length,room.player.attack.height,14)
    
    for i in range (len(room.walls_hitboxes)):
        pyxel.rect(room.walls_hitboxes[i].xpos,room.walls_hitboxes[i].ypos,room.walls_hitboxes[i].length,room.walls_hitboxes[i].height,4)
    
pyxel.run(update, draw)
