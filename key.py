import pygame as pg
from pygame.math import Vector2

pg.font.init()
font = pg.font.Font('Assets/Fonts/Jetbrains_Mono.ttf', 10)


class Key:
    keys = []

    @staticmethod
    def draw_all(screen):
        for key in Key.keys:
            key.draw(screen)

    def __init__(self, pos: Vector2, size: Vector2, id, text_low, text_high=None):
        self.id = id
        self.pos = pos
        self.size = size
        self.rect = pg.Rect(*tuple(self.pos), *tuple(self.size*45))

        if text_high is None:
            self.txt = font.render(text_low, True, '#ffffff')
            self.txt_rect = self.txt.get_rect(center=self.rect.center)
            self.shifty = False
        else:
            self.ttxt = font.render(text_high, True, '#ffffff')
            self.ttxt_rect = self.ttxt.get_rect(center=self.rect.center + Vector2(0, -8))
            self.ltxt = font.render(text_low, True, '#ffffff')
            self.ltxt_rect = self.ltxt.get_rect(center=self.rect.center + Vector2(0, 8))
            self.shifty = True

        self.keys.append(self)

    def draw(self, screen):
        color = '#0f0f0f'
        if self.id is not None:
            if pg.key.get_pressed()[self.id]:
                color = '#666666'

        pg.draw.rect(screen, color, self.rect, 0, 3)
        pg.draw.rect(screen, '#666666', self.rect, 2, 3)
        if not self.shifty:
            screen.blit(self.txt, self.txt_rect)
        else:
            screen.blit(self.ttxt, self.ttxt_rect)
            screen.blit(self.ltxt, self.ltxt_rect)

