def move_player(player_pos, direction, maze):
    """Déplace le joueur dans la direction donnée."""
    row, col = player_pos

    if direction == "up" and row > 0 and maze[row - 1][col] == 0:
        player_pos[0] -= 1
    elif direction == "down" and row < len(maze) - 1 and maze[row + 1][col] == 0:
        player_pos[0] += 1
    elif direction == "left" and col > 0 and maze[row][col - 1] == 0:
        player_pos[1] -= 1
    elif direction == "right" and col < len(maze[0]) - 1 and maze[row][col + 1] == 0:
        player_pos[1] += 1
    return player_pos


    