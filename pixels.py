import pygame
import grid

window_width = 500
window_height = 500

grid_width = 20
grid_height = 20
grid_padding = 8

generate_pixels = 20
infected_pixels = 4

timestep = 100

def main():
    # Initialize pygame
    pygame.init()
    
    # Define the size of the window
    window = pygame.display.set_mode((window_width, window_height))

    # Set the title of the window
    pygame.display.set_caption('Pixels - Plague Simulator')

    simulation_grid = grid.Grid(window_width, window_height, grid_width, grid_height, grid_padding, generate_pixels, infected_pixels)

    # Loop
    running = True
    while running:
        # Give a fixed delay to make the simulation consistent (in theory)
        pygame.time.delay(timestep)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen (likely unnecessary)
        #window.fill((0, 0, 0))

        # Update and render the simulation grid
        simulation_grid.update()
        simulation_grid.render(window)

        # Update the display
        pygame.display.update()

    # Clean up after the program is done running
    pygame.quit()

# Call the main function
main()