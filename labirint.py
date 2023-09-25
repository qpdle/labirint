from pygame import *
display.set_caption("qpdle")
window = display.set_mode((700, 500))
back = (190, 190, 190)
window.fill(back)
pic = transform.scale(image.load('jungle.png'), (700, 500))
run = True
card = (190, 0, 0)

class GameSprite(sprite.Sprite):
     def __init__(self, picture, w, h, x, y):
          super().__init__()
          self.image = transform.scale(image.load(picture), (w, h))
          self.rect = self.image.get_rect()
          self.rect.x = x
          self.rect.y = y
     def reset(self):
          window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
     def __init__(self, picture, w, h, x, y, x_speed, y_speed):
          super().__init__(picture, w, h, x, y)
          self.x_speed = x_speed
          self.y_speed = y_speed
     def update(self):
          self.rect.x += self.x_speed
          self.rect.y += self.y_speed
          if self.rect.x > 0 and self.x_speed < 0 or self.rect.x<700-80 and self.x_speed > 0:
               self.rect.x += self.x_speed
          if self.rect.y >0 and self.rect.y >0 or self.rect.y < 500-80 and self.y_speed > 0:
               self.rect.y += self.y_speed


class Card():
     def __init__(self, weight, hight, x, y, color):
          super().__init__()
          self.fillcolor=color
          self.rect=Rect(x, y, weight, hight)
     def draw(self):
          draw.rect(window, self.fillcolor, self.rect)

final = GameSprite('trophy.png', 80, 80, 600, 400)
final.reset()

BLUE = (190, 190, 190)
#player1 = Card(8, 80, 100, 150, BLUE)
wall_1 = GameSprite('wall.png', 200, 180, 200, 250)

wall_2 = GameSprite('wall.png', 300, 240, 100, 90)

wall_3 = GameSprite('wall.png', 400, 100, 40, 380)

player = Player('pacp.png', 60, 60, 0, 0, 0, 0)
player.reset()
#player1.draw()
#player2 = Pic('osenlist.png', 80, 80, 200, 250)
#player2.reset()
#player2.draw()
wrag = Player('wrag.png', 60, 60, 230, 40, 0, 0)
wrag.reset()

finish=False
win = transform.scale(image.load('winner_1.jpg'), (700, 500))
lose = transform.scale(image.load('lose.jpg'), (700, 500))
while run:
     time.delay(50)
    # window.blit(pic, (0, 0))
    # wall_1.reset()
    # wall_2.reset()
    # wall_3.reset()
     for e in event.get():
          if e.type == QUIT:
               run = False
          elif e.type == KEYDOWN:
               if e.key == K_w:
                    player.y_speed = -5
               if e.key == K_s:
                    player.y_speed = 5
               if e.key == K_a:
                    player.x_speed = -5
               if e.key == K_d:
                    player.x_speed = 5
          elif e.type == KEYUP:
               if e.key == K_w:
                    player.y_speed = 0
               if e.key == K_s:
                    player.y_speed = 0
               if e.key == K_a:
                    player.x_speed = 0
               if e.key == K_d:
                    player.x_speed = 0
     if finish != True:
          window.blit(pic, (0, 0))
          player.update()
          player.reset()
          wall_1.reset()
          wall_2.reset()
          wall_3.reset()
          final.reset()
          wrag.reset()
          if sprite.collide_rect(player, final):
               finish = True
               window.blit(win, (0, 0))
          if sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wrag):
               finish = True
               window.blit(lose, (0, 0))

     
     display.update()

