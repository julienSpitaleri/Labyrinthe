import pygame

from maze import is_cell_moutain, use_bombe
from ui import TILE_SIZE, WIDTH, HEIGHT, WHITE, get_avatar, get_crack_image

def break_wall(screen, maze, pos):
    crack_image = get_crack_image(TILE_SIZE)
    row, col = pos
    if maze[row][col] == 1:  # Vérifie qu'il s'agit d'un mur
        rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        
        # Affiche l'image de fracture
        screen.blit(crack_image, rect.topleft)
        pygame.display.flip()
        pygame.time.delay(200)  # Durée de l'effet en millisecondes
        
        # Supprime le mur
        maze[row][col] = 0


def teleport_player(screen, player_pos, new_pos):
    avatar = get_avatar(TILE_SIZE)
    """Animation visuelle pour la téléportation avec effet d'éclair."""
    lightning_color = (128, 0, 128)  # Couleur jaune pour l'effet
    lightning_duration = 100  # Durée en millisecondes

    if not is_cell_moutain(new_pos):
        # Effet à la nouvelle position
        pygame.draw.rect(
            screen, lightning_color,
            (new_pos[1] * TILE_SIZE, new_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )
        pygame.display.flip()
        pygame.time.delay(lightning_duration)

        # Mise à jour de la position
        player_pos[0], player_pos[1] = new_pos   



def bomb_explosion(screen, maze, player_pos):
    """Animation visuelle pour l'explosion de la bombe."""
    row, col = player_pos
    center = (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2)
    for radius in range(0, TILE_SIZE * 2, 10):  # Cercles concentriques
        pygame.draw.circle(screen, (255, 0, 0), center, radius, 2)
        pygame.display.flip()
        pygame.time.delay(50)
        use_bombe(maze, player_pos)  # Supprime les murs adjacents
