# NSI_Project

Objective:</br>
make a retro type game in python using pyxel

Specifications:</br>

A main character:</br>
    - can move left and right</br>
    - can jump (the more you hold the higher you jump)</br>
    - can be controled mid air ( but can't jump)</br>
    - attacks up right left down</br>
    - a health bar</br>
</br>
    
    
Some upgrades/abilities:</br>
- Dash</br>
- Walljump</br>
- Doublejump</br>
- Ranged attack</br>
- Weapon upgrades</br>
</br>

A combat system:</br>
    -Each entity has a health bar</br>
    -Attacks deal dammage to entities</br>
</br>

Level loading system:</br>
    - Takes a list (texture of the room) of lists (rows) of tuples (textures of the objects)</br>
    - each tuple has 2 ints, one is the number of the texture loaded and the other the rotation</br>
    - another list for the hitboxes of the walls (a list of list of 4 values, xpos, ypos, length and height of the hitbox</br>
    - a way to load enemies</br>
</br>

Some enemies:</br>
    - basic one that just walks until an edege or a wall and turns around</br>
    - more complex ones (runs towards/attacks the player on sight)</br>
    - a flying one?</br>
    </br>
    
Some bosses:</br>
    - Have to be big and cool and epic and stuff</br>
    </br>
    
Boss:</br>
    - baby zombie (hidden)</br>
    - lich</br>

Random idas:</br>
-zombie (big)</br>
-a cat </br>              

to play the game, use this link: https://kitao.github.io/pyxel/wasm/launcher/?run=samuel-minonne.NSI_Project.main 

useful links:
https://nuitducode.github.io/DOCUMENTATION/PYTHON/Premiers%20pas%20avec%20Pyxel%20-%20Premi%C3%A8re%20et%20Terminale/Tutoriel-01/
</br>

