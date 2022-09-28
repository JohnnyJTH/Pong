import pygame
from ball import Ball
from paddle import Paddle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = (700, 500)

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(10, 10)
ball.rect.x = 345
ball.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

game_loop = True
bounceable = True
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

while game_loop:
    for event in pygame.event.get():
        if event.type != pygame.QUIT and event.type == pygame.KEYDOWN and event.key == pygame.K_x or event.type == pygame.QUIT:
            game_loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
        bounceable = False
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
        bounceable = False
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    if (
        pygame.sprite.collide_mask(ball, paddleA)
        or pygame.sprite.collide_mask(ball, paddleB)
    ) and bounceable:
        ball.bounce()

    if ball.rect.x > 340 and ball.rect.x < 460:
        bounceable = True

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

    all_sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
