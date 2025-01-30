import pygame
import sys
from animation import bomb_explosion, break_wall, teleport_player
from maze import get_maze
from player import move_player
from ui import draw_grid, draw_player_avatar, draw_exit, WIDTH, HEIGHT, WHITE, get_cell_from_mouse

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Labyrinthe")

# Initialisation
maze = get_maze()
player_pos = [0, 0]  # Ligne, Colonne
exit_pos = [5, 5]  # Sortie
bomb_used = False
teleportation_used = False
pioche = 3


# Boucle principale
running = True
while running:
    screen.fill(WHITE)

    draw_grid(screen, maze)
    draw_player_avatar(screen, player_pos)
    draw_exit(screen, exit_pos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            #gestion des touches du clavier
            if event.key == pygame.K_UP:
                player_pos = move_player(player_pos, "left", maze)
            elif event.key == pygame.K_DOWN:
                player_pos = move_player(player_pos, "up", maze)
            elif event.key == pygame.K_LEFT:
                player_pos = move_player(player_pos, "right", maze)
            elif event.key == pygame.K_RIGHT:
                player_pos = move_player(player_pos, "down", maze)
            elif event.key == pygame.K_SPACE and not bomb_used:
                bomb_used = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #gestion des touches de la souris
            mouse_pos = pygame.mouse.get_pos()
            cell = get_cell_from_mouse(mouse_pos)
            if event.button == 1 and pioche > 0:  # Clic gauche 
                pioche = pioche - 1 
            elif event.button == 3 and not teleportation_used:  # Clic droit
                teleportation_used = True

    # Vérifie si le joueur a atteint la sortie
    if player_pos == exit_pos:
        print("Félicitations ! Vous avez trouvé la sortie !")
        running = False

pygame.quit()
sys.exit()
