import pygame
CELL_SIZE = 40
COLUMNS = 20
ROWS = COLUMNS
PADDING = 20
PADDING_IMAGE = 1
GAME_SIZE = pygame.Vector2(COLUMNS * CELL_SIZE, ROWS * CELL_SIZE)
SCORE_SIZE = pygame.Vector2(ROWS * CELL_SIZE // 3,  GAME_SIZE.y)

WINDOW_SIZE = GAME_SIZE + SCORE_SIZE + (3 * PADDING, 2 * PADDING) - pygame.Vector2(0, SCORE_SIZE.y)
OFFSET = (COLUMNS // 2, 1)

# Biến thể của màu đỏ
LIGHT_RED   = (255, 102, 102)  # Đỏ nhạt
DARK_RED    = (139, 0, 0)      # Đỏ đậm

# Biến thể của màu xanh lá
LIGHT_GREEN = (144, 238, 144)  # Xanh lá nhạt
DARK_GREEN  = (0, 100, 0)      # Xanh lá đậm

# Biến thể của màu xanh dương
LIGHT_BLUE  = (173, 216, 230)  # Xanh dương nhạt
DARK_BLUE   = (0, 0, 139)      # Xanh dương đậm

# Biến thể của màu vàng
LIGHT_YELLOW = (255, 255, 224) # Vàng nhạt
DARK_YELLOW  = (204, 204, 0)   # Vàng đậm

# Biến thể của màu cam
LIGHT_ORANGE = (255, 200, 150) # Cam nhạt
DARK_ORANGE  = (255, 140, 0)   # Cam đậm

# Biến thể của màu tím
LIGHT_PURPLE = (216, 191, 216) # Tím nhạt
DARK_PURPLE  = (75, 0, 130)    # Tím đậm

# Biến thể của màu hồng
LIGHT_PINK   = (255, 182, 193) # Hồng nhạt
DARK_PINK    = (255, 20, 147)  # Hồng đậm

# Biến thể của màu nâu
LIGHT_BROWN  = (222, 184, 135) # Nâu nhạt
DARK_BROWN   = (101, 67, 33)   # Nâu đậm

# Biến thể của màu xám
SILVER       = (192, 192, 192) # Bạc (xám nhạt)
DIM_GRAY     = (105, 105, 105) # Xám mờ

# Một số màu đặc biệt khác
GOLD         = (255, 215, 0)   # Vàng ánh kim
OLIVE        = (128, 128, 0)   # Xanh oliu
TEAL         = (0, 128, 128)   # Xanh mòng két
NAVY         = (0, 0, 128)     # Xanh hải quân


LINE_COLOR = (255,160,122)
BACKGROUND_GAME_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (255, 255, 255)
#BACKGROUND_COLOR = (105, 105, 105)

# (x for col, y for row)
# (row, col)
DIRECTION_LEFT = (0, -1)
DIRECTION_RIGHT = (0, 1)
DIRECTION_UP = (-1, 0)
DIRECTION_DOWN = (1, 0)

DIREECTION = [DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_UP, DIRECTION_RIGHT]

HEAD = 0
TAIL = -1

EMPTY_CELL = -1
APPLE_CELL = -2
PLAYER_CELL = 1
COMPUTER_CELL = 2

MOVE_TIMING = 150

KEY_IMAGES = {r"head\left", r"head\right", r"head\up", r"head\down", 
              r"body\computer\up", r"body\computer\down", r"body\computer\right", r"body\computer\left", 
              r"body\player\up", r"body\player\down", r"body\player\right", r"body\player\left", 
              r"tail\left", r"tail\right", r"tail\up", r"tail\down",
              "apple"}