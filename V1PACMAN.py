import pygame
import math

# Initialize Pygame
pygame.init()

# Screen setup
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygame Pac-Man')

# Maze setup
maze_layout = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W.d............WW.dW",
    "W.WWWW.WWWWW.WW.WWWW",
    "WPWWWW.WWWWW.WW.WWWW",
    "Wd....WW...WW.....dW",
    "W.WWWWWWWWWWWW.WWWW",
    "W...............WdW",
    "WWWWWWWWWWWWWWWWWWWW"
]

maze_row_height = screen_height // len(maze_layout)
maze_column_width = screen_width // len(maze_layout[0])
wall_color = (0, 0, 255)  # Blue walls
dot_color = (255, 255, 255)  # White dots

# Pac-Man setup
pacman_color = (255, 255, 0)  # Classic yellow
pacman_x = 0
pacman_y = 0
pacman_direction = 'right'
pacman_speed = maze_column_width // 10  # Adjust speed relative to maze size
pacman_radius = min(maze_row_height, maze_column_width) // 4  # Adjust size relative to maze
pacman_open_angle = 45  # Degrees Pac-Man's mouth is open

# Find Pac-Man's starting position
for row_index, row in enumerate(maze_layout):
    for col_index, cell in enumerate(row):
        if cell == 'P':
            pacman_x = col_index * maze_column_width + maze_column_width // 2
            pacman_y = row_index * maze_row_height + maze_row_height // 2
            break

# Game loop setup
running = True
clock = pygame.time.Clock()

def is_wall(x, y):
    # Check if the next position is a wall
    row = y // maze_row_height
    col = x // maze_column_width
    if maze_layout[row][col] == 'W':
        return True
    return False

# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Key press events to change directions
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pacman_direction = 'right'
            elif event.key == pygame.K_LEFT:
                pacman_direction = 'left'
            elif event.key == pygame.K_UP:
                pacman_direction = 'up'
            elif event.key == pygame.K_DOWN:
                pacman_direction = 'down'

    # Pac-Man Movement with wall collision
    next_x, next_y = pacman_x, pacman_y
    if pacman_direction == 'right':
        next_x += pacman_speed
    elif pacman_direction == 'left':
        next_x -= pacman_speed
    elif pacman_direction == 'up':
        next_y -= pacman_speed
    elif pacman_direction == 'down':
        next_y += pacman_speed

    # Check for wall collisions
    if not is_wall(next_x, next_y):
        pacman_x, pacman_y = next_x, next_y

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw the maze
    for row_index, row in enumerate(maze_layout):
        for col_index, cell in enumerate(row):
            x = col_index * maze_column_width
            y = row_index * maze_row_height
            if cell == 'W':
                pygame.draw.rect(screen, wall_color, (x, y, maze_column_width, maze_row_height))
            elif cell == 'd':
                pygame.draw.circle(screen, dot_color, (x + maze_column_width // 2, y + maze_row_height // 2), pacman_radius // 2)

    # Draw Pac-Man
    start_angle = pacman_open_angle if pacman_direction in ['left', 'up'] else 0
    end_angle = 360 - pacman_open_angle if pacman_direction in ['right', 'down'] else 180
    pygame.draw.arc(screen, pacman_color, (pacman_x - pacman_radius, pacman_y - pacman_radius, 2 * pacman_radius, 2 * pacman_radius), 
                    math.radians(start_angle), math.radians(end_angle), pacman_radius)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
