import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    three_img = pg.image.load("ex01/fig/3.png")
    three_img = pg.transform.flip(three_img, True, False)
    threea_img = pg.transform.rotozoom(three_img, 10, 1.0)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        if tmr % 2 == 0 :
            screen.blit(three_img, [300, 200])
        if tmr % 2 == 1 :
            screen.blit(threea_img, [300, 200])
        #img_rct = three_img.get_rect()
        #img_rct.center = 300, 200
        #screen.blit(three_img, img_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()