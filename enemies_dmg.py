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
      self.edge_left = False
      self.edge_right = False
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
         if not hb.is_point_in(self.xpos-1,self.ypos+self.height) and hb.is_point_in(self.xpos,self.ypos+self.height):
            self.edge_left = True
         if not hb.is_point_in(self.xpos+self.length+1,self.ypos+self.height) and hb.is_point_in(self.xpos+self.length,self.ypos+self.height):
            self.edge_right = True
      


      if self.xspeed > 0: #si on va vers la droite
         if self.touches_right or self.edge_right: #et qu'on touche à droite on tourne
               self.xspeed = -self.xspeed
         else:
               self.xpos += self.xspeed #sinon (si on touche pas) on se déplace de xspeed
      elif self.xspeed < 0:
         if self.touches_left or self.edge_left:#même chose pour la gauche
               self.xspeed = -self.xspeed
         else:
               self.xpos += self.xspeed
      if self.yspeed > 0: #mouvement sur l'axe y
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

