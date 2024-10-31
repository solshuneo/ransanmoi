import pygame
from game import Game
from score import Score
from settings import *
from os.path import join

class Main:
    def __init__(self):
        pygame.init()
        self.title = "ransanmoi"
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(self.title)

        self.game = Game()
        self.score = Score(self.game.player_snake, self.game.AI_snake)


    def run(self):        
        while True:
            self.screen.fill(BACKGROUND_COLOR)
            self.game.run()
            self.score.run()
            for event  in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                is_dragging = False
                # Bắt đầu kéo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Chuột trái
                        is_dragging = True
                        last_mouse_position = event.pos  # Lưu vị trí chuột

                # Kết thúc kéo
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Chuột trái
                        is_dragging = False

                # Di chuyển cửa sổ
                if event.type == pygame.MOUSEMOTION:
                    if is_dragging:
                        # Tính toán khoảng cách di chuyển
                        delta_x = event.pos[0] - last_mouse_position[0]
                        delta_y = event.pos[1] - last_mouse_position[1]

                        # Di chuyển cửa sổ
                        pygame.display.set_mode(WINDOW_SIZE, pygame.NOFRAME)  # Tắt khung
                        x, y = pygame.mouse.get_pos()  # Lấy vị trí chuột
                        pygame.display.set_mode(WINDOW_SIZE, pygame.NOFRAME | pygame.RESIZABLE)  # Bật lại khung
                        pygame.display.set_caption("Cửa sổ di chuyển")  # Đặt tiêu đề cửa sổ

                        # Di chuyển cửa sổ bằng cách thay đổi vị trí (chỉ áp dụng trên Windows)
                        pygame.display.set_mode(WINDOW_SIZE)  # Bật lại kích thước

                        # Lưu vị trí chuột
                        last_mouse_position = event.pos
            pygame.display.update()
            pygame.display.flip()


if __name__ == "__main__":
    main = Main()
    main.run()
