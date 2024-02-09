import pygame as pg

class Projectile:
    
    def __init__(self, x, y, vel=1, damage=1):
        self.x = x
        self.y = y
        self.vel = vel
        self.dmg = damage
        
    
    def draw(self, screen):
        for projectile in Projectile:
            rect = (projectile.x, projectile.y, projectile_w, projectile_h)
            pg.draw.rect(screen, (255, 0, 0), rect) 
            
    def move(self):
        self.x += 0
        self.y -= 1