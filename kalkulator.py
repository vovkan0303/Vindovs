from datetime import datetime, date
import os

import pygame
import sys
import math
import random
from button import ImageButton
from tkinter import *
import pygame, math

pygame.init()

window_height = 1920
window_width = 1080
window = pygame.display.set_mode((window_height, window_width))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class button():
    pygame.mouse.set_visible(True)
    glav = load_image('kalkucl_fon.png')
    window.blit(glav, (0, 0))

    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width + 50
        self.height = height + 50
        self.text = text
        self.over = False

    def draw(self, window, outline=None):
        if outline:
            pygame.draw.rect(window, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False


white = (255, 255, 255)
s_1s = button((153, 153, 153), 1350, 500, 30, 30, '1')
s_2s = button((153, 153, 153), 1465, 500, 30, 30, '2')
s_3s = button((153, 153, 153), 1585, 500, 30, 30, '3')
s_4s = button((153, 153, 153), 1350, 400, 30, 30, '4')
s_5s = button((153, 153, 153), 1465, 400, 30, 30, '5')
s_6s = button((153, 153, 153), 1585, 400, 30, 30, '6')
s_7s = button((153, 153, 153), 1350, 300, 30, 30, '7')
s_8s = button((153, 153, 153), 1465, 300, 30, 30, '8')
s_9s = button((153, 153, 153), 1585, 300, 30, 30, '9')
s_0s = button((153, 153, 153), 1350, 600, 30, 30, '0')

numbers = [s_1s, s_2s, s_3s, s_4s, s_5s, s_6s, s_7s, s_8s, s_9s, s_0s]

d_1s = button((255, 165, 0), 1700, 500, 30, 30, '+')
d_2s = button((255, 165, 0), 1700, 600, 30, 30, '-')
d_3s = button((255, 165, 0), 1465, 600, 30, 30, 'x')
d_4s = button((255, 165, 0), 1585, 600, 30, 30, '÷')
d_5s = button((255, 165, 0), 1700, 400, 30, 30, '=')
d_6s = button((255, 165, 0), 1700, 300, 30, 30, 'C')

symbols = [d_1s, d_2s, d_3s, d_4s, d_5s, d_6s]


def redraw(inputtap):
    for button in numbers:
        button.draw(window)

    for button in symbols:
        button.draw(window)

    inputtap.draw(window)


def Symbols():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()

        try:
            if is_finished or user_input[-1] in ["+", "-", "x", "÷", "="]:
                return
        except IndexError:
            return

        if d_1s.isOver(pos):
            user_input += "+"
            python_input += "+"

        if d_2s.isOver(pos):
            user_input += "-"
            python_input += "-"

        if d_3s.isOver(pos):
            user_input += "x"
            python_input += "*"

        if d_4s.isOver(pos):
            user_input += "÷"
            python_input += "/"

        if d_5s.isOver(pos):
            result = eval(python_input)
            python_input = ""
            user_input += f"={result:.2f}"
            is_finished = True

        if d_6s.isOver(pos):
            python_input = ""
            user_input = ""


def MOUSEOVERnumbers():
    global user_input
    global python_input
    global is_finished

    if event.type == pygame.MOUSEBUTTONDOWN:
        if is_finished:
            user_input = ""
            python_input = ""
            is_finished = False
        pos = pygame.mouse.get_pos()
        if s_1s.isOver(pos):
            user_input += "1"
            python_input += "1"
        if s_2s.isOver(pos):
            user_input += "2"
            python_input += "2"
        if s_3s.isOver(pos):
            user_input += "3"
            python_input += "3"
        if s_4s.isOver(pos):
            user_input += "4"
            python_input += "4"
        if s_5s.isOver(pos):
            user_input += "5"
            python_input += "5"
        if s_6s.isOver(pos):
            user_input += "6"
            python_input += "6"
        if s_7s.isOver(pos):
            user_input += "7"
            python_input += "7"
        if s_8s.isOver(pos):
            user_input += "8"
            python_input += "8"
        if s_9s.isOver(pos):
            user_input += "9"
            python_input += "9"
        if s_0s.isOver(pos):
            user_input += "0"
            python_input += "0"


run = True
user_input = ""
python_input = ""
is_finished = True

while run:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()
    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_58 = pygame.font.Font(ARIAL_FONT_PATH, 58)
    time_now_date = ARIAL_58.render(str(current_date), True, (0, 0, 0))
    time_now_date_rect = time_now_date.get_rect()
    time_now_date_rect.midtop = 1790, 1010
    window.blit(time_now_date, time_now_date_rect)
    inputtap = button((255, 255, 255), 1340, 140, 400, 100, f"{user_input}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)
        MOUSEOVERnumbers()
        Symbols()
        redraw(inputtap)
    pygame.display.update()
    pygame.display.flip()


pygame.quit()
