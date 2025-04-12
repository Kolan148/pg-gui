#GUI
import pygame

pygame.init()

def join(arr, sym):
    str1 = ""
    for x in arr:
        str1 += x+sym
    return str1

class Label:
    def __init__(self, surf, x, y, text, widgets, font=(12, "Calibri"), color=(0, 0, 0)):
        self.surf = surf
        self.pos = [x, y]
        self.text = text
        self.color = color
        self.fontSize = font[0]
        self.fontType = font[1]
        self.font = pygame.sysfont.SysFont(self.fontType, self.fontSize)
        widgets.append(self)
    def update(self):
        text = self.font.render(self.text, False, self.color)
        self.surf.blit(text, self.pos)
class Button:
    def __init__(self, surf, x, y, text, command, widgets, font=(12, "Calibri"), color=(200, 200, 200)):
        self.surf = surf
        self.pos = [x, y]
        self.text = text
        self.color = color
        self.fontSize = font[0]
        self.fontType = font[1]
        self.font = pygame.sysfont.SysFont(self.fontType, self.fontSize)
        self.command = command
        self.pressed = False
        widgets.append(self)
    def update(self):

        width = self.fontSize*len(self.text)
        height = self.fontSize*2

        self.rect = pygame.Rect(self.pos[0], self.pos[1], width, height)

        pressed1 = pygame.mouse.get_pressed()[0]
        
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pressed1 and not self.pressed:
            self.command()
            self.pressed = True
        if not pressed1:
            self.pressed = False
        pygame.draw.rect(self.surf, self.color, (self.pos[0], self.pos[1], self.fontSize*len(self.text), self.fontSize*2))
        text = self.font.render(self.text, False, (0, 0, 0))
        self.surf.blit(text, (self.pos[0]+self.fontSize, self.pos[1]+self.fontSize))

class Entry:
    def __init__(self, surf, x, y, widgets, font=(12, "Calibri"), color=(200, 200, 200)):
        self.surf = surf
        self.pos = [x, y]
        self.text = ""
        self.color = color
        self.fontSize = font[0]
        self.fontType = font[1]
        self.font = pygame.sysfont.SysFont(self.fontType, self.fontSize)
        self.change = False
        self.pressed = False
        widgets.append(self)
    def update(self):
        width = self.fontSize/2*(len(self.text))+10
        height = self.fontSize*2

        self.rect = pygame.Rect(self.pos[0], self.pos[1], width+20, height+20)

        pressed1 = pygame.mouse.get_pressed()[0]
        
        if pressed1:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.change = True
            else:
                self.change = False
        if self.change:
            key = pygame.key.get_pressed()
            if key[pygame.K_BACKSPACE]:
                arr_text = list(self.text)
                if len(arr_text) > 0:
                    del arr_text[-1]
                self.text = join(arr_text, "")
            if key[pygame.K_q]:
                self.text += 'q'

            elif key[pygame.K_w]:
                self.text += 'w'

            elif key[pygame.K_e]:
                self.text += 'e'

            elif key[pygame.K_r]:
                self.text += 'r'

            elif key[pygame.K_t]:
                self.text += 't'

            elif key[pygame.K_y]:
                self.text += 'y'

            elif key[pygame.K_u]:
                self.text += 'u'

            elif key[pygame.K_i]:
                self.text += 'i'

            elif key[pygame.K_o]:
                self.text += 'o'

            elif key[pygame.K_p]:
                self.text += 'p'

            elif key[pygame.K_a]:
                self.text += 'a'

            elif key[pygame.K_s]:
                self.text += 's'

            elif key[pygame.K_d]:
                self.text += 'd'

            elif key[pygame.K_f]:
                self.text += 'f'

            elif key[pygame.K_g]:
                self.text += 'g'

            elif key[pygame.K_h]:
                self.text += 'h'

            elif key[pygame.K_j]:
                self.text += 'j'

            elif key[pygame.K_k]:
                self.text += 'k'

            elif key[pygame.K_l]:
                self.text += 'l'

            elif key[pygame.K_z]:
                self.text += 'z'

            elif key[pygame.K_x]:
                self.text += 'x'

            elif key[pygame.K_c]:
                self.text += 'c'

            elif key[pygame.K_v]:
                self.text += 'v'

            elif key[pygame.K_b]:
                self.text += 'b'

            elif key[pygame.K_n]:
                self.text += 'n'

            elif key[pygame.K_m]:
                self.text += 'm'

            elif key[pygame.K_1]:
                self.text += '1'

            elif key[pygame.K_2]:
                self.text += '2'

            elif key[pygame.K_3]:
                self.text += '3'

            elif key[pygame.K_4]:
                self.text += '4'

            elif key[pygame.K_5]:
                self.text += '5'

            elif key[pygame.K_6]:
                self.text += '6'

            elif key[pygame.K_7]:
                self.text += '7'

            elif key[pygame.K_8]:
                self.text += '8'

            elif key[pygame.K_9]:
                self.text += '9'

            elif key[pygame.K_0]:
                self.text += '0'

            elif key[pygame.K_SPACE]:
                self.text += ' '
        #pygame.draw.rect(self.surf, self.color, (self.pos[0], self.pos[1], width, height))
        text = self.font.render(self.text, False, (0, 0, 0))
        #print(dir(text))
        pygame.draw.rect(self.surf, self.color, (self.pos[0], self.pos[1], text.get_width()+20, text.get_height()+20))
        self.surf.blit(text, (self.pos[0]+self.fontSize, self.pos[1]+self.fontSize))

class CheckBox:
    def __init__(self, surf, x, y, text, widgets, font=(12, "Calibri"), bg=(200, 200, 200), fg=(0, 0, 0)):
        self.surf = surf
        self.pos = [x, y]
        self.text = text
        self.bg = bg
        self.fg = fg
        self.fontSize = font[0]
        self.fontType = font[1]
        self.font = pygame.sysfont.SysFont(self.fontType, self.fontSize)
        self.checkt = False
        self.pressed = False
        widgets.append(self)
    def update(self):
        width = 15
        height = 15

        self.rect = pygame.Rect(self.pos[0], self.pos[1], width, height)

        pressed1 = pygame.mouse.get_pressed()[0]
        
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pressed1 and not self.pressed:
            self.checkt = not self.checkt
            self.pressed = True
        if not pressed1:
            self.pressed = False
        pygame.draw.rect(self.surf, self.bg, (self.pos[0], self.pos[1], width, height))

        if self.checkt:
            pygame.draw.rect(self.surf, (0, 0, 0), (self.pos[0]+5, self.pos[1]+5, 5, 5))
        
        text = self.font.render(self.text, False, self.fg)
        self.surf.blit(text, (self.pos[0]+20, self.pos[1]))

class SpinBox:
    def __init__(self, surf, x, y, widgets, font=(12, "Calibri"), bg=(200, 200, 200), fg=(0, 0, 0)):
        self.surf = surf
        self.pos = [x, y]
        self.num = 0
        self.bg = bg
        self.fg = fg
        self.fontSize = font[0]
        self.fontType = font[1]
        self.font = pygame.sysfont.SysFont(self.fontType, self.fontSize)
        widgets.append(self)
    def update(self):
        width = self.fontSize/2*len(str(self.num))
        height = self.fontSize*2

        width1 = 15
        height1 = 15

        width2 = 15
        height2 = 15
        
        self.rect1 = pygame.Rect(self.pos[0]+width, self.pos[1], width1, height1)

        self.rect2 = pygame.Rect(self.pos[0]+width, self.pos[1]+height2, width2, height2)

        pressed1 = pygame.mouse.get_pressed()[0]
        
        if self.rect1.collidepoint(pygame.mouse.get_pos()) and pressed1:
            self.num += 1
        if self.rect2.collidepoint(pygame.mouse.get_pos()) and pressed1:
            self.num -= 1
        
        pygame.draw.rect(self.surf, self.bg, (self.pos[0], self.pos[1], width, height))

        pygame.draw.rect(self.surf, self.bg, self.rect1, 3)

        pygame.draw.rect(self.surf, self.bg, self.rect2, 3)

        
        text = self.font.render(str(self.num), False, self.fg)
        self.surf.blit(text, (self.pos[0], self.pos[1]))

class ProgressBar:
    def __init__(self, surf, x, y, width, height, widgets, progress=0, bg=(200, 200, 200), pg=(0, 255, 0)):
        self.surf = surf
        self.pos = [x, y]
        self.width = width
        self.height = height
        self.num = 0
        self.bg = bg
        self.pg = pg
        self.progress = progress
        widgets.append(self)
    def update(self):
        width1 = self.width/100*self.progress
        pygame.draw.rect(self.surf, self.bg, (self.pos[0], self.pos[1], self.width, self.height))
        pygame.draw.rect(self.surf, self.pg, (self.pos[0], self.pos[1], width1, self.height))
