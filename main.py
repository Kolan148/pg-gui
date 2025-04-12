import pygame
from gui import *

if __name__ == "__main__":
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Pygame GUI")

    clock = pygame.time.Clock()
    b = 0
    def click():
        global b
        #btn.pos[0] += 1
        b += 1
        lbl4.text = str(b)
    #progress1 = ProgressBar(screen, 50, 50, 1000, 25, progress=75)
    widgets = []
    entry = Entry(screen, 50, 50, widgets, font=(15, "Arial Black"))
    lbl1 = Label(screen, 50, 250, '""', widgets)
    
    chk_box = CheckBox(screen, 50, 100, "ads", widgets)
    lbl2 = Label(screen, 100, 100, '0', widgets)
    
    spin_box = SpinBox(screen, 50, 150, widgets)
    lbl3 = Label(screen, 100, 150, '0', widgets)
    
    btn = Button(screen, 50, 200, "ads", click, widgets)
    lbl4 = Label(screen, 100, 200, '0', widgets)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        screen.fill((255, 255, 255))


        #for x in range(0, 100):
        #    progress1.progress = x
        #    progress1.update()
        #    pygame.display.flip()
        #    for event in pygame.event.get():
        #        if event.type == pygame.QUIT:
        #            exit()
        #    clock.tick(12)
        lbl1.text = '"'+entry.text+'"'
        lbl2.text = str(chk_box.checkt)
        lbl3.text = str(spin_box.num)
        for widget in widgets:
            widget.update()
        pygame.display.flip()

        clock.tick(30)
