import pyxel
import hitboxes
import gameobjects
import math

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
         if self.touches_right or self.edge_right: #et qu'on touche ou que y'a du vide à droite on tourne 
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

   def mouvement(self,player):
     print("ye")

   def draw(self,x,y):
        pyxel.rect(x,y,self.length,self.height,4)
        

class Bat(gameobjects.Entity):
      
      def __init__(self, x, y, walls_list, speedx = 0, speedy = 0, facing_right = True):
            super().__init__(x,y,8,8,5,walls_list)#mettre les valeur manuellement
            self.xspeed = 0.7
      
      def mouvement(self,player):

            if (player.xpos - self.xpos)**2 + (player.ypos - self.ypos)**2 <= 2304:
                  angle_to_player = math.atan2(self.ypos-player.ypos,self.xpos-player.xpos)
                  self.setSpeedWithAngle(angle_to_player,-0.5)  

            else:
                  if self.xspeed > 0:
                        self.xspeed -= 0.25
                  elif self.xspeed < 0:
                        self.xspeed += 0.25

                  if self.yspeed > 0:
                        self.yspeed -= 0.25
                  elif self.yspeed < 0:
                        self.yspeed += 0.25
      def draw(self,x,y):
            pyxel.rect(x,y,self.length,self.height,1)

class Whizard(gameobjects.Entity):
     
     def __init__(self, x, y, wall_list, speedx = 0, speedy =0):
          super().__init__(x,y,8,8,5, wall_list)#mettre les valeur manuellement
          self.xspeed = 0.7
          facing_player = False
          edge_right = False
          edge_left = False
          blindness_time = 0 

     def mouvement(self,player):      
            if (player.xpos - self.xpos)**2 + (player.ypos - self.ypos)**2 <= 2304:
               facing_player = True 

            if facing_player == True and self.xpos > player.xpos:
                  self.xspeed += 0.01
            elif facing_player == True and self.xpos < player.xpos:
                  self.xspeed -= 0.01
            
            else:
               
               for hb in self.walls_list:
                    if not hb.is_point_in(self.xpos-1,self.ypos+self.height) and hb.is_point_in(self.xpos,self.ypos+self.height):
                        self.edge_left = True
                    if not hb.is_point_in(self.xpos+self.length+1,self.ypos+self.height) and hb.is_point_in(self.xpos+self.length,self.ypos+self.height):
                        self.edge_right = True

               if self.edge_left == True or self.edge_right == True:
                    self.xspeed = -self.xspeed

     def attack(self, player):     
          if self.xpos == player.xpos: 
               while self.blindness_time > 0:
                    pyxel.camera(30,20)

     def draw(self,x,y):
            pyxel.rect(x,y,self.length,self.height,)

