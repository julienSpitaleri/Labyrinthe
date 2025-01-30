def get_maze():
    return [
        [0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 1],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0],
    ]

def is_cell_moutain(pos):
    bool = False
    row, col = pos
    maze = get_maze()
    if maze[row][col] == 1:
        bool = True
    return bool

def break_wall(maze, pos):
    """Casse un mur à la position donnée."""
    row, col = pos
    if is_cell_moutain(pos) :
        maze[row][col] = 0

def use_bombe(maze, player_pos):
    """Casse les murs adjacents à la position du joueur."""
    row, col = player_pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # Haut, Bas, Gauche, Droite
    for dr, dc in directions:
        adj_row, adj_col = row + dr, col + dc
        if 0 <= adj_row < len(maze) and 0 <= adj_col < len(maze[0]):
            if maze[adj_row][adj_col] == 1:
                maze[adj_row][adj_col] = 0