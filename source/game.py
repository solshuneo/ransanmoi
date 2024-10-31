import pygame
from settings import *
import random
from pygame.image import load
from os import path
from os.path import join
from timer import Timer
class Game:
    def __init__(self):
        self.field_data = self.field_data = [[EMPTY_CELL for x in range(COLUMNS)] for y in range(ROWS)]        
        self.player = [(2, 2), (3, 2), (4, 2), (5, 2)] # (row, col) 
        self.AI = [(7, 5), (8, 5), (9, 5), (10, 5)]       
        self.player_snake = snake(self.player, self.field_data, PLAYER_CELL, self.game_over)
        self.AI_snake = AIsnake(self.AI, self.field_data, COMPUTER_CELL, self.game_over)
        self.display_surface = pygame.display.get_surface()
        self.surface = pygame.Surface(GAME_SIZE)
        self.rect = self.surface.get_rect(topleft = (PADDING, PADDING))

        self.music = pygame.mixer.Sound(join('.', 'sound', 'music.wav'))
        self.music.set_volume(0.1)
        self.music.play(-1)

        self.current_apple = Apple(self.field_data)
        self.field_data[self.current_apple.positionRow][self.current_apple.positionCol] = APPLE_CELL
        self.graphics = {key : pygame.image.load(path.join('.', 'image', f'{key}.png')).convert_alpha() for key in KEY_IMAGES }
        self.delay = MOVE_TIMING
        self.timer = Timer(self.delay, True, self.move)
        self.timer.activate()
        for i in range(self.player_snake.getLength()):
            position = self.player_snake.getPosition(i)
            self.field_data[position[0]][position[1]] = PLAYER_CELL
        for i in range(self.AI_snake.getLength()):
            position = self.AI_snake.getPosition(i)
            self.field_data[position[0]][position[1]] = COMPUTER_CELL
    def game_over(self):
        self.timer.activate()
        self.timer.duration = 10000000
        self.music.stop()
    def move(self):
        self.player_snake.automove()
        self.AI_snake.update()
        self.AI_snake.automove()

    def input(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.player_snake.move != self.player_snake.move_left and self.player_snake.move != self.player_snake.move_right:
            self.player_snake.move = self.player_snake.move_left
        elif key[pygame.K_RIGHT] and self.player_snake.move != self.player_snake.move_left and self.player_snake.move != self.player_snake.move_right:
            self.player_snake.move = self.player_snake.move_right
        elif key[pygame.K_UP] and self.player_snake.move != self.player_snake.move_down and self.player_snake.move != self.player_snake.move_up:
            self.player_snake.move = self.player_snake.move_up
        elif key[pygame.K_DOWN] and self.player_snake.move != self.player_snake.move_down and self.player_snake.move != self.player_snake.move_up:
            self.player_snake.move = self.player_snake.move_down

    def display_graphics(self):
        def alter_direction(theroot, another):
            return (another[0] - theroot[0], another[1] - theroot[1])
        def thekey(dir, parter):
            key = parter
            if dir == DIRECTION_DOWN:
                key += r"\down"
            elif dir == DIRECTION_LEFT:
                key += r"\left"
            elif dir == DIRECTION_UP:
                key += r"\up"
            else:
                key += r"\right"
            return key
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.field_data[row][col] == EMPTY_CELL:
                    continue
                y = row * CELL_SIZE
                x = col * CELL_SIZE
                img = None        
                if self.field_data[row][col] == PLAYER_CELL:            
                    if self.player_snake.getPosition(HEAD) == (row, col):
                        dir = alter_direction(self.player_snake.getPosition(HEAD + 1), self.player_snake.getPosition(HEAD))
                        key = thekey(dir, "head")
                        img = self.graphics[key]
                    elif self.player_snake.getPosition(TAIL) == (row, col):
                        dir = alter_direction(self.player_snake.getPosition(TAIL), self.player_snake.getPosition(TAIL - 1))
                        key = thekey(dir, "tail")
                        img = self.graphics[key]
                    else:
                        index = self.player_snake.findIndex(row, col)
                        dir = alter_direction(self.player_snake.getPosition(index), self.player_snake.getPosition(index-1))
                        key = thekey(dir, r"body\player")
                        img = self.graphics[key]
                elif self.field_data[row][col] == COMPUTER_CELL:            
                    if self.AI_snake.getPosition(HEAD) == (row, col):
                        dir = alter_direction(self.AI_snake.getPosition(HEAD + 1), self.AI_snake.getPosition(HEAD))
                        key = thekey(dir, "head")
                        img = self.graphics[key]
                    elif self.AI_snake.getPosition(TAIL) == (row, col):
                        dir = alter_direction(self.AI_snake.getPosition(TAIL), self.AI_snake.getPosition(TAIL - 1))
                        key = thekey(dir, "tail")
                        img = self.graphics[key]
                    else:
                        index = self.AI_snake.findIndex(row, col)
                        dir = alter_direction(self.AI_snake.getPosition(index), self.AI_snake.getPosition(index-1))
                        key = thekey(dir, r"body\computer")
                        img = self.graphics[key]
                elif self.field_data[row][col] == APPLE_CELL:
                    img = self.graphics["apple"]
                if img == None:
                    continue
                img_resized = pygame.transform.scale(img, (CELL_SIZE - PADDING_IMAGE, CELL_SIZE - PADDING_IMAGE))
                rect = img_resized.get_rect(topleft=(x + PADDING_IMAGE, y + PADDING_IMAGE))
                self.surface.blit(img_resized, rect)
    def draw_grid(self):
        for col in range(1, COLUMNS):
            x = col * CELL_SIZE            
            pygame.draw.line(self.surface, LINE_COLOR, (x, 0), (x, self.surface.get_height()), 1)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.surface, LINE_COLOR, (0, y), (self.surface.get_width(), y), 1)

    def run(self):
        self.display_surface.blit(self.surface, (PADDING, PADDING))
        self.surface.fill(BACKGROUND_GAME_COLOR)
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)
        self.draw_grid()
        self.display_graphics()
        self.timer.update()
        self.current_apple.update_new_position()
        self.input()

class Apple:
    def __init__(self, field_data):
        self._field_data = field_data
        self.position = None
        self.lengthField_data = len(self._field_data)
        while True:            
            self.position = random.randint(0, self.lengthField_data ** 2 - 1)
            row = self.position // self.lengthField_data
            col = self.position % self.lengthField_data
            if self._field_data[row][col] == EMPTY_CELL:
                break
        self.positionRow = self.position // self.lengthField_data
        self.positionCol = self.position % self.lengthField_data
    def update_new_position(self):        
        if self.position != None:
            row = self.position // self.lengthField_data
            col = self.position % self.lengthField_data
            if self._field_data[row][col] == APPLE_CELL:
                return
        while True:            
            self.position = random.randint(0, self.lengthField_data ** 2 - 1)
            row = self.position // self.lengthField_data
            col = self.position % self.lengthField_data
            if self._field_data[row][col] == EMPTY_CELL:
                self.positionRow = self.position // self.lengthField_data
                self.positionCol = self.position % self.lengthField_data
                self._field_data[row][col] = APPLE_CELL
                break
class snake():
    def __init__(self, initial_position, field_data, type, game_over):
        self._body = initial_position
        self._field_data = field_data
        self.type = type
        self.body = self._body
        self.move = self.move_right
        self.game_over = game_over
        self.apple = 0
    def automove(self):
        self.move()
    def getLength(self):
        return len(self._body)
    def getPosition(self, index):
        if not index < self.getLength():
            return None
        return self._body[index]
    def findIndex(self, row, col):
        index = HEAD
        while index < self.getLength() and self._body[index] != (row, col):
            index += 1
        if index == self.getLength():
            return None
        return index
    def __updateSize(self):
        self._body.append(self._body[-1])
        self.apple += 1
    def _isCollision(self, row, col):
        res = not (0 <= row < ROWS and 0 <= col < COLUMNS and (self._field_data[row][col] == EMPTY_CELL or self._field_data[row][col] == APPLE_CELL))       
        if res:
            if (0 <= row < ROWS and 0 <= col < COLUMNS and self._field_data[row][col] == self.type and self.findIndex(row, col) == HEAD + 1):
                return True
            self.game_over()
            return res
        if self._field_data[row][col] == APPLE_CELL:
            self.__updateSize()            
            self._field_data[row][col] = EMPTY_CELL            
            self.music = pygame.mixer.Sound(join('.', 'sound', 'landing.wav'))
            self.music.set_volume(0.1)
            self.music.play(1)
        return res
    def move_left(self):
        new_head = (self._body[0][0] + DIRECTION_LEFT[0], self._body[0][1] + DIRECTION_LEFT[1])
        if self._isCollision(new_head[0], new_head[1]):
           return 
        self._body.insert(0, new_head)
        self._field_data[self._body[-1][0]][self._body[-1][1]] = EMPTY_CELL
        self._body.pop()
        self._field_data[new_head[0]][new_head[1]] = self.type
        self._field_data[self._body[-1][0]][self._body[-1][1]] = self.type
    def move_right(self):
        new_head = (self._body[0][0] + DIRECTION_RIGHT[0], self._body[0][1] + DIRECTION_RIGHT[1])
        if self._isCollision(new_head[0], new_head[1]):
           return 
        self._body.insert(0, new_head)
        self._field_data[self._body[-1][0]][self._body[-1][1]] = EMPTY_CELL
        self._body.pop()
        self._field_data[new_head[0]][new_head[1]] = self.type
        self._field_data[self._body[-1][0]][self._body[-1][1]] = self.type
    def move_up(self):
        new_head = (self._body[0][0] + DIRECTION_UP[0], self._body[0][1] + DIRECTION_UP[1])
        if self._isCollision(new_head[0], new_head[1]):
           return 
        self._body.insert(0, new_head)
        self._field_data[self._body[-1][0]][self._body[-1][1]] = EMPTY_CELL
        self._body.pop()
        self._field_data[new_head[0]][new_head[1]] = self.type
        self._field_data[self._body[-1][0]][self._body[-1][1]] = self.type
    def move_down(self):
        new_head = (self._body[0][0] + DIRECTION_DOWN[0], self._body[0][1] + DIRECTION_DOWN[1])
        if self._isCollision(new_head[0], new_head[1]):
           return 
        self._body.insert(0, new_head)
        self._field_data[self._body[TAIL][0]][self._body[TAIL][1]] = EMPTY_CELL
        self._body.pop()
        self._field_data[new_head[0]][new_head[1]] = self.type
        self._field_data[self._body[TAIL][0]][self._body[TAIL][1]] = self.type

class AIsnake(snake):
    def __init__(self, initial_position, field_data, type, game_over):
        super().__init__(initial_position, field_data, type, game_over)
    def update(self):
        bestDirection = self.bestDirection()
        print(bestDirection)
        if bestDirection == DIRECTION_DOWN:
            self.automove = self.move_down
        if bestDirection == DIRECTION_LEFT:
            self.automove = self.move_left
        if bestDirection == DIRECTION_RIGHT:
            self.automove = self.move_right
        if bestDirection == DIRECTION_UP:
            self.automove = self.move_up
    def bestDirection(self):
        score = [[100000 for x in range(COLUMNS)] for y in range(ROWS)]        
        
        # Xác định vị trí của quả táo
        def goal():
            for row in range(ROWS):
                for col in range(COLUMNS):
                    if self._field_data[row][col] == APPLE_CELL:
                        return (row, col)
            return None
        
        dest = goal()
        if dest is None:
            return None
        
        # Tìm đường đi và ghi điểm số tối thiểu vào bảng `score`
        def dfs(source, destination, data):
            rows, cols = len(data), len(data[0])            
            stack = [(source[0], source[1], 0)]  # (row, col, current_score)
            score[source[0]][source[1]] = 0  # Điểm bắt đầu có điểm số là 0

            while stack:
                x, y, current_score = stack.pop()

                if (x, y) == destination:
                    continue

                # Duyệt tất cả các hướng
                for dx, dy in DIREECTION:
                    nx, ny = x + dx, y + dy

                    # Kiểm tra điều kiện nằm trong bản đồ và không phải là 'stone'
                    if 0 <= nx < rows and 0 <= ny < cols and (
                        data[nx][ny] == EMPTY_CELL or 
                        (data[nx][ny] == COMPUTER_CELL and current_score > self.getLength() - self.findIndex(nx, ny))
                    ):
                        new_score = current_score + 1  # Tăng điểm số lên 1 cho bước đi mới

                        # Nếu ô này chưa được đi qua hoặc có điểm số thấp hơn
                        if new_score < score[nx][ny]:
                            score[nx][ny] = new_score
                            stack.append((nx, ny, new_score))
            return

        dfs(self._body[HEAD], dest, self._field_data)

        # Truy vết đường đi từ `source` đến `destination`
        source = self._body[HEAD]
        current_position = source

        while current_position != dest:
            best = float('inf')
            next_step = None

            # Tìm bước tiếp theo có `score` nhỏ nhất
            for dx, dy in DIREECTION:
                nx, ny = dest[0] + dx, dest[1] + dy
                
                if 0 <= nx < ROWS and 0 <= ny < COLUMNS and score[nx][ny] < best:
                    best = score[nx][ny]
                    next_step = (nx, ny)
            
            if next_step is None:
                return None  # Không tìm thấy đường đi
            print(next_step)
            if next_step == current_position:
                break
            dest = next_step

            # Cập nhật vị trí hiện tại
        
        return (dest[0] - current_position[0], dest[1] - current_position[1])

