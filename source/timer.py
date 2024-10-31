from pygame.time import get_ticks
class Timer:
    def __init__(self, duration, repeated = False, func = None) -> None:
        self.repeated = repeated
        self.func = func
        self.duration = duration
    
        self.start_game = 0
        self.active = False
    def activate(self):
        self.active = True
        self.start_game = get_ticks()
    def deactivate(self):
        self.active = False
        self.start_game = 0
    def update(self):
        current_time = get_ticks()
        if current_time - self.start_game >= self.duration and self.active:
            if self.func and self.start_game != 0:
                self.func()
            self.deactivate()
            if self.repeated:
                self.activate()