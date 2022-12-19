import pyxel
import hitboxes
import gameobjects
import json

class Room:
    """A room, handles the running of the actual game"""
    def __init__(self) -> None:
        """Creates a Room"""
        self.player = gameobjects.Player(0,0)#The player
        self.walls_hitboxes = [] #All the hitboxes of the walls
        
room = Room()
pyxel.init(128, 128, title="Protoknight", fps= 60)

def update():
    room.player.update()
    
def draw():
    pyxel.cls(0)
    pyxel.rect(room.player.xpos,room.player.ypos,room.player.length,room.player.height,3)
    
pyxel.run(update, draw)
