import pyxel
import hitboxes
import gameobjects
import enemies
import json

#Samuel todo list: make it so that the attack only does dmg, not 10xdmg and fix the dash bug with the new collisions
#make it so that the corretions applies the the closest edge of the hitbox we are touching # Doesn't work in all cases, gonna have to find something else(probably speed related)
#ne deplacer la camera que si on depasse une certaine coordonne pour eviter de bouger la cam avec des petits mouvements

with open("./config.json") as json_file:# more Marko wizardy to open and read a json file
    config = dict(json.load(json_file))


class Room:
    """A room, runs the actual game"""
    def __init__(self) -> None:
        """Creates a Room"""
        self.walls_hitboxes = [] #All the hitboxes of the walls
        #self.walls_hitboxes.append(hitboxes.Hitbox(8,80,72,8))
        #self.walls_hitboxes.append(hitboxes.Hitbox(48,72,9,8))
        #self.walls_hitboxes.append(hitboxes.Hitbox(80,72,8,8))
        #self.walls_hitboxes.append(hitboxes.Hitbox(8,64,8,8))
        #self.walls_hitboxes.append(hitboxes.Hitbox(0,56,8,8))
        #self.walls_hitboxes.append(hitboxes.Hitbox(32,64,8,8))
        #self.walls_hitboxes.append(hitboxes.Hitbox(112,16,8,64))
        #self.walls_hitboxes.append(hitboxes.Hitbox(32,104,48,8))

        self.load_hitboxes("./room1.json")

        self.walls_textures = []
        self.load_textures("./room1.json")
        
        self.enemies_list=[]
        self.enemies_list.append(enemies.Test_enemy(5,8,self.walls_hitboxes))
        self.enemies_list.append(enemies.Bat(32,16,self.walls_hitboxes))


        self.items_list = []
        #self.items_list.append(gameobjects.Item(16,16,"dash",0))
        self.load_items("./testroom.json")
        
        self.player = gameobjects.Player(0,-50,self.walls_hitboxes,self.items_list)#The player
    
    def load_hitboxes(self,filepath:str):
        '''Creates the hitboxes from a room file'''
        with open(filepath) as json_file:
            file = dict(json.load(json_file))
        hitboxes_list = file['hitboxes']
        for l in hitboxes_list:
            self.walls_hitboxes.append(hitboxes.Hitbox(*l))

    def load_textures(self,filepath:str):
        """Creates the textures with the room file"""
        with open(filepath) as json_file:
            file = dict(json.load(json_file))
        textures = file["textures"]
        for i in range(len(textures)):
            self.walls_textures.append([textures[i][0],textures[i][1],0,textures[i][2]*8,textures[i][2]//256,8*self.rotid_to_fw(textures[i][3]),8*self.rotid_to_fh(textures[i][3])])

    def load_items(self,filepath:str):
        '''Creates the items from a room file'''
        with open(filepath) as json_file:
            file = dict(json.load(json_file))
        items = file['items']
        for i in items:
            self.items_list.append(gameobjects.Item(*i))

    def rotid_to_fw(rotid,arg2):
        if rotid == 0:
            fw = -1
        else:
            fw = 1
        return fw

    def rotid_to_fh(rotid,arg2):
        if rotid == 0:
            fh = -1
        else:
            fh = 1
        return fh
        
        
room = Room()
camera = gameobjects.Camera()
pyxel.init(config["game"]["width"], config["game"]["height"], title="Protoknight", fps= 60, display_scale=5)
pyxel.load("res.pyxres")


def update():
    room.player.movement()
    room.player.update()
    room.player.combat(room.enemies_list)
    camera.focusOn(room.player.xpos+4,room.player.ypos+4)
    #print(room.player.xpos)
    if len(room.enemies_list)>0:
        print(room.enemies_list[0].hp)
    else:
        print("he's dead")

    print(room.player.upgrades)

    for e in room.enemies_list:
        if e.hp > 0:
            e.update()
            e.mouvement(room.player)
        else:
            room.enemies_list.remove(e)
    
    if room.player.ypos > 250:
        room.player.hp = 0


def draw():
    pyxel.cls(0)

    pyxel.text(config["game"]["width"]/10,config["game"]["height"]/10, "lives:",7)
    pyxel.text(config["game"]["width"]/10 + 25,config["game"]["height"]/10 , format(room.player.hp),7)

    
    for i in range (len(room.walls_hitboxes)):
        pyxel.rect(camera.xOnScreen(room.walls_hitboxes[i].xpos),camera.yOnScreen(room.walls_hitboxes[i].ypos),room.walls_hitboxes[i].length,room.walls_hitboxes[i].height,4)

    for w  in range(len(room.walls_textures)):
        pyxel.blt(camera.xOnScreen(room.walls_textures[w][0]),camera.yOnScreen(room.walls_textures[w][1]),room.walls_textures[w][2],room.walls_textures[w][3],room.walls_textures[w][4],room.walls_textures[w][5],room.walls_textures[w][6])

    for i in range (len(room.enemies_list)):
        pyxel.rect(camera.xOnScreen(room.enemies_list[i].xpos),camera.yOnScreen(room.enemies_list[i].ypos),room.enemies_list[i].length,room.enemies_list[i].height,2)
        
    for w  in room.walls_hitboxes:
        pyxel.blt(camera.xOnScreen(w.xpos),camera.yOnScreen(w.ypos),0,8,0,8,8)

    for i in room.items_list:
        i.draw(camera.xOnScreen(i.xpos),camera.yOnScreen(i.ypos))
    
    room.player.draw(camera.xOnScreen(room.player.xpos),camera.yOnScreen(room.player.ypos))

        
    if room.player.hp <= 0:
        pyxel.cls(0)
        pyxel.text(config["game"]["width"]/2,config["game"]["height"]/2 ,"GAME OVER",7)
        pyxel.text(config["game"]["width"]/2,config["game"]["height"]/3 ,"you died",7)
    
pyxel.run(update, draw)
