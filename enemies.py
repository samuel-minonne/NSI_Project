import pyxel
import hitboxes
import gameobjects

class Test_enemy(gameobjects.Entity):
     def __init__(self,x,y,walls_list,speedx = 0,speedy = 0,facing_right = True):
        super().__init__(x,y,8,8,5,walls_list)#mettre les valeur manuellement
        self.xspeed = 0.5
      
     def update(self):
        """
        Updates the entity (position, hp,...). MUST be executed once per frame.
        """
        if self.yspeed < 1:
            self.yspeed = self.yspeed + 0.05
            
        
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
                self.xspeed = -self.xspeed
            else:
                self.xpos += self.xspeed #sinon (si on touche pas) on se déplace de xspeed
        elif self.xspeed < 0:
            if self.touches_left:#même chose pour la gauche
                self.xspeed = -self.xspeed
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
        
        