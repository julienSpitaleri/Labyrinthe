import pygame

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 6, 6
TILE_SIZE = WIDTH // COLS


# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
# Chargez l'image de montagne
mountain_image = pygame.image.load("assets/montagne.png")  # Remplacez par le chemin réel
mountain_image = pygame.transform.scale(mountain_image, (TILE_SIZE, TILE_SIZE))  # Redimensionner
# Chargez l'image de l'arrive
flag_image = pygame.image.load("assets/drapeau.png")  # Remplacez par le chemin réel
flag_image = pygame.transform.scale(flag_image, (TILE_SIZE, TILE_SIZE))  # Redimensionner

def draw_grid(screen, maze):
    """Dessine la grille et le labyrinthe."""
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if maze[row][col] == 1:
                screen.blit(mountain_image, rect.topleft)
            else:
                pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_player(screen, player_pos):
    """Dessine le joueur."""
    rect = pygame.Rect(player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, BLUE, rect)

def draw_player_avatar(screen, player_pos):
    """Dessine le joueur avec une image réduite et centrée sur un fond coloré."""
    # Taille de la case
    rect = pygame.Rect(player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    avatar = get_avatar(TILE_SIZE)
    # Taille réduite de l'avatar (95% de la case)
    avatar_size = int(TILE_SIZE * 0.95)
    resized_avatar = pygame.transform.scale(avatar, (avatar_size, avatar_size))
    
    # Calcul des marges pour centrer l'avatar dans la case
    margin_x = (TILE_SIZE - avatar_size) // 2
    margin_y = (TILE_SIZE - avatar_size) // 2
    
    # Dessiner l'avatar centré
    screen.blit(resized_avatar, (rect.x + margin_x, rect.y + margin_y))

def draw_exit(screen, exit_pos):
    """Dessine la sortie."""
    rect = pygame.Rect(exit_pos[1] * TILE_SIZE, exit_pos[0] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    screen.blit(flag_image, rect.topleft)
    
def get_cell_from_mouse(pos):
    """Renvoie la cellule cliquée à partir de la position de la souris."""
    x, y = pos
    return y // TILE_SIZE, x // TILE_SIZE

def get_avatar(tile_size):
    """Charge et redimensionne l'image de l'avatar."""
    avatar_path = "assets/robot.png"  # Chemin vers l'image de l'avatar
    avatar = pygame.image.load(avatar_path).convert_alpha()  # Charger l'image avec transparence
    avatar = pygame.transform.scale(avatar, (int(tile_size * 0.95), int(tile_size * 0.95)))  # Redimensionner à 95% de la taille de la case
    return avatar

def get_crack_image(tile_size):
    """Charge et redimensionne l'image de fracture."""
    crack_path = "assets/pioche.png"  # Chemin vers l'image de fracture
    crack = pygame.image.load(crack_path).convert_alpha()
    crack = pygame.transform.scale(crack, (tile_size, tile_size))  # Taille de la case
    return crack
