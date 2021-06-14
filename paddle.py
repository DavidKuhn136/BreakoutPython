import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    # this class represents a paddle.  it derives from the sprite class

    def __init__(self, color, width, height):
        # call the parent class (Sprite) constructor
        super().__init__()

        # pass in the color of the car, and its x and y position, width and height
        # set the background color and set it to be transparent
        self.image = pygame.Surface([width,height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # check that it is not going off screen
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # check that it is not going off screen
        if self.rect.x > 700:
            self.rect.x = 700
            