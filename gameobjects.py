"""
A module that handles the gameobjects for a pyxel game
"""
import pyxel
import hitboxes

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
        assert type(x) = int or type(x) = float, "x must be a number"
        assert type(y) = int or type(y) = float, "y must be a number"
        assert type(l) = int or type(l) = float, "l must be a number"
        assert type(h) = int or type(h) = float, "h must be a number"
        
        self.xpos = x
        self.ypos = y
        self.length = l
        self.height = h
        self.hitbox = hitboxes.Hitbox(self.xpos,self.ypos,self.length,self.height)
        
        
class Player:
    """A player"""
        
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbos = True)