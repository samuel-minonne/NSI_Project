# NSI_Project

Objective:</br>
make a retro type game in python using pyxel</br>
</br>

To-do list:</br>
    - Ajouter des tests unitaires</br>
    - Find a title</br>
    </br>

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
</br>

A combat system:</br>
    -Each entity has a health bar</br>
    -Attacks deal dammage to entities</br>
</br>



Level loading system:</br>
    - Uses two lists containing lists, one for the hitboxes one for the textures (in tutorial.json)</br>
    - the list for the textures contains lists containing these infos:(x,y,page on the spritesheet,x in spritesheet,y in spritesheet,width copied, length copied, the color that doesn't show)</br>
    - the list for the hitboxes of the walls is a list of list of 4 values, xpos, ypos, length and height of the hitbox</br>
    - a way to load enemies</br>
</br>

Some enemies:</br>
    - basic one that just walks until an edege or a wall and turns around</br>
    - a wizzard</br>
    - a flying one</br>
    </br>
    
Some bosses:</br>
    - Have to be big and cool and epic and stuff</br>
    </br>
    
Who does what:</br>
    - Samuel, gameobjects, hitboxes and combat sythem, helping us folks</br>
    - Valentin, textures designing, texture showing, animations, music</br>
    - Elisa, enemies and death animations</br>
    </br>
    

Random idas:</br>
    - zombie (big)</br>
    - baby zombie (hidden)</br>
    - lich</br>
    - a cat </br>              

to play the game, use this link: https://kitao.github.io/pyxel/wasm/launcher/?run=samuel-minonne.NSI_Project.main 

useful links:
https://nuitducode.github.io/DOCUMENTATION/PYTHON/Premiers%20pas%20avec%20Pyxel%20-%20Premi%C3%A8re%20et%20Terminale/Tutoriel-01/
</br>

