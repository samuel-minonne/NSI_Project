import pyxel
import hitboxes
import gameobjects
import json

with open("./config.json") as json_file:# more Marko wizardy to open and read a json file
    config = dict(json.load(json_file))

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
        self.walls_hitboxes.append(hitboxes.Hitbox(112,16,8,64))
        
        self.enemies_list = []
        
        self.player = gameobjects.Player(0,0,self.walls_hitboxes)#The player
        
        
room = Room()
camera = gameobjects.Camera()
pyxel.init(config["game"]["width"], config["game"]["height"], title="Protoknight", fps= 60)

def update():
    room.player.update()
    room.player.movement()
    for e in room.enemies_list:
        e.update()
    camera.focusOn(room.player.xpos+4,room.player.ypos+4)

    if room.player.ypos > 250:
        room.player.hp = 0


def draw():
    pyxel.cls(0)
    pyxel.rect(camera.xOnScreen(room.player.xpos),camera.yOnScreen(room.player.ypos),room.player.length,room.player.height,3)
    if room.player.attacking:
        pyxel.rect(camera.xOnScreen(room.player.attack.xpos),camera.yOnScreen(room.player.attack.ypos),room.player.attack.length,room.player.attack.height,14)
    
    for i in range (len(room.walls_hitboxes)):
        pyxel.rect(camera.xOnScreen(room.walls_hitboxes[i].xpos),camera.yOnScreen(room.walls_hitboxes[i].ypos),room.walls_hitboxes[i].length,room.walls_hitboxes[i].height,4)
    
    if room.player.hp <= 0 :
        pyxel.cls(0)
        pyxel.text(config["game"]["width"]/2,config["game"]["height"]/2 ,"GAME OVER",7)
        pyxel.text(config["game"]["width"]/2,config["game"]["height"]/3 ,"you died",7)
pyxel.run(update, draw)
