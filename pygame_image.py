import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    three_img = pg.image.load("ex01/fig/3.png")
    three_img = pg.transform.flip(three_img, True, False)
    threea_img = pg.transform.rotozoom(three_img, 1, 1.0)
    threeb_img = pg.transform.rotozoom(three_img, 2, 1.0)
    threec_img = pg.transform.rotozoom(three_img, 3, 1.0)
    threed_img = pg.transform.rotozoom(three_img, 4, 1.0)
    #threee_img = pg.transform.rotozoom(threed_img, 2, 1.0)
    #threef_img = pg.transform.rotozoom(threea_img, 1, 1.0)
    tmr = 0
    count = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        if count >= 799 :
            screen.blit(bg_img, [0, 0])
            count = 0
        #if 1600 <= count <= 3199 :
        #    screen.blit(bg_img, [1600 - count , 0])
        #    screen.blit(bg_img, [-count, 0])
        #elif count >= 3200:
        #    count = 0
        else:
            screen.blit(bg_img, [-count, 0])

        if tmr % 10 == 0 or tmr % 10 == 9:
            screen.blit(three_img, [300, 200])
        elif tmr % 10 == 1 or tmr % 10 == 8:
            screen.blit(threea_img, [300, 200])
        elif tmr % 10 == 2 or tmr % 10 == 7:
            screen.blit(threeb_img, [300, 200])
        elif tmr % 10 == 3 or tmr % 10 == 6:
            screen.blit(threec_img, [300, 200])
        elif tmr % 10 == 4 or tmr % 10 == 5:
            screen.blit(threed_img, [300, 200])                                        
            #else:
            #    screen.blit(threeb_img, [300, 200])
        #img_rct = three_img.get_rect()
        #img_rct.center = 300, 200
        #screen.blit(three_img, img_rct)
        pg.display.update()
        tmr += 1        
        count += 1
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()