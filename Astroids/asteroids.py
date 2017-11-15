import sys
import random
import pygame
import math
import time
from pygame.locals import *
from ship import Ship
from boss import Boss
from astroid import Astroid
from star import Star
from bullet import Bullet
from game import Game
from point import Point


class Asteroids( Game ):
    """
    Asteroids extends the base class Game to provide logic for the specifics of the game
    """


    score = 0
    health = 3

    def __init__(self, name, width, height):
        super().__init__( name, width, height )
        pygame.init()  # to enable timer
        self.ship = Ship() #  TODO: should create a Ship object here
        # TODO: should create asteroids
        astroids = [Astroid(x=150,y=300,movement=Point(0.2,0.2),ang_vel=1),Astroid(x=50,y=100,movement=Point(0.2,-0.2),ang_vel=1),Astroid(x=400,y=400,movement=Point(-0.2,0.2),ang_vel=-1)]
        self.asteroids= astroids
        # TODO: should create stars
        stars = []
        for i in range(10):
            for j in range (8):
                stars.append(Star(x=i*64,y=j*64))
        self.stars=stars
        bullets=[]
        self.bullets = bullets
        self.currentBoss = 0

        self.font = pygame.font.SysFont("Courier new", 20)

    shootingTimer = 0
    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] and self.ship:
            self.ship.rotate(-1)
        if keys_pressed[K_RIGHT] and self.ship:
            self.ship.rotate(1)
        if keys_pressed[K_UP] and self.ship:
            self.ship.accelerate(0.01)
        if keys_pressed[K_DOWN] and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:

                self.shootingTimer+=1

                if self.shootingTimer>20:
                    bullet = Bullet()
                    bullet.timer = pygame.time.get_ticks()
                    bullet.position=self.ship.position
                    bullet.pull.x = (2 * math.cos(math.radians(self.ship.rotation)))
                    bullet.pull.y = (2 * math.sin(math.radians(self.ship.rotation)))
                    self.bullets.append(bullet)
                    self.shootingTimer = 0
            # TODO: should create a bullet when the user fires

    bulletAsteroidTimer = 0
    def update_simulation(self):
        """
        update_simulation() causes all objects in the game to update themselves
        """



        super().update_simulation()


        if(len(self.asteroids) == 0):
            self.currentBoss = Boss()

        if self.ship:
            self.ship.update( self.width, self.height )

            if(self.currentBoss!=0):

                self.currentBoss.r = 255
                self.currentBoss.g = 0
                self.currentBoss.b = 0

                self.currentBoss.update(self.width, self.height)



                if self.currentBoss.position.y <50:
                    self.currentBoss.accelerate(0.01)
                else:
                    self.currentBoss.accelerate(0)

                if(self.ship.position.x>self.currentBoss.position.x):
                    self.currentBoss.position.x+=0.5
                else:
                    self.currentBoss.position.x -= 0.5

                if(self.bulletAsteroidTimer>200 and len(self.asteroids)<3):
                    bulletAsteroid = Astroid(x=self.currentBoss.position.x, y=self.currentBoss.position.y,  movement=Point(0, 1))
                    self.asteroids.append(bulletAsteroid)
                    self.bulletAsteroidTimer = 0
                else:
                    self.bulletAsteroidTimer+=1

                if self.currentBoss.health <= 0:
                    self.currentBoss = 0
                    self.asteroids.clear()
                    self.asteroids.append(Astroid(x=150, y=300, movement=Point(0.2, 0.3), ang_vel=1))
                    self.asteroids.append(Astroid(x=400, y=300, movement=Point(0.2, 0.2), ang_vel=1))
                    self.asteroids.append(Astroid(x=0, y=0, movement=Point(0.2, 0.2), ang_vel=1))

        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
        for star in self.stars:
            star.update( self.width, self.height )
        for bullet in self.bullets: #ny
            if ((pygame.time.get_ticks() - bullet.timer)/1000) < 1:
                bullet.update(self.width, self.height)
            else:
                self.bullets.remove(bullet)        # TODO: should probably call update on our bullet/bullets here
        # TODO: should probably work out how to remove a bullet when it gets old
        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()
        # Render the ship.py:
        if self.ship:
            self.ship.draw( self.screen )

        if(self.currentBoss):
            self.currentBoss.draw(self.screen)

        # Render all the stars, if any:
        for star in self.stars:
            star.draw( self.screen )
        # Render all the asteroids, if any:
        for asteroid in self.asteroids:
            asteroid.draw( self.screen )
        # Render all the bullet, if any:
        for bullet in self.bullets:
            bullet.draw( self.screen )

        Game.screen.blit(self.font.render('Score: {0}'.format(self.score), True, (255, 255, 255)), (10, 10))

        generatedHealthString = ""

        for i in range(self.health):
            generatedHealthString+="♥ "

        Game.screen.blit(self.font.render('Health left: '+generatedHealthString, True, (255, 255, 255)), (10, 35))

    def handle_collisions(self):
        """
        handle_collisions() should check:
            - if our ship.py has crashed into an asteroid (the ship.py gets destroyed - game over!)
            - if a bullet has hit an asteroid (the asteroid gets destroyed)
        :return: 
        """
        # TODO: implement collission detection,
        #       using the collission detection methods in all of the shapes
        if self.currentBoss!=0:
            for bullet in self.bullets:
                if bullet.collideWithPoly(self.currentBoss):
                    self.currentBoss.health   -=2
                    self.bullets.remove(bullet)
                    self.score+=10


        for asteroid in self.asteroids:
            if asteroid.collide(self.ship):
                print("krock")

                if(self.health>0):
                    self.health -= 1
                    self.asteroids.remove(asteroid)
                else:
                    self.running = False

            for bullet in self.bullets:
                if bullet.collideWithPoly(asteroid):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    self.score+=1






