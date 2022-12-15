"""
A module that handles the gameobjects for a pyxel game
"""
import pyxel
import hitboxes
import math

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
    A Gameobject that can move: inherits the properties of the Gameobject class, and adds a x and y speed and  move method"""
    def __init__(self,x,y,l,h,speedx = 0,speedy = 0):
        """Creates an entity with x and y as coordinates and l and h as length and height and a hitbox.
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
        self.xspeed = speedx
        self.yspeed = speedy

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


class Player(Entity):
    """
    A player: inherits the properties of the Entity class and adds way too much stuff (someone pls write a propper desciption)
    """
    def __init__(self,x,y):
        """Creates a Player with x and y as coordinates and l and h as length and height and a hitbox.
        """
        assert type(x) == int or type(x) == float, "x must be a number"
        assert type(y) == int or type(y) == float, "y must be a number"
        assert type(l) == int or type(l) == float, "l must be a number"
        assert type(h) == int or type(h) == float, "h must be a number"

        self.xpos = x
        self.ypos = y
        self.length = 8
        self.height = 8
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.length,self.height)
        self.xspeed = speedx
        self.yspeed = speedy

        self.hp = 5
        self.upgrades = [True,True,True,True,True] #a list of bool
        self.touches_ground = True

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbos = True)
