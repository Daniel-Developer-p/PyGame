# PING - PONG
import pygame
from random import randint as rnd

pygame.init()
width = 800
height = 600

sc = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

panel_w = 330
panel_h = 35
panel_speed = 5
panel = pygame.Rect(width // 2 - panel_w//2, height - panel_h - 10, panel_w, panel_h)

ball_radius = 15
v_ball = 1
dx, dy = 1, -1
ball_rect = ball_radius * 2
ball = pygame.Rect(rnd(ball_rect, width - ball_rect), height // 2, ball_rect, ball_rect)

blocks = []
for j in range(5):
    Y = 10 + 70 * j
    for i in range(10):
        X = 10 + 120 * i
        bl = pygame.Rect(X, Y, 100, 50)
        blocks.append(bl)


def collision(dx, dy, ball, block):
    if dx > 0:
        delta_x = ball.right - block.left
    else:
        delta_x = block.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - block.top
    else:
        delta_y = block.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(pygame.Color('black'))
    pygame.draw.rect(sc, pygame.Color('darkorange'), panel)
    pygame.draw.circle(sc, pygame.Color('yellow'), ball.center, ball_radius)

    for i in range(len(blocks)):
        pygame.draw.rect(sc, pygame.Color('#000000'), blocks[i])

    flag = ball.collidelist(blocks)
    if flag != -1:
        del_block = blocks.pop(flag)
        dx, dy = collision(dx, dy, ball, del_block)

    ball.x += v_ball * dx
    ball.y += v_ball * dy

    if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
        dx = -dx
    if ball.centery < ball_radius:
        dy = -dy

    if ball.colliderect(panel) and dy > 0:
        dy = -dy

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and panel.left > 0:
        panel.left -= panel_speed
    if key[pygame.K_RIGHT] and panel.right < width:
        panel.right += panel_speed
    pygame.display.flip()
    clock.tick(60)

