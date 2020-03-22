import random

class Pixel:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    def __init__(self, grid_width, grid_height):
        self.__grid_width = grid_width
        self.__grid_height = grid_height

        self.x = 0
        self.y = 0

        self.color = Pixel.green

    def update(self, pixels):
        new_x = self.x
        new_y = self.y

        new_x += random.randint(-1, 1)
        new_y += random.randint(-1, 1)

        if new_x < 0:
            new_x = 0
        elif new_x >= self.__grid_width:
            new_x = self.__grid_width - 1
        
        if new_y < 0:
            new_y = 0
        elif new_y >= self.__grid_height:
            new_y = self.__grid_height - 1

        collision = self.__check_collision(new_x, new_y, pixels)

        if collision == None:
            self.x = new_x
            self.y = new_y
        else:
            if self.color == Pixel.red:
                collision.color = Pixel.red

    def __check_collision(self, x, y, pixels):
        for p in pixels:
            if p == self:
                continue

            if p.x == x and p.y == y:
                return p
        
        return None