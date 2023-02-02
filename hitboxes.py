"""
A module that handles hitboxes for pyxel.
Has a Hitbox class, a doHitboxesCollide method and a doHitboxesTouch method
"""

import pyxel

class Hitbox:
    """A hitbox with x and y coordinates, a length l and a height h"""
    def __init__(self,x,y,l,h):
        """
        Creates an object of the Hitbox class
        
        >>>testbox = Hitbox(0,4,8,16)
        testbox.xpos = 0
        testbox.ypos = 4
        testbox.length = 8
        testbox.height = 16
        testbox.top = 0
        testbox.bottom = 16
        testbox.left = 4
        testbox.right = 12
        
        >>>testbox = Hitbox(2.0,6.4,9.8,5.2)
        testbox.xpos = 2.0
        testbox.ypos = 6.4
        testbox.length = 9.8
        testbox.height = 5.2
        testbox.top = 6.4
        testbox.bottom = 11.6
        testbox.left = 2.0
        testbox.right = 11.8
        
        >>>testbox = Hitbox(-1,-4,8,16)
        testbox.xpos = -1
        testbox.ypos = -4
        testbox.length = 8
        testbox.height = 16
        testbox.top = -4
        testbox.bottom = 12
        testbox.left = -1
        testbox.right = 7
        
        >>>testbox = Hitbox(-1.0,-4.,8.,16.)
        testbox.xpos = -1.0
        testbox.ypos = -4.0
        testbox.length = 8.0
        testbox.height = 16.0
        testbox.top = -4.0
        testbox.bottom = 12.
        testbox.left = -1.0
        testbox.right = 7.0
        
        >>>testbox = Hitbox(-1,-4,-8,16)
        AssertionError: l must be > 0
        
        >>>testbox = Hitbox(-1,-4,8,-16)
        AssertionError: h must be > 0
        
        >>>testbox = Hitbox(2.0,6.4,9.8,5.2)
        testbox.xpos = 2.0
        testbox.ypos = 6.4
        testbox.length = 9.8
        testbox.height = 5.2
        testbox.top = 6.4
        testbox.bottom = 11.6
        testbox.left = 2.0
        testbox.right = 11.8
        
        >>>testbox = Hitbox('6',6,12,2)
        AssertionError: x must be a number
        
        >>>testbox = Hitbox(6,'6',12,2)
        AssertionError : y must be a number
        
        >>>testbox = Hitbox(6,6,'12',2)
        AssertionError: l must be a number
        
        >>>testbox = Hitbox(6,6,12,'2')
        AssertionError : h must be a number
        """
        assert type(x) == int or type(x) == float, "x must be a number"
        assert type(y) == int or type(y) == float, "y must be a number"
        assert type(l) == int or type(l) == float, "l must be a number"
        assert type(h) == int or type(h) == float, "h must be a number"
        assert l > 0,"l must be > 0"
        assert h > 0,"h must be > 0"
        
        self.xpos = x
        self.ypos = y
        self.length = l
        self.height = h
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.length
        
    def moveTo(self,x,y):
        """Moves the hitbox to the specified coordinates
        
        >>>testbox = Hitbox(0,4,8,16)
        >>>testbox.moveTo(1,5)
        testbox.xpos = 1
        testbox.ypos = 5
        testbox.top = 5
        testbox.bottom = 21
        testbox.left = 1
        testbox.right = 9
        
        >>>testbox = Hitbox(0.0,4.0,8.0,16.0)
        >>>testbox.moveTo(1.0,5.0)
        testbox.xpos = 1.0
        testbox.ypos = 5.0
        testbox.top = 5.0
        testbox.bottom = 21.0
        testbox.left = 1.0
        testbox.right = 9.0
        
        >>>testbox = Hitbox(0,-4,8,16)
        >>>testbox.moveTo(1,-3)
        testbox.xpos = 1
        testbox.ypos = -3
        testbox.top = -3
        testbox.bottom = 13 
        testbox.left = 1
        testbox.right = 9
        
        >>>testbox = Hitbox(-2,4,8,16)
        >>>testbox.moveTo(-1,5)
        testbox.xpos = -1
        testbox.ypos = 5
        testbox.top = 5
        testbox.bottom = 21
        testbox.left = -1
        testbox.right = 7
        
        >>>testbox = Hitbox(0.0,-4.0,8.0,16.0)
        >>>testbox.moveTo(1.0,-3.0)
        testbox.xpos = 1.0
        testbox.ypos = -3.0
        testbox.top = -3.0
        testbox.bottom = 13.0
        testbox.left = 1.0
        testbox.right = 9.0
        
        >>>testbox = Hitbox(-2.0,4.0,8.0,16.0)
        >>>testbox.moveTo(-1.0,5.0)
        testbox.xpos = -1.0
        testbox.ypos = 5.0
        testbox.top = 5.0
        testbox.bottom = 21.0
        testbox.left = -1.0
        testbox.right = 7.0
        
        >>>testbox = Hitbox(-2.0,4.0,8.0,16.0)
        >>>testbox.moveTo('-1.0',5.0)
        AssertionError: x must be a number
        
        >>>testbox = Hitbox(-2.0,4.0,8.0,16.0)
        >>>testbox.moveTo(-1.0,'5.0')
        AssertionError: y must be a number
        """
        assert type(x) == int or type(x) == float, "x must be a number"
        assert type(y) == int or type(y) == float, "y must be a number"
        
        self.xpos = x
        self.ypos = y
        self.top = self.ypos
        self.bottom = self.ypos + self.height
        self.left = self.xpos
        self.right = self.xpos + self.length
        
    def is_point_in(self, x, y):
        """
        Checks if the point with the specified coordinates is strictly in the hitbox.
        Takes x and y as parameters, the x and y coordinates od the point
        """
        
        if x>=self.left and x<=self.right and y>=self.top and y<=self.bottom:
            return True
        else:
            return False 
        
def doHitboxesCollide(hitbox1:Hitbox,hitbox2:Hitbox):
    """Checks if 2 hitboxes collide, takes two hitboxes as parameters, returns True if they collide and False if they don't"""
    if ((hitbox1.bottom>=hitbox2.top and hitbox1.bottom<=hitbox2.bottom) or (hitbox1.top>=hitbox2.top and hitbox1.top<=hitbox2.bottom)) and ((hitbox1.left>=hitbox2.left and hitbox1.left<=hitbox2.right ) or (hitbox1.right>=hitbox2.left and hitbox1.right<=hitbox2.right)):
        return True
    else:
        return False
    
def doHitboxesTouch(hitbox1:Hitbox,hitbox2:Hitbox):
    """takes two hitboxes as inputs and checks if they are touching, 
    returns a tuple of str containig ['f','f'] if not, ['x','+'] if hitbox1 is left of hitbox2, ['x','-'] if hitbox1 is left of hitbox2, 
    ['y','+'] if hitbox1 is under hitbox2, ['y','-'] if hitbox1 is above hitbox2 and ['o','o'] if they overlap"""
    if hitbox1.bottom==hitbox2.top and ((hitbox1.left>=hitbox2.left and hitbox1.left<=hitbox2.right ) or (hitbox1.right>=hitbox2.left and hitbox1.right<=hitbox2.right)):
        return ['y','-']
    elif hitbox1.top==hitbox2.bottom and ((hitbox1.left>=hitbox2.left and hitbox1.left<=hitbox2.right ) or (hitbox1.right>=hitbox2.left and hitbox1.right<=hitbox2.right)):
        return ['y','+']
    elif hitbox1.right==hitbox2.left and ((hitbox1.bottom>=hitbox2.top and hitbox1.bottom<=hitbox2.bottom) or (hitbox1.top>=hitbox2.top and hitbox1.top<=hitbox2.bottom)):
        return ['x','+']
    elif hitbox1.left==hitbox2.right and ((hitbox1.bottom>=hitbox2.top and hitbox1.bottom<=hitbox2.bottom) or (hitbox1.top>=hitbox2.top and hitbox1.top<=hitbox2.bottom)):
        return ['x','-']
    elif ((hitbox1.bottom>=hitbox2.top and hitbox1.bottom<=hitbox2.bottom) or (hitbox1.top>=hitbox2.top and hitbox1.top<=hitbox2.bottom)) and ((hitbox1.left>=hitbox2.left and hitbox1.left<=hitbox2.right ) or (hitbox1.right>=hitbox2.left and hitbox1.right<=hitbox2.right)):
        return ['o','o']
    else:
        return ['f','f']

def how_deep_left(hitbox1:Hitbox,hitbox2:Hitbox):
    """returns 0 if the left side of hitbox1 is touching the right side of hitbox2, 
    if the side is inside hitbox2 returns the distance between the side and the right side of hitbox2
    returns -1 otherwise"""
    if  ((hitbox1.bottom>hitbox2.top and hitbox1.bottom<hitbox2.bottom) or (hitbox1.top>hitbox2.top and hitbox1.top<hitbox2.bottom) or (hitbox1.top==hitbox2.top or hitbox1.bottom==hitbox2.bottom)) and hitbox2.right - hitbox1.left >= 0 and hitbox1.left > hitbox2.left:
        return hitbox2.right - hitbox1.left
    else:
        return -1

def how_deep_right(hitbox1:Hitbox,hitbox2:Hitbox):
    """returns 0 if the right side of hitbox1 is touching the left side of hitbox2, 
    if the side is inside hitbox2 returns the negative distance between the side and the left side of hitbox2
    returns 1 otherwise"""
    if  ((hitbox1.bottom>hitbox2.top and hitbox1.bottom<hitbox2.bottom) or (hitbox1.top>hitbox2.top and hitbox1.top<hitbox2.bottom) or (hitbox1.top==hitbox2.top or hitbox1.bottom==hitbox2.bottom)) and hitbox2.left - hitbox1.right <= 0 and hitbox1.right <= hitbox2.right:
        return hitbox2.left - hitbox1.right
    else:
        return 1

def how_deep_down(hitbox1:Hitbox,hitbox2:Hitbox):
    """returns 0 if the lower side of hitbox1 is touching the upper side of hitbox2, 
    if the side is inside hitbox2 returns the distance between the side and the upper side of hitbox2
    returns -1 otherwise"""
    if  ((hitbox1.left>hitbox2.left and hitbox1.left<hitbox2.right) or (hitbox1.right>hitbox2.left and hitbox1.right<hitbox2.right) or (hitbox1.left==hitbox2.left or hitbox1.right==hitbox2.right)) and hitbox1.bottom - hitbox2.top >= 0 and hitbox1.bottom < hitbox2.bottom:
        return hitbox1.bottom - hitbox2.top
    else:
        return -1
    
def how_deep_up(hitbox1:Hitbox,hitbox2:Hitbox):
    """returns 0 if the lower side of hitbox1 is touching the upper side of hitbox2, 
    if the side is inside hitbox2 returns the distance between the side and the upper side of hitbox2
    returns -1 otherwise"""
    if  ((hitbox1.left>hitbox2.left and hitbox1.left<hitbox2.right) or (hitbox1.right>hitbox2.left and hitbox1.right<hitbox2.right) or (hitbox1.left==hitbox2.left or hitbox1.right==hitbox2.right)) and hitbox1.top - hitbox2.bottom <= 0 and hitbox1.top > hitbox2.top:
        return hitbox1.top - hitbox2.bottom
    else:
        return 1



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbos = True)
