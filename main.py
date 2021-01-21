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
panel_speed = 15
panel = pygame.Rect(width // 2 - panel_w//2, height - panel_h - 10, panel_w, panel_h)

ball_radius = 15
v_ball = 1
dx, dy = 1, -1
ball_rect = ball_radius * 2
ball = pygame.Rect(rnd(ball_rect, width - ball_rect), height // 2, ball_rect, ball_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(pygame.Color('black'))
    pygame.draw.rect(sc, pygame.Color('darkorange'), panel)
    pygame.draw.circle(sc, pygame.Color('yellow'), ball.center, ball_radius)
    ball.x += v_ball * dx
    ball.y += v_ball * dy

    if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
        dx = -dx
    if ball.centerx < ball_radius or ball.centerx > height - ball_radius:
        dx = -dx

    blocks = []
    for j in range(5):
        Y = 10+70*j
        for i in range(10):
            X = 10 + 120*i
            bl = pygame.Rect(X, Y, 100, 50)
            blocks.append(bl)

    if key[pygame.K_LEFT] and panel.left > 0:
        panel.left -= panel_speed
    if key[pygame.K_RIGHT] and panel.right < width:
        panel.right += panel_speed
    pygame.display.flip()
    clock.tick(60)

