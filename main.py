import pygame as pg
from sys import exit
from pygame.math import Vector2

from key import Key

pg.init()
screen = pg.display.set_mode((700, 280))
pg.display.set_caption("Keyboard")

x_offset = 0
y_offset = 0

k_names = [
    ['esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', '^'],
    ['`ß~', '1ß!', '2ß@', '3ß#', '4ß$', '5ß%', '6ß^', '7ß&', '8ß*', '9ß(', '0ß)', '-ß_', '=ß+', 'delete'],
    ['tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[ß{', ']ß}', '\\'],
    ['capslock', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';ß:', "'ß\"", 'return'],
    ['shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',ß<', '.ß>', '/ß?', 'shift'],
    ['fn', 'ctrl', 'alt', 'cmd', 'space', 'cmd', 'alt'],
    ['▲', '◀', '▼', '▶']
]

k_ids = [
    [pg.K_ESCAPE, pg.K_F1, pg.K_F2, pg.K_F3, pg.K_F4, pg.K_F5, pg.K_F6, pg.K_F7, pg.K_F8, pg.K_F9, pg.K_F10, pg.K_F11, pg.K_F12, None],
    [pg.K_BACKQUOTE, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9, pg.K_0, pg.K_MINUS,
     pg.K_EQUALS, pg.K_BACKSPACE],
    [pg.K_TAB, pg.K_q, pg.K_w, pg.K_e, pg.K_r, pg.K_t, pg.K_y, pg.K_u, pg.K_i, pg.K_o, pg.K_p, pg.K_LEFTBRACKET,
     pg.K_RIGHTBRACKET, pg.K_BACKSLASH],
    [pg.K_CAPSLOCK, pg.K_a, pg.K_s, pg.K_d, pg.K_f, pg.K_g, pg.K_h, pg.K_j, pg.K_k, pg.K_l, pg.K_SEMICOLON, pg.K_QUOTE, pg.K_RETURN],
    [pg.K_LSHIFT, pg.K_z, pg.K_x, pg.K_c, pg.K_v, pg.K_b, pg.K_n, pg.K_m, pg.K_COMMA, pg.K_PERIOD, pg.K_SLASH,
     pg.K_RSHIFT],
    [None, pg.K_LCTRL, pg.K_LALT, pg.K_LMETA, pg.K_SPACE, pg.K_RMETA, pg.K_RALT],
    [pg.K_UP, pg.K_LEFT, pg.K_DOWN, pg.K_RIGHT]
]

# Key Instantiation ----
[Key(Vector2(2 + x_offset + i*50, 5 + y_offset), Vector2(1, 0.5), k_ids[0][i], k_names[0][i]) for i in range(14)]

[Key(Vector2(2 + x_offset + i * 48, 27 + 5 + y_offset), Vector2(1, 1), k_ids[1][i], *k_names[1][i].split('ß'))
 for i in range(13)]
Key(Vector2(2 + x_offset + 13 * 48, 27 + 5 + y_offset), Vector2(1.57, 1), k_ids[1][13], k_names[1][13])

Key(Vector2(2 + x_offset + 0 * 48, 27 + (1*50) + 5 + y_offset), Vector2(1.57, 1), k_ids[2][0], k_names[2][0])
[Key(Vector2(28 + x_offset + (i+1) * 48, 27 + (1*50) + 5 + y_offset), Vector2(1, 1), k_ids[2][i+1],
     *k_names[2][i+1].split('ß')) for i in range(13)]

Key(Vector2(2 + x_offset + 0 * 48, 27 + (2*50) + 5 + y_offset), Vector2(1.9, 1), k_ids[3][0], k_names[3][0])
[Key(Vector2(-6 + x_offset + (i+2) * 48, 27 + (2*50) + 5 + y_offset), Vector2(1, 1), k_ids[3][i+1],
     *k_names[3][i+1].split('ß'))
 for i in range(11)]
Key(Vector2(-6 + x_offset + 13 * 48, 27 + (2*50) + 5 + y_offset), Vector2(1.75, 1), k_ids[3][12],
    *k_names[3][12].split('ß'))

Key(Vector2(2 + x_offset + 0 * 48, 27 + (3*50) + 5 + y_offset), Vector2(2.4, 1), k_ids[4][0], k_names[4][0])
[Key(Vector2(17 + x_offset + (i+2) * 48, 27 + (3*50) + 5 + y_offset), Vector2(1, 1), k_ids[4][i+1],
     *k_names[4][i+1].split('ß'))
 for i in range(10)]
Key(Vector2(17 + x_offset + 12 * 48, 27 + (3*50) + 5 + y_offset), Vector2(2.3, 1), k_ids[4][11],
    *k_names[4][11].split('ß'))

[Key(Vector2(2 + x_offset + i * 50, 27 + (4*50) + 5 + y_offset), Vector2(1, 1), k_ids[5][i], k_names[5][i])
 for i in range(3)]
Key(Vector2(2 + x_offset + 3 * 50, 27 + (4*50) + 5 + y_offset), Vector2(1.2, 1), k_ids[5][3], k_names[5][3])
Key(Vector2(10 + x_offset + 4 * 50, 27 + (4*50) + 5 + y_offset), Vector2(5.25, 1), k_ids[5][4], k_names[5][4])
Key(Vector2(17 + x_offset + 9 * 48, 27 + (4*50) + 5 + y_offset), Vector2(1.2, 1), k_ids[5][5], k_names[5][5])
Key(Vector2(26 + x_offset + 10 * 48, 27 + (4*50) + 5 + y_offset), Vector2(1, 1), k_ids[5][6], k_names[5][6])

Key(Vector2(26 + x_offset + 12 * 48, 27 + (4*50) + 5 + y_offset), Vector2(1, 0.5), k_ids[6][0], k_names[6][0])
Key(Vector2(26 + x_offset + 11 * 48, 27 + (4*50) + 28 + y_offset), Vector2(1, 0.5), k_ids[6][1], k_names[6][1])
Key(Vector2(26 + x_offset + 12 * 48, 27 + (4*50) + 28 + y_offset), Vector2(1, 0.5), k_ids[6][2], k_names[6][2])
Key(Vector2(26 + x_offset + 13 * 48, 27 + (4*50) + 28 + y_offset), Vector2(1, 0.5), k_ids[6][3], k_names[6][3])
# ----------------------
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.fill('#0f0f0f')
    Key.draw_all(screen)
    pg.display.flip()
