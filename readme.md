# Jeux découverte de la programmation

## 2 phases : 
    1ère phase :
        débugger les touches directionnel qui permettent au robot de se déplacer
        attribuer les joker en fonction de la rapidité et de la dynamique du groupe
    2ème phase : 
        Insérer le code au dos des joker pour executer les actions
## Joker : 
    carte marteau pour casser les murs
        durabilite = 3
    carte téléportation
        durabilte = 1
    carte bombe
        durabilite = 1

## Correction : 
    1ère phase :
        ligne 42 : player_pos = move_player(player_pos, "up", maze)
        ligne 44 : player_pos = move_player(player_pos, "down", maze)
        ligne 46 : player_pos = move_player(player_pos, "left", maze)
        ligne 48 : player_pos = move_player(player_pos, "right", maze)
    2ème phase : 
        ligne 50 : bomb_explosion(screen, maze,player_pos)
        ligne 57 : break_wall(screen, maze, cell)
        ligne 60 : teleport_player(screen, player_pos,list(cell))
