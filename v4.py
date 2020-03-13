import math
import pygame as pg
import random
from random import randrange
import os
import time
pg.mixer.pre_init(44100, -16, 1, 512)
pg.init()
background = pg.image.load('starfield.png')
background_rect = background.get_rect()

class Enemy:
    def __init__(self, images, screen_rect, start_pos,lives):
        self.screen_rect = screen_rect
        self.image = images[0]
        self.mask = images[1]
        start_buffer = 0
        self.coll = False
        self.rect = self.image.get_rect(
            center=(start_pos[0], start_pos[1]+120)
        )
        self.rect_left = self.image.get_rect(
            center=(start_pos[0]-40, start_pos[1]+10)
        )
        self.rect_right = self.image.get_rect(
            center=(start_pos[0]+40, start_pos[1]+10)
        )
        self.distance_above_player = 100
        self.speed = 4
        self.bullet_color = (255, 0, 0)
        self.is_hit = False
        self.range_to_fire = False
        self.timer = 0.0
        self.timer2 = 0.0
        self.timer3 = 0.0
        self.bullets = []
        self.dead = False
        self.health = lives
        self.attack = True

    def pos_towards_player(self, player_rect):
        c = math.sqrt(
            (player_rect.x+80 - self.rect.x) ** 2 + (player_rect.y - self.distance_above_player - self.rect.y) ** 2)
        try:
            x = (2*(player_rect.x - self.rect.x) / c)
            y = ((player_rect.y - self.distance_above_player)  - self.rect.y) / c
        except ZeroDivisionError:
            return False
        return (x, y)

    def update(self, dt, player):
        if self.health <= 0:
            self.attack = False
            if pg.time.get_ticks() - self.timer3 > 1150.0:
                self.image = pg.image.load('tile022.png')
                self.image = pg.transform.scale(self.image, (100, 100))
                self.dead = True
            elif pg.time.get_ticks() - self.timer3 > 1100.0:
                self.image = pg.image.load('tile021.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 1050.0:
                self.image = pg.image.load('tile020.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 1000.0:
                self.image = pg.image.load('tile019.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 900.0:
                self.image = pg.image.load('tile018.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 850.0:
                self.image = pg.image.load('tile017.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 800.0:
                self.image = pg.image.load('tile016.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 750.0:
                self.image = pg.image.load('tile015.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 700.0:
                self.image = pg.image.load('tile014.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 650.0:
                self.image = pg.image.load('tile013.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 600.0:
                self.image = pg.image.load('tile012.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 550.0:
                self.image = pg.image.load('tile011.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 500.0:
                self.image = pg.image.load('tile010.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 450.0:
                self.image = pg.image.load('tile009.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 400.0:
                self.image = pg.image.load('tile008.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 350.0:
                self.image = pg.image.load('tile007.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 300.0:
                self.image = pg.image.load('tile006.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 250.0:
                self.image = pg.image.load('tile005.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 200.0:
                self.image = pg.image.load('tile004.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 150.0:
                self.image = pg.image.load('tile003.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 100.0:
                self.image = pg.image.load('tile002.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 50.0:
                self.image = pg.image.load('tile001.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 0.0:
                self.image = pg.image.load('tile000.png')
                self.image = pg.transform.scale(self.image, (100, 100))
        else:
            self.timer3 = pg.time.get_ticks()

        new_pos = self.pos_towards_player(player.rect)
        if new_pos and self.rect.y < 50:
            self.rect.x ,self.rect.y = (self.rect.x + new_pos[0] * self.speed,self.rect.y + new_pos[1] * self.speed)
            self.rect_left.x, self.rect_left.y = (self.rect.x-40 + new_pos[0] * self.speed, self.rect.y-50 + new_pos[1] * self.speed)
            self.rect_right.x, self.rect_right.y = (self.rect.x+40 + new_pos[0] * self.speed, self.rect.y-50 + new_pos[1] * self.speed)
        elif new_pos:
            self.rect.x, self.rect.y = (self.rect.x + new_pos[0] * self.speed, 50)
            self.rect_left.x, self.rect_left.y = (self.rect.x-40 + new_pos[0] * self.speed, 0)
            self.rect_right.x, self.rect_right.y = (self.rect.x+40 + new_pos[0] * self.speed, 0)
        self.check_attack_ability(player)

        if self.rect.y <= player.rect.y+80 and self.rect.y >= player.rect.y-80 and self.rect.x <= player.rect.x + 60 and self.rect.x >= player.rect.x - 100 and self.coll == False:
            self.coll = True
            player.take_damage(5)
            self.timer2 = pg.time.get_ticks()
        if pg.time.get_ticks() - self.timer2 > 1000.0:
            self.coll = False

        if self.range_to_fire:
            if pg.time.get_ticks() - self.timer > 1500.0:
                self.timer = pg.time.get_ticks()
                self.bullets.append(Laser(self.rect.center, self.bullet_color,0))
                self.bullets.append(Laser(self.rect_left.center, self.bullet_color,0))
                self.bullets.append(Laser(self.rect_right.center, self.bullet_color,0))
        self.update_bullets(player)

    def draw(self, surf):
        if self.bullets:
            for bullet in self.bullets:
                surf.blit(bullet.image, bullet.rect)
        if self.health > 0:
            surf.blit(self.image, self.rect)
        elif self.health <=0:
            surf.blit(self.image, (self.rect.x+20,self.rect.y+40))

    def check_attack_ability(self, player):
        # if player is lower than enemy
        if self.attack == True:
            if player.rect.y >= self.rect.y:
                try:
                    offset_x = self.rect.x - player.rect.x
                    offset_y = self.rect.y - player.rect.y
                    d = int(math.degrees(math.atan(offset_x / offset_y)))
                except ZeroDivisionError:  # player is above enemy
                    return
                # if player is within 15 degrees lower of enemy
                if math.fabs(d) <= 15:
                    self.range_to_fire = True
                else:
                    self.range_to_fire = False
        else:
            self.range_to_fire = False

    def update_bullets(self, player):
        if self.bullets:
            for obj in self.bullets:
                obj.update('down')
                if obj.rect.colliderect(player.rect):
                    offset_x = obj.rect.x - player.rect.x
                    offset_y = obj.rect.y - player.rect.y
                    if player.mask.overlap(obj.mask, (offset_x, offset_y)):
                        player.take_damage(1)
                        self.bullets.remove(obj)

class Enemy_1:
    def __init__(self, images, screen_rect, start_pos,lives):
        self.screen_rect = screen_rect
        self.image = images[0]
        self.mask = images[1]
        start_buffer = 0
        self.coll = False
        self.rect = self.image.get_rect(
            center=(start_pos[0], start_pos[1]+120)
        )
        self.rect_left = self.image.get_rect(
            center=(start_pos[0]-40, start_pos[1]+10)
        )
        self.rect_right = self.image.get_rect(
            center=(start_pos[0]+40, start_pos[1]+10)
        )
        self.distance_above_player = 0
        self.speed = 2
        self.bullet_color = (255, 0, 0)
        self.is_hit = False
        self.range_to_fire = False
        self.timer = 0.0
        self.timer2 = 0.0
        self.timer3 = 0.0
        self.bullets = []
        self.dead = False
        self.health = lives
        self.attack = True

    def pos_towards_player(self, player_rect):
        c = math.sqrt(
            (player_rect.x+100 - self.rect.x) ** 2 + (player_rect.y - self.distance_above_player - self.rect.y) ** 2)
        try:
            x = (2*(player_rect.x - self.rect.x) / c)
            y = ((player_rect.y - self.distance_above_player)  - self.rect.y) / c
        except ZeroDivisionError:
            return False
        return (x, y)

    def update(self, dt, player):
        if self.health <= 0:
            self.attack = False
            if pg.time.get_ticks() - self.timer3 > 1150.0:
                self.image = pg.image.load('tile022.png')
                self.image = pg.transform.scale(self.image, (100, 100))
                self.dead = True
            elif pg.time.get_ticks() - self.timer3 > 1100.0:
                self.image = pg.image.load('tile021.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 1050.0:
                self.image = pg.image.load('tile020.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 1000.0:
                self.image = pg.image.load('tile019.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 900.0:
                self.image = pg.image.load('tile018.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 850.0:
                self.image = pg.image.load('tile017.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 800.0:
                self.image = pg.image.load('tile016.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 750.0:
                self.image = pg.image.load('tile015.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 700.0:
                self.image = pg.image.load('tile014.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 650.0:
                self.image = pg.image.load('tile013.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 600.0:
                self.image = pg.image.load('tile012.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 550.0:
                self.image = pg.image.load('tile011.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 500.0:
                self.image = pg.image.load('tile010.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 450.0:
                self.image = pg.image.load('tile009.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 400.0:
                self.image = pg.image.load('tile008.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 350.0:
                self.image = pg.image.load('tile007.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 300.0:
                self.image = pg.image.load('tile006.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 250.0:
                self.image = pg.image.load('tile005.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 200.0:
                self.image = pg.image.load('tile004.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 150.0:
                self.image = pg.image.load('tile003.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 100.0:
                self.image = pg.image.load('tile002.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 50.0:
                self.image = pg.image.load('tile001.png')
                self.image = pg.transform.scale(self.image, (100, 100))
            elif pg.time.get_ticks() - self.timer3 > 0.0:
                self.image = pg.image.load('tile000.png')
                self.image = pg.transform.scale(self.image, (100, 100))
        else:
            self.timer3 = pg.time.get_ticks()

        new_pos = self.pos_towards_player(player.rect)
        self.rect.x, self.rect.y = (self.rect.x + new_pos[0] * self.speed, self.rect.y + new_pos[1] * self.speed)
        self.rect_left.x, self.rect_left.y = (
        self.rect.x - 40 + new_pos[0] * self.speed, self.rect.y - 50 + new_pos[1] * self.speed)
        self.rect_right.x, self.rect_right.y = (
        self.rect.x + 40 + new_pos[0] * self.speed, self.rect.y - 50 + new_pos[1] * self.speed)
        self.check_attack_ability(player)

        if self.rect.y <= player.rect.y + 80 and self.rect.y >= player.rect.y - 80 and self.rect.x <= player.rect.x + 60 and self.rect.x >= player.rect.x - 100 and self.coll == False:
            self.coll = True
            player.take_damage(5)
            self.timer2 = pg.time.get_ticks()
        if pg.time.get_ticks() - self.timer2 > 1000.0:
            self.coll = False

        if self.range_to_fire:
            if pg.time.get_ticks() - self.timer > 1500.0:
                self.timer = pg.time.get_ticks()
                self.bullets.append(Laser(self.rect.center, self.bullet_color,0))
                self.bullets.append(Laser(self.rect_left.center, self.bullet_color,0))
                self.bullets.append(Laser(self.rect_right.center, self.bullet_color,0))
        self.update_bullets(player)

    def draw(self, surf):
        if self.bullets:
            for bullet in self.bullets:
                surf.blit(bullet.image, bullet.rect)
        if self.health > 0:
            surf.blit(self.image, self.rect)
        elif self.health <= 0:
            surf.blit(self.image, (self.rect.x+20, self.rect.y + 40))

    def check_attack_ability(self, player):
        # if player is lower than enemy
        if self.attack == True:
            if player.rect.y >= self.rect.y:
                try:
                    offset_x = self.rect.x - player.rect.x
                    offset_y = self.rect.y - player.rect.y
                    d = int(math.degrees(math.atan(offset_x / offset_y)))
                except ZeroDivisionError:  # player is above enemy
                    return
                # if player is within 15 degrees lower of enemy
                if math.fabs(d) <= 15:
                    self.range_to_fire = True
                else:
                    self.range_to_fire = False
        else:
            self.range_to_fire = False

    def update_bullets(self, player):
        if self.bullets:
            for obj in self.bullets:
                obj.update('down')
                if obj.rect.colliderect(player.rect):
                    offset_x = obj.rect.x - player.rect.x
                    offset_y = obj.rect.y - player.rect.y
                    if player.mask.overlap(obj.mask, (offset_x, offset_y)):
                        player.take_damage(1)
                        self.bullets.remove(obj)

class Soldier:
    def __init__(self, images, screen_rect, start_pos,lives,speed):
        self.screen_rect = screen_rect
        self.image = images[0]
        self.mask = images[1]
        start_buffer = 0
        self.rect = self.image.get_rect(
            center=(start_pos[0], start_pos[1])
        )
        self.distance_above_player = 100
        self.speed = speed
        self.bullet_color = (255, 0, 0)
        self.is_hit = False
        self.range_to_fire = False
        self.timer = 0.0
        self.bullets = []
        self.dead = False
        self.health = lives
        self.attack = True


    def update(self, dt, player):
        self.rect.x += self.speed
        if self.attack == False:
            self.dead = True
        if self.rect.x > 750 - 50:
            self.rect.y += 75
            self.speed = -self.speed
        if self.rect.x <= 0 and self.rect.y >= 50:
            self.speed = -self.speed
            self.rect.y += 75
        if self.rect.y >= 450 and self.rect.x == 650:
            player.take_damage(1)
            player.score -= 25
            self.dead = True
        if self.rect.y <= player.rect.y+40 and self.rect.y >= player.rect.y-40 and self.rect.x <= player.rect.x + 20 and self.rect.x >= player.rect.x - 100:
            self.dead = True
            player.take_damage(2)
        self.check_attack_ability(player)
        if self.range_to_fire:
            if pg.time.get_ticks() - self.timer > 1500.0:
                self.timer = pg.time.get_ticks()
                self.bullets.append(Laser(self.rect.center, self.bullet_color,0))
        self.update_bullets(player)



    def draw(self, surf):
        if self.bullets:
            for bullet in self.bullets:
                surf.blit(bullet.image, bullet.rect)
        surf.blit(self.image, self.rect)

    def take_damage(self, value):
        self.health -= value

    def check_attack_ability(self, player):
        # if player is lower than enemy
        if player.rect.x <= self.rect.x + 10 and player.rect.x >= self.rect.x - 10 and player.rect.y >= self.rect.y:
            self.range_to_fire = True
        else:
            self.range_to_fire = False

    def update_bullets(self, player):
        if self.bullets:
            for obj in self.bullets:
                obj.update('down')
                if obj.rect.colliderect(player.rect):
                    offset_x = obj.rect.x - player.rect.x
                    offset_y = obj.rect.y - player.rect.y
                    if player.mask.overlap(obj.mask, (offset_x, offset_y)):
                        player.take_damage(1)
                        self.bullets.remove(obj)

class Power_Up:
    def __init__(self, images, screen_rect, start_pos,nr):
        self.screen_rect = screen_rect
        self.image = images[0]
        self.mask = images[1]
        start_buffer = 0
        self.health = 3
        self.nr = nr
        self.rect = self.image.get_rect(
            center=(start_pos[0], start_pos[1])
        )
        self.distance_above_player = 100
        self.speed = 2
        self.bullet_color = (255, 0, 0)
        self.timer = 0.0
        self.dead = False

    def update(self, dt, player):
        self.rect.y += self.speed
        if self.rect.y >= 800:
            self.dead = True
        if self.rect.y <= player.rect.y+40 and self.rect.y >= player.rect.y-40 and self.rect.x <= player.rect.x + 60 and self.rect.x >= player.rect.x - 40:
            if self.nr == 0:
                player.add_damage(10)
                player.score -= 25
                self.dead = True
            elif self.nr == 1:
                player.laser_add_delay(50)
                player.score -= 25
                self.dead = True
            elif self.nr == 2:
                player.add_player_dmg()
                player.score -= 25
                self.dead = True
            elif self.nr == 3:
                player.add_player_lives()
                player.score -= 25
                self.dead = True


    def draw(self, surf):
        surf.blit(self.image, self.rect)


class Laser:
    def __init__(self, loc, screen_rect,nr):
        self.screen_rect = screen_rect
        if nr == 0:
            self.image = pg.image.load("laser.png")
        elif nr == 1:
            self.image = pg.image.load("electro_trans.png")
            self.image = pg.transform.scale(self.image, (60, 80))
            self.image = pg.transform.rotate(self.image, 145)
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=loc)
        self.speed = 5
    def update(self,direction='up'):
        if direction == 'down':
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

        #if self.rect.bottom < self.screen_rect.top:   -   limit
        #    return True

    def render(self, surf):
        surf.blit(self.image, self.rect)

class Player:
    def __init__(self, screen_rect):
        self.screen_rect = screen_rect
        self.image_ship = pg.image.load('ship.png')  # create player.image attribute
        self.image = pg.transform.scale(self.image_ship, (60, 80))
        self.image.set_colorkey((255, 0, 255))
        self.mask = pg.mask.from_surface(self.image)
        start_buffer = 300
        self.rect = self.image.get_rect(
            center=(screen_rect.centerx, screen_rect.centery + start_buffer)
        )
        self.dx = 300
        self.dy = 300
        self.lasers = []
        self.timer = 0.0
        self.laser_delay = 500
        self.add_laser = False
        self.damage = 10
        self.player_damage = 1
        self.player_laser_damage = 1
        self.score = 0
        self.dead = False
        self.lives = 2

    def take_damage(self, value):
        self.damage -= value
        TOOLS.update_damage(self.damage)

    def add_damage(self, value):
        self.damage += value
        TOOLS.update_damage(self.damage)

    def add_player_dmg(self):
        self.player_damage += 1

    def laser_add_delay(self, value):
        self.laser_delay -= value
        if self.laser_delay <= 100:
            self.lasr_delay = 100

    def add_player_lives(self):
        self.lives += 1
        TOOLS.update_lives(self.lives)

    def lose_live(self):
        self.lives -= 1
        self.damage = 10
        if self.player_damage > 1:
            self.player_damage -= 1
        if self.player_laser_damage > 1:
            self.player_laser_damage -= 1
        self.rect.x = 370
        self.rect.y = 800
        TOOLS.update_damage(self.damage)
        TOOLS.update_lives(self.lives)

    def get_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if self.add_laser:
                    if self.player_damage == 1:
                        self.lasers.append(Laser(self.rect.center, self.screen_rect,0))
                        self.add_laser = False
                    elif self.player_damage == 2:
                        self.lasers.append(Laser((self.rect.x + 60,self.rect.y), self.screen_rect,0))
                        self.lasers.append(Laser((self.rect.x ,self.rect.y), self.screen_rect,0))
                        self.add_laser = False
                    elif self.player_damage == 3:
                        self.lasers.append(Laser(self.rect.center, self.screen_rect,0))
                        self.lasers.append(Laser((self.rect.x + 60,self.rect.y), self.screen_rect,0))
                        self.lasers.append(Laser((self.rect.x ,self.rect.y), self.screen_rect,0))
                        self.add_laser = False
                    elif self.player_damage >= 4:
                        self.player_laser_damage = 2
                        self.lasers.append(Laser((self.rect.x + 57, self.rect.y), self.screen_rect, 1))
                        self.lasers.append(Laser((self.rect.x, self.rect.y), self.screen_rect, 1))
                        self.add_laser = False

    def update(self, keys, dt, enemies):
        if self.rect.y <= 550:
            self.rect.clamp_ip(self.screen_rect)
        if self.rect.y > 551:
            self.rect.y -= 6
            self.damage = 10

        if keys[pg.K_LEFT]:
            self.rect.x -= self.dx * dt
        if keys[pg.K_RIGHT]:
            self.rect.x += self.dx * dt
        if keys[pg.K_UP]:
            self.rect.y -= self.dy * dt
        if keys[pg.K_DOWN]:
            self.rect.y += self.dy * dt
        for laser in self.lasers:
            laser.update()

        if pg.time.get_ticks() - self.timer > self.laser_delay:
            self.timer = pg.time.get_ticks()
            self.add_laser = True
        self.check_laser_collision(enemies)

        if self.damage <= 0:
            if self.lives == 0:
                self.dead = True
            else:
                player.lose_live()

    def check_laser_collision(self, enemies):
        for laser in self.lasers[:]:
            laser.update()
            for e in enemies:
                if laser.rect.colliderect(e.rect):
                    offset_x = laser.rect.x - e.rect.x
                    offset_y = laser.rect.y - e.rect.y
                    if e.mask.overlap(laser.mask, (offset_x, offset_y)):
                        e.health -= self.player_laser_damage
                        if e.health <= 0:
                            e.attack = False
                        if self.player_damage <= 5:
                            self.lasers.remove(laser)
                        break

    def draw(self, surf):
        for laser in self.lasers:
            laser.render(surf)
        surf.blit(self.image, self.rect)

    def add_score(self, amt):
        self.score += amt
        TOOLS.update_text(self.score)

class EnemyController:
    def __init__(self,nr,max,lives,speed,enemies):
        self.enemies = enemies
        if nr == 10:
            self.enemy_image = self.enemy_boss0_image_load()
            self.max_enemies = max
            for i in range(self.max_enemies):
                self.enemies.append(self.randomized_enemy(lives))
        elif nr == 11:
            self.enemy_image = self.enemy_boss1_image_load()
            self.max_enemies = max
            for i in range(self.max_enemies):
                self.enemies.append(self.randomized_enemy_1(lives))
        elif nr == 20:
            self.enemy_image = self.enemy_weak1_image_load()
            self.max_enemies = max
            for i in range(self.max_enemies):
                nr = (i+1) * 150
                self.enemies.append(self.weak_enemy(nr,lives,speed))
        elif nr == 21:
            self.enemy_image = self.enemy_weak2_image_load()
            self.max_enemies = max
            for i in range(self.max_enemies):
                nr = (i+1) * 150
                self.enemies.append(self.weak_enemy(nr,lives,speed))
        elif nr == 22:
            self.enemy_image = self.enemy_weak_yellow_image_load()
            self.max_enemies = max
            for i in range(self.max_enemies):
                nr = (i+1) * 150
                self.enemies.append(self.weak_enemy(nr,lives,speed))
        elif nr == 23:
            self.enemy_image = self.enemy_weak_purple_image_load()
            self.max_enemies = max
            for i in range(self.max_enemies):
                nr = (i+1) * 150
                self.enemies.append(self.weak_enemy(nr,lives,speed))
        elif nr == 0:
            self.enemy_image = self.power_up()
            self.enemies.append(self.power_up_spawn(nr))
        elif nr == 1:
            self.enemy_image = self.power_up_bullet_speed()
            self.enemies.append(self.power_up_spawn(nr))
        elif nr == 2:
            self.enemy_image = self.power_up_damage()
            self.enemies.append(self.power_up_spawn(nr))
        elif nr == 3:
            self.enemy_image = self.power_up_live()
            self.enemies.append(self.power_up_spawn(nr))

    def power_up(self):
        image = pg.image.load('health.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (40, 40))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def power_up_live(self):
        image = pg.image.load('heart.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (40, 40))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def power_up_damage(self):
        image = pg.image.load('bullet.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (40, 40))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def power_up_bullet_speed(self):
        image = pg.image.load('power_speed.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (40, 40))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def enemy_boss0_image_load(self):
        image = pg.image.load('enemy_boss3.png')
        image.set_colorkey((255, 0, 255))
        transformed_image = pg.transform.rotate(image, 180)
        orig_image = pg.transform.scale(transformed_image, (140, 180))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def enemy_boss1_image_load(self):
        image = pg.image.load('enemy_boss.png')
        image.set_colorkey((255, 0, 255))
        transformed_image = pg.transform.rotate(image, 180)
        orig_image = pg.transform.scale(transformed_image, (140, 180))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def enemy_weak1_image_load(self):
        image = pg.image.load('enemy_weak1.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (100, 50))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def enemy_weak2_image_load(self):
        image = pg.image.load('enemy_weak2.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (80, 60))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def enemy_weak_purple_image_load(self):
        image = pg.image.load('enemy_weak_purple.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (100, 80))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def enemy_weak_yellow_image_load(self):
        image = pg.image.load('enemy_weak_yellow.png')
        image.set_colorkey((255, 0, 255))
        orig_image = pg.transform.scale(image, (100, 60))
        mask = pg.mask.from_surface(orig_image)
        return (orig_image, mask)

    def randomized_enemy(self,lives):
        y = random.randint(-500, -400)  # above screen
        x = random.randint(100, 400)
        return Enemy(self.enemy_image, screen_rect, (x, y),lives)

    def randomized_enemy_1(self,lives):
        y = random.randint(-500, -400)  # above screen
        x = random.randint(100, 400)
        return Enemy_1(self.enemy_image, screen_rect, (x, y),lives)

    def weak_enemy(self,nr,lives,speed):
        y = 50 # above screen
        x = -nr
        return Soldier(self.enemy_image, screen_rect, (x, y),lives,speed)

    def power_up_spawn(self,nr):
        y = -50  # above screen
        x = randrange(50,650)
        return Power_Up(self.enemy_image, screen_rect, (x, y),nr)

    def update(self, dt, player):
        for e in self.enemies[:]:
            e.update(dt, player)
            if e.dead:
                self.enemies.remove(e)
                player.add_score(25)
            e.draw(screen)


class Tools:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font_init(screen.get_rect())

    def font_init(self, screen_rect):
        self.text_size = 15
        self.text_color = (255, 255, 255)
        self.score_pos = (10, 10)
        self.damage_pos = (10, 30)
        self.lives_pos = (10, 50)
        self.font = pg.font.SysFont('Arial', self.text_size)
        self.update_text()
        self.update_damage()
        self.update_lives()
        self.game_over()

    def update_text(self, score=0):
        self.text, self.text_rect = self.make_text('Score: {}'.format(score),self.score_pos)

    def update_damage(self, damage=10):
        self.damage, self.damage_rect = self.make_text('Health: {}'.format(damage), self.damage_pos)

    def update_lives(self, lives=2):
        self.lives, self.lives_rect = self.make_text('Lives: {}'.format(lives), self.lives_pos)

    def make_text(self, message,pos):
        text = self.font.render(message, True, self.text_color)
        rect = text.get_rect(topleft=pos)
        return text, rect

    def game_over(self):
        game_over_font = pg.font.SysFont('Arial', 45)
        self.game_over_text = game_over_font.render('Game Over', True, (255, 0, 0))
        self.game_over_rect = self.game_over_text.get_rect(center=self.screen_rect.center)

    def draw(self):
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.damage, self.damage_rect)
        self.screen.blit(self.lives, self.lives_rect)


screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
TOOLS = Tools(screen)
player = Player(screen_rect)
# wave
wave = 0
enemy_control1 = EnemyController(20,5,1,2,[])
enemy_control2 = EnemyController(0,0,0,0,[])
enemy_control3 = EnemyController(5,0,0,0,[])
clock = pg.time.Clock()
background = pg.image.load('starfield.png')
done = False
while not done:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        player.get_event(event)
    rand = randrange(1,100)
    # waves
    if not enemy_control1.enemies and wave == 0:
        wave = 1
        enemy_control2 = EnemyController(20,10, 1,2,enemy_control1.enemies)
        if rand < 200:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(2, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 1 and wave == 1:
        wave = 2
        enemy_control1 = EnemyController(21, 10, 1,4,enemy_control2.enemies)
        print(rand)
        if rand < 200:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(2, 1,0,0,enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 4 and wave == 2:
        wave = 3
        enemy_control2 = EnemyController(20, 20, 1,2,enemy_control1.enemies)
        if rand < 200:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(2, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 8 and wave == 3:
        wave = 4
        enemy_control1 = EnemyController(21, 15, 1,4,enemy_control2.enemies)
        if rand < 200:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(2, 1,0,0,enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 5 and wave == 4:
        wave = 5
        enemy_control2 = EnemyController(20, 20, 1,2,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <=14 and wave == 5:
        player.lasers.clear()
        wave = 6
        enemy_control1 = EnemyController(21, 20, 1,4,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0, 4)
            enemy_control3 = EnemyController(nr, 1, 0, 0, enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 10 and wave == 6:
        wave = 7
        enemy_control2 = EnemyController(21, 10, 1,4,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0, 4)
            enemy_control3 = EnemyController(nr, 1, 0, 0, enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 10 and wave == 7:
        player.lasers.clear()
        wave = 8
        enemy_control1 = EnemyController(20, 10, 1,2,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 2 and wave == 8:
        player.lasers.clear()
        wave = 9
        enemy_control2 = EnemyController(20, 10, 1,2,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 6 and wave == 9:
        wave = 10
        enemy_control1 = EnemyController(21, 20, 1,4,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if not enemy_control1.enemies and not enemy_control2.enemies and wave == 10:
        wave = 11
        enemy_control2 = EnemyController(10, 1, 20,2,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if not enemy_control2.enemies and wave == 11:
        player.lasers.clear()
        wave = 12
        enemy_control1 = EnemyController(21, 10, 1,4,enemy_control2.enemies)
        if rand < 60:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if not enemy_control1.enemies and wave == 12:
        wave = 13
        enemy_control2 = EnemyController(22, 10, 3,2,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 2 and wave == 13:
        player.lasers.clear()
        wave = 14
        enemy_control1 = EnemyController(21, 15, 1,4,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 2 and wave == 14:
        wave = 15
        enemy_control2 = EnemyController(22, 15, 3,2,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 8 and wave == 15:
        player.lasers.clear()
        wave = 16
        enemy_control1 = EnemyController(21, 20, 1,4,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 10 and wave == 16:
        wave = 17
        enemy_control2 = EnemyController(21, 30, 1,5,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 15 and wave == 17:
        player.lasers.clear()
        wave = 18
        enemy_control1 = EnemyController(22, 10, 3,2,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control1.enemies) <= 1 and wave == 18:
        player.lasers.clear()
        wave = 19
        enemy_control2 = EnemyController(22, 10, 3,3,enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if len(enemy_control2.enemies) <= 5 and wave == 19:
        player.lasers.clear()
        wave = 20
        enemy_control1 = EnemyController(21, 20, 1,5,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if not enemy_control1.enemies and not enemy_control2.enemies and wave == 20:
        wave = 21
        enemy_control2 = EnemyController(11, 1, 30, 0, enemy_control1.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    if not enemy_control2.enemies and wave == 21:
        player.lasers.clear()
        wave = 20
        enemy_control1 = EnemyController(23, 20, 2,4,enemy_control2.enemies)
        if rand < 20:
            nr = randrange(0,4)
            enemy_control3 = EnemyController(nr, 1,0,0,enemy_control3.enemies)
    screen.blit(background, background_rect)
    delta_time = clock.tick(60)/1000.0
    if not player.dead:
        if wave%2 == 0:
            player.update(keys, delta_time, enemy_control1.enemies)
            enemy_control1.update(delta_time, player)
        else:
            player.update(keys, delta_time, enemy_control2.enemies)
            enemy_control2.update(delta_time, player)
        enemy_control3.update(delta_time, player)
    else:
        screen.blit(TOOLS.game_over_text, TOOLS.game_over_rect)
    player.draw(screen)
    TOOLS.draw()
    pg.display.update()
