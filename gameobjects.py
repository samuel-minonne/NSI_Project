"""
A module that handles the gameobjects for a pyxel game. Has a Gameobject class, an Entity class, an Attack class and a Player class (that we should put somewhere else)
"""
import pyxel
import hitboxes
import json
import math

with open("./config.json") as json_file:# more Marko wizardy to open and read a json file
    config = dict(json.load(json_file))
with open("./controls.json") as json_file:# more Marko wizardy to open and read a json file
    controls = dict(json.load(json_file))

class Gameobject:
    """The base gameobject class, has x and y as coordinates, a length l and a height h and a Hitbox"""
    def __init__(self,x,y,l,h):
        """Creates a gameobject with x and y as coordinates and l and h as length and height and a hitbox.
        
        >>>testobject = Gameobject(0,4,8,16)
        testobject.xpos = 0
        testobject.ypos = 4
        testobject.length = 8
        testobject.height = 16
        type(testobject.hitbox) = Hitbox
        
        >>>testobject = Gameobject(-1,-4,8,16)
        testobject.xpos = -1
        testobject.ypos = -4
        testobject.length = 8
        testobject.height = 16
        type(testobject.hitbox) = Hitbox
        """
        assert type(x) == int or type(x) == float, "x must be a number"
        assert type(y) == int or type(y) == float, "y must be a number"
        assert type(l) == int or type(l) == float, "l must be a number"
        assert type(h) == int or type(h) == float, "h must be a number"

        self.xpos = x
        self.ypos = y
        self.length = l
        self.height = h
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.length,self.height)


class Entity(Gameobject):
    """
    A Gameobject that can move and has hp: inherits the properties of the Gameobject class, and adds a x and y speed and  move method"""
    def __init__(self,x,y,l,h,hp,walls_list:list,speedx = 0.0,speedy = 0.0):
        super().__init__(x,y,l,h)
        """
        Creates an entity with x and y as coordinates and l and h as length and height and a hitbox.
        """
        assert type(hp) == int, "hp must be an int"

        self.xspeed = speedx
        self.yspeed = speedy
        self.walls_list = walls_list
        self.touches_up = False
        self.touches_down = False
        self.touches_left = False
        self.touches_right = False
        self.hp = hp
        


    def update(self):
        """
        Updates the entity (position, hp,...). MUST be executed once per frame.
        """
        self.touches_up = False
        self.touches_down = False
        self.touches_left = False
        self.touches_right = False
        for hb in self.walls_list:
            collision_status = hitboxes.doHitboxesTouch(self.hitbox,hb)
            if collision_status == ['y','-']:
                self.touches_down = True
            elif collision_status == ['x','+']:
                self.touches_right = True
            elif collision_status == ['x','-']:
                self.touches_left = True
            elif collision_status == ['y','+']:
                self.touches_up = True
                
        if self.xspeed > 0: #si on va vers la droite
            if self.touches_right: #et qu'on touche à droite on s'arrête
                self.xspeed = 0
            else:
                self.xpos += self.xspeed #sinon (si on touche pas) on se déplace de xspeed
        elif self.xspeed < 0:
            if self.touches_left:#même chose pour la gauche
                self.xspeed = 0
            else:
                self.xpos += self.xspeed
        if self.yspeed > 0: #même chose pour l'axe y
            if self.touches_down:
                self.yspeed = 0
            else:
                self.ypos += self.yspeed
        elif self.yspeed < 0:
            if self.touches_up:
                self.yspeed = 0
            else:
                self.ypos += self.yspeed
        self.hitbox.moveTo(round(self.xpos),round(self.ypos))
        
        
    def update_walls_list(self,walls_list):
        self.walls_list = walls_list
            
    def moveTo(self,x,y):
        """
        Moves the entity to the specified coordinates
        Ajouter tests
        """

        assert type(x) == int or type(x) == float, "x must be a number"
        assert type(y) == int or type(y) == float, "y must be a number"

        self.xpos = x
        self.ypos = y
        self.hitbox.moveTo(x,y)

    def set_xspeed(self,speed):
        """
        Sets the xspeed to the specified value
        """
        assert type(speed) == int or type(speed) == float, "speed must be a number"

        self.xspeed = speed

    def set_yspeed(self,speed):
        """
        Sets the yspeed to the specified value
        """
        assert type(speed) == int or type(speed) == float, "speed must be a number"

        self.yspeed = speed

    def setSpeedWithAngle(angle,speed):
        """
        Sets the xspeed and yspeed values based on a speed and an angle
        """

    def moveWithSpeed(self):
        """
        Moves the entity with its xspeed and yspeed
        """

class Attack(hitboxes.Hitbox):
    """An Attack, a child of the Hitbox class with a duration, a damage and a list of entities that have been hit"""
    def __init__(self, x, y, l, h, dmg, duration:int,xoffset = 0,yoffset = 0):
        super().__init__(x, y, l, h,)
        """Creates an attack"""
        self.dmg = dmg #the dammage dealt by the attack
        self.timer = duration #for how long the attack will stay on screen
        self.entities_hit = [] #all the entites that have been hit by the attack
        self.xoffset = xoffset
        self.yoffset = yoffset
        
    def update(self):
        self.timer -= 1
        
    def moveTo(self,x,y):
        """Moves the hitbox to the specified coordinates"""
        assert type(x) == int or type(x) == float, "x must be a number"
        assert type(y) == int or type(y) == float, "y must be a number"
        
        self.xpos = x + self.xoffset
        self.ypos = y + self.yoffset
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.length
        
        
class Player(Entity):
    """
    A player: inherits the properties of the Entity class and adds way too much stuff (someone pls write a propper desciption)
    """
    def __init__(self,x,y,walls_list,speedx = 0,speedy = 0,facing_right = True):
        super().__init__(x,y,8,8,5,walls_list)#mettre les valeur manuellement
        """Creates a Player with x and y as coordinates and l and h as length and height and a hitbox.
        """
        self.config = config["player"]
        self.upgrades = [True,True,True,True,True] #a list of bool
        
        self.facing_right = facing_right
        self.vertical_direction = 1 #0 is facing up, 1 horizontally and 2 is facing down 
        
        self.attacking = False

        self.can_doublejump = True
        self.dashing = False
        self.dash_timer = 0
        self.can_dash = True
    
    def movement(self):
        """Reads the imputs and chages the speed and movement status values accordingly"""
        
        if pyxel.btn(pyxel.KEY_D) and not pyxel.btn(pyxel.KEY_Q):
            self.facing_right = True
        if pyxel.btn(pyxel.KEY_Q) and not pyxel.btn(pyxel.KEY_D):
            self.facing_right = False
        
        if pyxel.btn(pyxel.KEY_Z) and pyxel.btn(pyxel.KEY_S):
            self.vertical_direction = 1 #0 is facing up, 1 horizontally and 2 is facing down 
        elif pyxel.btn(pyxel.KEY_Z):
            self.vertical_direction = 0
        elif pyxel.btn(pyxel.KEY_S):
            self.vertical_direction = 2
        else:
            self.vertical_direction = 1
            
        self.dash_timer -= 1
        if self.dash_timer < 0:
            self.dashing = False
            
        if not self.dashing: 
            if self.touches_down: #resets the dash and doublejump if the player touches the floor
                self.can_dash = True 
                self.can_doublejump = True  
            #movement sur l'axe x
            if pyxel.btn(pyxel.KEY_Q) and self.xspeed > -self.config["movement"]["max_speed"]:
                self.xspeed -= self.config["movement"]["speed_increment"]
            elif self.xspeed < 0: 
                self.xspeed += self.config["movement"]["ground_drag"]
                if self.xspeed > 0: #évite de dépasser 0
                    self.xspeed = 0
            if pyxel.btn(pyxel.KEY_D) and self.xspeed < self.config["movement"]["max_speed"]:
                self.xspeed += self.config["movement"]["speed_increment"]
            elif self.xspeed > 0:
                self.xspeed -= self.config["movement"]["ground_drag"]
                if self.xspeed < 0: #évite de dépasser 0
                    self.xspeed = 0
            #movement sur l'axe y
            if self.yspeed < self.config["movement"]["max_falling_speed"]:
                self.yspeed += self.config["movement"]["gravity"]
                if self.yspeed > self.config["movement"]["max_falling_speed"]:#pour éviter de dépasser la max falling speed
                    self.yspeed = self.config["movement"]["max_falling_speed"]
            
            #all the types of jumps
            if pyxel.btn(pyxel.KEY_SPACE) and self.touches_down: #normal jumps
                self.yspeed = -1   
            elif self.touches_right and pyxel.btnp(pyxel.KEY_SPACE): #temporary stuff for the walljumps
                self.yspeed = -1
                self.xspeed -= 1
            elif self.touches_left and pyxel.btnp(pyxel.KEY_SPACE): #walls jumps the other way
                self.yspeed = -1
                self.xspeed += 1
            elif pyxel.btnp(pyxel.KEY_SPACE) and self.can_doublejump: #double jumps
                self.yspeed = -1
                self.can_doublejump = False
            
        if pyxel.btnp(pyxel.KEY_KP_2) and self.can_dash: #temporary stuff for the dash
            if self.facing_right:
                self.yspeed = 0
                self.xspeed = 2
                self.can_dash = False
                self.dashing = True
                self.dash_timer = self.config["movement"]["dash_time"]
            else:
                self.yspeed = 0
                self.xspeed = -2
                self.can_dash = False
                self.dashing = True
                self.dash_timer = self.config["movement"]["dash_time"]
        
    def combat(self):
        """very temporary"""
        if pyxel.btnp(pyxel.KEY_KP_1) and not self.attacking: #quand le boutton d'attaque est pressé
            if self.vertical_direction == 1: #si on regarde horizontalement
                if self.facing_right: #on vérifie de quel côté on regarde et on attaque de ce côté là
                    self.attack = Attack(self.xpos,self.ypos,8,8,self.config["combat"]["damage"],self.config["combat"]["attack_time"], xoffset = self.length)
                    self.attacking = True
                else:
                    self.attack = Attack(self.xpos,self.ypos,8,8,self.config["combat"]["damage"],self.config["combat"]["attack_time"], xoffset = -self.length)
                    self.attacking = True
            elif self.vertical_direction < 1: #si on regarde en haut on attaque en haut
                self.attack = Attack(self.xpos,self.ypos,8,8,self.config["combat"]["damage"],self.config["combat"]["attack_time"],yoffset = -self.height)
                self.attacking = True
            elif self.vertical_direction > 1: #si on regarde en bas on attaque en bas
                self.attack = Attack(self.xpos,self.ypos,8,8,self.config["combat"]["damage"],self.config["combat"]["attack_time"],yoffset = self.height)
                self.attacking = True
            
        if self.attacking:
            self.attack.update()
            self.attack.moveTo(round(self.xpos),round(self.ypos))
            if self.attack.timer < 0:
                self.attacking = False
                
class Camera():
    """A class that handles the movement of the camera. xoffset and yoffset are the values by which we offset the drawings on the screen"""
    def __init__(self,xoffset = 0, yoffset = 0):
        self.xoffset = xoffset
        self.yoffset = yoffset
        
    def xOnScreen(self,x):
        """Returns the x coordinate on screen of an actual x coordinate in game"""
        return x-self.xoffset
    
    def yOnScreen(self,y):
        """Returns the y coordinate on screen of an actual y coordinate in game"""
        return y-self.yoffset
    
    def setCameraX(self,x):
        """Sets the xoffset to the specified value"""
        self.xoffset = x
        
    def setCameraY(self,y):
        """Sets the yoffset to the specified value"""
        self.xoffset = y
        
    def focusOn(self,x,y):
        """Centers the camera on the specified coordinates"""
        self.xoffset = x - config["game"]["width"]/2
        self.yoffset = y - config["game"]["height"]/2
        
        
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbos = True)

print(pyxel.__dict__["KEY_A"])# very useful Marko wizardry (gets the int of the KEY_A (because it's an int for some reason and pyxel uses an int))
