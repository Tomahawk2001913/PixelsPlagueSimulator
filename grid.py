import pygame
import pixel
import random

class Grid:
    def __init__(self, window_width, window_height, grid_width, grid_height, grid_padding, generate_pixels = 20, infected_pixels = -1):
        self.window_width = window_width
        self.window_height = window_height

        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid_padding = grid_padding

        self.square_width = window_width / grid_width
        self.square_height = window_height / grid_height

        # Define a blank grid to copy when clearing the grid. Hopefully more efficient than generating it each time.
        self.__blank_grid = [(255, 255, 255)] * self.grid_width * self.grid_height
        
        self.__past_grid = [None] * len(self.__blank_grid)

        self.__clear_grid()

        self.__generate_pixels_randomly(generate_pixels, infected_pixels)

    def __generate_pixels_randomly(self, number, infected = -1):
        self.pixels = []

        # Handle the default infected value
        if infected < 0:
            infected = int(number * 0.2) + 1

        # Create the requested number of pixels
        for i in range(number):
            new_pixel = pixel.Pixel(self.grid_width, self.grid_height)

            new_pixel.x = random.randint(0, self.grid_width - 1)
            new_pixel.y = random.randint(0, self.grid_height - 1)

            # Infect the number of pixels defined by the infected variable
            if i < infected:
                new_pixel.color = pixel.Pixel.red

            self.pixels.append(new_pixel)

    def __generate_pixels_evenly(self, number): # TODO: Finish
        self.pixels = []

        for i in range(number):
            new_pixel = pixel.Pixel(self.grid_width, self.grid_height)

            self.pixels.append(new_pixel)

    def update(self):
        for p in self.pixels:
            p.update(self.pixels)

    def render(self, window):
        # Reset the grid to white
        self.__clear_grid()

        # Assign the color green to every spot with a pixel
        for p in self.pixels:
            self.__grid[p.x + p.y * self.grid_width] = p.color

        # Draw the grid to the screen
        self.__draw_grid(window)

    def __clear_grid(self):
        self.__grid = list(self.__blank_grid)

    def __draw_grid(self, window):
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if self.__grid[x + y * self.grid_width] != self.__past_grid[x + y * self.grid_width]:
                    pygame.draw.rect(window, self.__grid[x + y * self.grid_width], (x * self.square_width + self.grid_padding / 2, y * self.square_height + self.grid_padding / 2, self.square_width - self.grid_padding, self.square_height - self.grid_padding))
        
        self.__past_grid = list(self.__grid)
