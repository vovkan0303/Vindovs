import os
from datetime import datetime, date
import pygame
import sys
import math
import random
import time
from button import ImageButton

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Рабочий стол
def Windows_gl_ikr():
    size = width, height = 1920, 1080
    Windows = pygame.display.set_mode(size)
    glav = load_image('glav.png')
    # time_kn = ImageButton(1659, 995, 261, 85, '', 'data/time_kn.png', '', 'data/klik.mp3')
    shariki_kn = ImageButton(750, 200, 200, 200, '', 'data/shariki.png', 'data/shariki_p.png', 'data/klik.mp3')
    kr_nl_kn = ImageButton(1100, 500, 200, 200, '', 'data/kr_nl.png', 'data/kr_nl_p.png', 'data/klik.mp3')
    sap_kn = ImageButton(1100, 200, 200, 200, '', 'data/sap.png', 'data/sap_p.png', 'data/klik.mp3')
    spike_kn = ImageButton(1500, 500, 200, 200, '', 'data/spayk_im.png', 'data/spayk_im_p.png', 'data/klik.mp3')
    kalkul_kn = ImageButton(100, 1008, 70, 70, '', 'data/kalkul.png', 'data/kalkul_p.png', 'data/klik.mp3')
    piton_kn = ImageButton(200, 1008, 70, 70, '', 'data/piton.png', 'data/piton_p.png', 'data/klik.mp3')
    kn_m = ImageButton(7, 1008, 70, 70, '', 'data/kn_vkl.png', 'data/kn_vkl_p.png', 'data/klik.mp3')
    zm_kn = ImageButton(750, 500, 200, 200, '', 'data/zm.png', 'data/zm_p.png', 'data/klik.mp3')
    fay = load_image('fay.png')
    pygame.font.init()
    # курсор
    all_sprites = pygame.sprite.Group()
    cursor = pygame.sprite.Sprite(all_sprites)
    cursor_im = load_image("kurs.png", -1)
    cursor.image = cursor_im
    cursor.rect = cursor.image.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = date.today()
        ARIAL_FONT_PATH = pygame.font.match_font('arial')
        ARIAL_50 = pygame.font.Font(ARIAL_FONT_PATH, 50)
        ARIAL_30 = pygame.font.Font(ARIAL_FONT_PATH, 30)
        time_now = ARIAL_50.render(current_time, True, (0, 0, 0))
        time_now_date = ARIAL_30.render(str(current_date), True, (0, 0, 0))
        t_n_rect = time_now.get_rect()
        t_n_rect.midtop = 1790, 1003
        time_now_date_rect = time_now_date.get_rect()
        time_now_date_rect.midtop = 1790, 1044
        Windows.blit(glav, (0, 0))
        Windows.blit(fay, (1566, 1014))

        shariki_kn.draw(Windows)
        shariki_kn.chek_hover(pygame.mouse.get_pos())
        kr_nl_kn.draw(Windows)
        kr_nl_kn.chek_hover(pygame.mouse.get_pos())
        sap_kn.draw(Windows)
        sap_kn.chek_hover(pygame.mouse.get_pos())
        spike_kn.draw(Windows)
        spike_kn.chek_hover(pygame.mouse.get_pos())
        zm_kn.draw(Windows)
        zm_kn.chek_hover(pygame.mouse.get_pos())
        piton_kn.draw(Windows)
        piton_kn.chek_hover(pygame.mouse.get_pos())
        # может быть реализую
        # time_kn.draw(Windows)
        # time_kn.chek_hover(pygame.mouse.get_pos())
        kalkul_kn.draw(Windows)
        kalkul_kn.chek_hover(pygame.mouse.get_pos())
        kn_m.draw(Windows)
        kn_m.chek_hover(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
            shariki_kn.handle_event(event)
            kr_nl_kn.handle_event(event)
            sap_kn.handle_event(event)
            spike_kn.handle_event(event)
            zm_kn.handle_event(event)
            piton_kn.handle_event(event)
            # time_kn.handle_event(event)
            kalkul_kn.handle_event(event)
            kn_m.handle_event(event)

            if event.type == pygame.USEREVENT and event.button == kn_m:
                main_menu()
            if event.type == pygame.USEREVENT and event.button == shariki_kn:
                SHARIKI()
            if event.type == pygame.USEREVENT and event.button == kr_nl_kn:
                KR_NL()
            if event.type == pygame.USEREVENT and event.button == sap_kn:
                BOOM()
            if event.type == pygame.USEREVENT and event.button == spike_kn:
                SPIKE()
            if event.type == pygame.USEREVENT and event.button == zm_kn:
                ZM()
            if event.type == pygame.USEREVENT and event.button == piton_kn:
                piton()
            if event.type == pygame.USEREVENT and event.button == kalkul_kn:
                os.system('python kalkulator.py')
        Windows.blit(time_now_date, time_now_date_rect)
        Windows.blit(time_now, t_n_rect)

        if pygame.mouse.get_focused():
            all_sprites.draw(Windows)
        pygame.display.flip()
    pygame.quit()


# МЕНЮ ЗАПУСКА
def main_menu():
    running = True
    pygame.mouse.set_visible(True)
    WIDTH, HEIGHT = 1920, 1080

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Включение или выключения пк!")

    green_button = ImageButton(WIDTH / 4, HEIGHT / 3, 255, 300, '', 'data/zl_kn.png', 'data/zl_kn_p.png',
                               'data/vkl.mp3')
    red_button = ImageButton(WIDTH / 1.7, HEIGHT / 3, 255, 300, '', 'data/kr_kn.png', 'data/kr_kn_p.png',
                             'data/vikl.mp3')
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Включить', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(600, 700))
        screen.blit(text_surface, text_rect)
        font = pygame.font.Font(None, 72)
        text_surface = font.render('Выключить', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(1270, 700))
        screen.blit(text_surface, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == green_button:
                time.sleep(3)
                Windows_gl_ikr()
            if event.type == pygame.USEREVENT and event.button == red_button:
                time.sleep(1.5)
                quit()
            green_button.handle_event(event)
            red_button.handle_event(event)

        green_button.draw(screen)
        green_button.chek_hover(pygame.mouse.get_pos())
        red_button.chek_hover(pygame.mouse.get_pos())
        red_button.draw(screen)
        pygame.display.flip()

# Змейка
def ZM():
    snake_speed = 20
    window_x = 1920
    window_y = 1080
    black = pygame.Color(0, 0, 0)
    glav = load_image('glav.png')
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    pygame.init()
    pygame.display.set_caption('Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))
    fps = pygame.time.Clock()
    snake_position = [window_x / 2, window_y / 2]
    snake_body = [[100, 60],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    direction = 'RIGHT'
    change_to = direction
    score = 0

    def show_score(choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        game_window.blit(score_surface, score_rect)

    def game_over():
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x / 2, window_y / 4)
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        Windows_gl_ikr()

    zm = True
    while zm:
        game_window.blit(glav, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Windows_gl_ikr()
                    pygame.mouse.set_visible(False)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_d:
                    change_to = 'RIGHT'
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()
        show_score(1, white, 'times new roman', 72)
        pygame.display.update()
        fps.tick(snake_speed)

# Шарики
def SHARIKI():
    pygame.mouse.set_visible(True)

    def create_ball(x, y, list):
        speed = random.randint(10, 300)
        angle = math.radians(random.randint(1, 360))
        colr = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        size = random.randint(2, 40)
        list.append([x, y, speed, angle, colr, size])
        return list

    if __name__ == '__main__':
        pygame.init()
        startspawn = False
        width, height = 1920, 1080
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Шарики')
        balls = []
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.mouse.set_visible(False)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Windows_gl_ikr()
                        pygame.mouse.set_visible(False)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    startspawn = True
                    x, y = event.pos
                elif event.type == pygame.MOUSEMOTION:
                    if startspawn:
                        x, y = event.pos
                        balls = create_ball(x, y, balls)

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    startspawn = False
                elif event.type == pygame.KEYDOWN:
                    balls.clear()
            else:
                if startspawn:
                    balls = create_ball(x, y, balls)
            screen.fill('black')
            for ball in balls:
                x, y, speed, angle, colr, size = ball
                c = ball[4]
                s = ball[5]
                pygame.draw.circle(screen, c, (int(x), int(y)), s)
                x += speed * math.cos(angle) * (1 / 60)
                y -= speed * math.sin(angle) * (1 / 60)
                if x <= 0 or x >= width:
                    angle = math.pi - angle
                if y <= 0 or y >= height:
                    angle = -angle
                ball[0] = x
                ball[1] = y
                ball[3] = angle
            clock.tick(300)
            pygame.display.flip()
        pygame.quit()

# Крестики Нолики
def KR_NL():
    pygame.mouse.set_visible(True)
    glav = load_image('fon.png')

    def chek(mas, sign):
        zeros = 0
        for row in mas:
            zeros += row.count(0)
            if row.count(sign) == 3:
                return sign
        for col in range(3):
            if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
                return sign
            if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
                return sign
            if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
                return sign
            if zeros == 0:
                return 'Ничья'
            return False

    pygame.init()
    size_block = 270
    margin = 15
    width = height = size_block * 3 + margin * 4

    size_window = (1920, 1080)
    screen = pygame.display.set_mode(size_window)
    pygame.display.set_caption('Крестики-нолики')

    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    mas = [[0] * 3 for i in range(3)]
    query = 0
    game_over = False
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = date.today()
        ARIAL_FONT_PATH = pygame.font.match_font('arial')
        ARIAL_50 = pygame.font.Font(ARIAL_FONT_PATH, 50)
        ARIAL_30 = pygame.font.Font(ARIAL_FONT_PATH, 30)
        time_now = ARIAL_50.render(current_time, True, (0, 0, 0))
        time_now_date = ARIAL_30.render(str(current_date), True, (0, 0, 0))
        t_n_rect = time_now.get_rect()
        t_n_rect.midtop = 1790, 1003
        time_now_date_rect = time_now_date.get_rect()
        time_now_date_rect.midtop = 1790, 1044
        screen.blit(glav, (0, 0))
        screen.blit(time_now_date, time_now_date_rect)
        screen.blit(time_now, t_n_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Windows_gl_ikr()
                    pygame.mouse.set_visible(False)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse // (size_block + margin)
                row = y_mouse // (size_block + margin)
                try:
                    if mas[row][col] == 0:
                        if query % 2 == 0:
                            mas[row][col] = 'x'
                        else:
                            mas[row][col] = 'o'
                        query += 1
                except:
                    Windows_gl_ikr()
                    pygame.mouse.set_visible(False)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_over = False
                mas = [[0] * 3 for i in range(3)]
                query = 0
        if not game_over:
            for row in range(3):
                for col in range(3):
                    if mas[row][col] == 'x':
                        color = red
                    elif mas[row][col] == 'o':
                        color = green
                    else:
                        color = white
                    x = col * size_block + (col + 1) * margin
                    y = row * size_block + (row + 1) * margin
                    pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                    if color == red:
                        pygame.draw.line(screen, white, (x + 6, y + 6), (x + size_block - 6, y + size_block - 6), 8)
                        pygame.draw.line(screen, white, (x + size_block - 6, y + 6), (x + 6, y + size_block - 6), 8)
                    elif color == green:
                        pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2),
                                           size_block // 2 - 3,
                                           8)
        if (query - 1) % 2 == 0:
            game_over = chek(mas, 'x')
        else:
            game_over = chek(mas, 'o')

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('result', 80)
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])
        pygame.display.update()

#питон
def piton():
    pygame.mouse.set_visible(False)
    pygame.init()
    pygame.font.init()

    W = 1920
    H = 1080
    SCREEN_SIZE = (W, H)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_100 = pygame.font.Font(ARIAL_FONT_PATH, 100)
    TARGET_IMAGE = pygame.image.load('data/piton_l.png')
    TARGET_IMAGE = pygame.transform.scale(TARGET_IMAGE, (800, 818))
    target_rect = TARGET_IMAGE.get_rect()
    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    Windows_gl_ikr()
                    pygame.mouse.set_visible(False)
        text = ARIAL_100.render('Операционная система сделана на Python', True, (0, 0, 0))
        rect_texta = text.get_rect()
        screen.fill((150, 255, 150))
        rect_texta.midtop = W // 2, 100
        screen.blit(text, rect_texta)
        pit_l = target_rect.midtop = W // 4 + 50, H // 4
        screen.blit(TARGET_IMAGE, pit_l)
        pygame.display.flip()

# Бомблчки
def BOOM():
    pygame.mouse.set_visible(True)
    pygame.init()
    width, height = 1920, 1080
    image_size = 100, 100
    size = width, height
    screen = pygame.display.set_mode(size)
    coords = pygame.sprite.Group()

    class Bomb(pygame.sprite.Sprite):
        image = load_image("bomb2.png")
        image = pygame.transform.scale(image, image_size)
        image_boom = load_image("boom.png", -1)
        image_boom = pygame.transform.scale(image_boom, image_size)

        def __init__(self, group):
            super().__init__(group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.sound = pygame.mixer.Sound('data/boom_pl.mp3')
            self.rect.x = random.randrange(width - image_size[0])
            self.rect.y = random.randrange(height - image_size[0])
            while pygame.sprite.spritecollideany(self, coords):
                self.rect.x = random.randrange(width - image_size[0])
                self.rect.y = random.randrange(height - image_size[0])
            self.add(coords)

        def update(self, *args):
            self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.image_boom

        def get_event(self):
            if self.rect.collidepoint(event.pos):
                self.image = self.image_boom
                self.sound.play()

    all_sprites = pygame.sprite.Group()
    bomb_image = load_image("bomb2.png")
    bomb_image = pygame.transform.scale(bomb_image, image_size)
    for _ in range(100):
        Bomb(all_sprites)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    bomb.get_event()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Windows_gl_ikr()
                    pygame.mouse.set_visible(False)
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
    pygame.quit()

# Догони меня
def SPIKE():
    pygame.mouse.set_visible(True)

    def respawn_target():
        target_rect.x = random.randint(0, W - target_rect.w)
        target_rect.y = random.randint(0, H - target_rect.h)

    pygame.init()
    pygame.font.init()

    W = 1920
    H = 1080
    SCREEN_SIZE = (W, H)
    SCREEN_CENTER = (W // 2, H // 2)
    SCREEN_ESC = (W // 2, H // 2 + 200)
    SCREEN_TOP = (W // 2, 0)

    screen = pygame.display.set_mode(SCREEN_SIZE)

    FPS = 60
    clock = pygame.time.Clock()

    ARIAL_FONT_PATH = pygame.font.match_font('arial')
    ARIAL_128 = pygame.font.Font(ARIAL_FONT_PATH, 128)
    ARIAL_100 = pygame.font.Font(ARIAL_FONT_PATH, 100)
    ARIAL_64 = pygame.font.Font(ARIAL_FONT_PATH, 64)

    INIT_DELAY = 2000
    finish_delay = INIT_DELAY
    DECREASE_BASE = 1.002
    last_respawn_time = 0

    game_over = False
    RETRY_SURFACE = ARIAL_100.render('Нажми любую клавушу чтобы начать заново', True, (0, 0, 0))
    RETRY_RECT = RETRY_SURFACE.get_rect()
    RETRY_RECT.midtop = SCREEN_CENTER
    RETRY_ESC = ARIAL_128.render('Или нажми ESC чтобы выйти', True, (0, 0, 0))
    RETRY_ESC_RECT = RETRY_ESC.get_rect()
    RETRY_ESC_RECT.midtop = SCREEN_ESC
    score = 0

    TARGET_IMAGE = pygame.image.load('data/spayk.png')
    TARGET_IMAGE = pygame.transform.scale(TARGET_IMAGE, (400, 385))
    target_rect = TARGET_IMAGE.get_rect()

    respawn_target()

    running = True
    while running:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            elif i.type == pygame.KEYDOWN:
                if game_over:
                    sc = str(score)
                    l_popitka = open('data/l_p.txt', 'w')
                    l_popitka.write(f'Last attempt: {sc}')
                    record = open('data/r_sp.txt', 'r+')
                    lin = record.readline()
                    re = lin.split(': ')
                    ch_r = re[1]
                    ch_rec_in_f = int(ch_r)
                    if ch_rec_in_f < score:
                        record.seek(0, 0)
                        record.write(f'Record: {sc}')
                    l_popitka.close()
                    record.close()
                    score = 0
                    finish_delay = INIT_DELAY
                    game_over = False
                    last_respawn_time = pygame.time.get_ticks()
            elif i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == pygame.BUTTON_LEFT:
                    if not game_over and target_rect.collidepoint(i.pos):
                        score += 1
                        respawn_target()
                        last_respawn_time = pygame.time.get_ticks()
                        finish_delay = INIT_DELAY / (DECREASE_BASE ** score)
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    Windows_gl_ikr()
                    pygame.mouse.set_visible(False)
        clock.tick(FPS)
        r = open('data/r_sp.txt', 'r')
        l = open('data/l_p.txt', 'r')
        screen.fill((255, 255, 255))
        score_surface = ARIAL_128.render('Твой результат: ' + str(score), True, (0, 0, 0))
        score_posl = ARIAL_128.render(l.readline(), True, (0, 255, 0))
        score_posl_rect = score_posl.get_rect()
        score_r = ARIAL_128.render(r.readline(), True, (255, 192, 20))
        score_r_rect = score_r.get_rect()
        score_rect = score_surface.get_rect()
        score_r_rect.midtop = 290, 0
        score_posl_rect.midtop = 380, 200
        now = pygame.time.get_ticks()
        elapsed = now - last_respawn_time
        if elapsed > finish_delay:
            game_over = True
            score_rect.midbottom = SCREEN_CENTER
            screen.blit(score_posl, score_posl_rect)
            screen.blit(score_r, score_r_rect)
            screen.blit(RETRY_SURFACE, RETRY_RECT)
            screen.blit(RETRY_ESC, RETRY_ESC_RECT)
            spike = target_rect.midtop = 800, 0
            screen.blit(TARGET_IMAGE, spike)
            r.close()
            l.close()

        else:
            h = H - H * elapsed / finish_delay
            time_rect = pygame.Rect((0, 0), (W, h))
            time_rect.bottomleft = (0, H)
            pygame.draw.rect(screen, (200, 255, 200), time_rect)

            screen.blit(TARGET_IMAGE, target_rect)

            score_rect.midtop = SCREEN_TOP
        screen.blit(score_surface, score_rect)

        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
