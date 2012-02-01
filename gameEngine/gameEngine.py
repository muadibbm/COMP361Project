'''
Created on Jan 23, 2012

@author: Bazibaz
'''
import random
import math

from direct.showbase import DirectObject 

import sys
sys.path.append("..")

from gameModel.solar import Star, Planet
from graphicEngine.environement import Environement
from graphicEngine.solar import StarDraw, PlanetDraw
from graphicEngine.camera import Camera
from gameModel.constants import MAX_DEAD_STAR_RADIUS, NUMBER_OF_STARS, \
    MAX_DEAD_PLANET_RADIUS, MIN_PLANET_VELOCITY, MAX_NUMBER_OF_PLANETS, DEEP_SPACE_DISTANCE, \
    UNIVERSE_SCALE, DISTANCE_BETWEEN_PLANETS
from panda3d.core import Point3

from mouseEvents import MouseEvents

class GameEngine(DirectObject.DirectObject):
    '''
    This class acts as the connection between the game model and the graphic engine.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.mouse_events = MouseEvents()
        
        self.all_stars = []
        self.all_planets = []
        self.prepareGame(NUMBER_OF_STARS, MAX_NUMBER_OF_PLANETS, self.all_stars, self.all_planets)
        
        #randomly set the camera on one of the stars
        rand = random.randrange(0,NUMBER_OF_STARS,1)
        '''@TODO : camera is not set on the correct position, why ? '''
        self.game_camera = Camera(self.all_stars[rand])
        
        self.startSinglePlayerGame()
        
    
    def prepareGame(self, number_of_stars, number_of_planets, stars, planets):
        '''
        Sets up the environment of the game
        @param number_of_stars : int, the desired number of stars 
        @precondition: number_of_stars > 0
        @param number_of_stars : int, the desired number of planets orbiting each star
        @precondition number_of_planets > 0
        @param stars : Star, list of the stars
        '''
        #Initialize graphics
        self.env_graphics = Environement()
        
        while(len(stars)<number_of_stars):
            rand = random.random()*10
            if (rand<2.5):
                x_random = -random.random()*UNIVERSE_SCALE/(1.8)
                y_random = -random.random()*UNIVERSE_SCALE/(1.8)
            elif (rand>=2.5 and rand<5):
                x_random = random.random()*UNIVERSE_SCALE/(1.8)
                y_random = -random.random()*UNIVERSE_SCALE/(1.8)
            elif (rand>=5 and rand<7.5):
                x_random = -random.random()*UNIVERSE_SCALE/(1.8)
                y_random = random.random()*UNIVERSE_SCALE/(1.8)
            else:
                x_random = random.random()*UNIVERSE_SCALE/(1.8)
                y_random = random.random()*UNIVERSE_SCALE/(1.8)
                
            add = True
            
            for star in stars:
                if(DEEP_SPACE_DISTANCE>abs(x_random-star[0].position.x) or \
                   DEEP_SPACE_DISTANCE>abs(y_random-star[0].position.y)):
                    add = False
            
            if(add):
                star = Star(position=Point3(0,0,0), radius = MAX_DEAD_STAR_RADIUS)
                dstar = StarDraw(star)
                #Add observer to star model
                star.attachObserver(dstar);
                stars.append((star,dstar))
                i=1
                #print ("star x : %lf", x_random)
                #print ("star y : %lf", y_random)
                while(i<=number_of_planets):
                    alpha = random.random()*math.pi*2
                    pxcord =  i * math.cos(alpha) * DISTANCE_BETWEEN_PLANETS
                    pycord = i * math.sin(alpha) * DISTANCE_BETWEEN_PLANETS
                    planet = Planet(position=Point3(pxcord + 0,\
                                                    pycord + 0, 0), \
                                    radius=MAX_DEAD_PLANET_RADIUS)
                    #print ("planet x : ", pxcord)
                    #print ("planet y : ", pycord)
                    print("2-norm: ", math.sqrt(math.pow(pxcord - x_random, 2) + math.pow(pycord - y_random, 2)) / DISTANCE_BETWEEN_PLANETS)
                    
                    planet.parent_star = star
                    planet.orbital_velocity = 0
                    planet.spin_velocity = 70
                    dplanet = PlanetDraw(planet, dstar.point_path)
                    dplanet.startSpin()
                    dplanet.startOrbit()
                    planet.attachObserver(dplanet);
                    star.addPlanet(planet)
                    planets.append((planet,dplanet))
                    i+=1
            
        
            
    def startSinglePlayerGame(self):
        '''
        Start a prepared game
        '''
        music = base.loader.loadSfx("sound/music/music1.mp3")
        music.play()

