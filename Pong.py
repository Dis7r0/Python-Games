import pygame, sys, os
#importing the required modules. Note that the module pygame is not installed by default.
#install pygame and continue.
pygame.init()
 
SIZE = WIDTH, HEIGHT = 768, 512 # Intializing the size of the screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong")
 
clock = pygame.time.Clock()
fps = 60 #Setting the frame rate which governs the motion in the game
 
BLACK, WHITE = (0,0,0), (255,255,255) 
 
class Player1(pygame.sprite.Sprite): #In computer graphics, a sprite is a two-dimensional bitmap that is integrated into a larger scene.
    def __init__(self, x, y):
        super(Player1, self).__init__()
        self.image = pygame.Surface((8,64))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.score = 0
 
    def movement(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_w]:
            if self.rect.y > 0:
                self.rect.y -= 16
        if k[pygame.K_s]:
            if self.rect.y + 64 < 512:
                self.rect.y += 16
 
class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player2, self).__init__()
        self.image = pygame.Surface((8,64))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.score = 0
 
    def movement(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_UP]:
            if self.rect.y > 0:
                self.rect.y -= 16
        if k[pygame.K_DOWN]: 
            if self.rect.y + 64 < 512:
                self.rect.y += 16
 
class Ball(pygame.sprite.Sprite): #Creating the ball
    def __init__(self, x, y):
        super(Ball, self).__init__()
        self.image = pygame.Surface((8,8))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
 
        self.sx, self.sy = 8, 8
 
    def movement(self):
 
        if self.rect.y <= 0:
            self.sy *= -0.25
            self.rect.y = 0.25
        elif self.rect.y >= HEIGHT - 8:
            self.sy *= -0.25
            self.rect.y = HEIGHT - 9
 
        self.rect.x += self.sx
        self.rect.y += self.sy
 
    def collisions(self):
 
        hit_list = pygame.sprite.spritecollide(self, draw_list, False)
        if len(hit_list) > 1:
            self.sx *= -1
 
    def scoring(self):  #the score system
 
        if self.rect.x <= -16:
            p2.score += 1
            self.rect.x, self.rect.y = WIDTH/2, HEIGHT/2
            print ("Player 2's score is: ", p2.score)
        elif self.rect.x >= WIDTH + 8:
            p1.score += 1
            self.rect.x, self.rect.y = WIDTH/2, HEIGHT/2
            print ("Player 1's score is  ", p1.score)
 
        if p1.score == 10:
            print ("Player 1 wins!")
            
            
        elif p2.score == 10:
            print ("Player 2 wins!")

        if (p1.score or p2.score)>10:
            pygame.quit()
            sys.exit()
p1 = Player1(0,0)
p2 = Player2(WIDTH - 8, 0)
b = Ball(WIDTH/2, HEIGHT/2)
 
draw_list = pygame.sprite.Group()
draw_list.add(p1, p2, b)
 
while True:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # This is responsible for the game to quit when one of the players reaches the winnning score.
            pygame.quit()
            sys.exit()
   
    screen.fill(BLACK)
    draw_list.draw(screen)
    p1.movement()
    p2.movement()
    b.movement()
    b.collisions()
    b.scoring()
    pygame.display.flip()
    clock.tick(fps)
