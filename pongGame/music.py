import pygame
from pygame.locals import *
from pygame import mixer

class Music:
    def __init__(self) -> None:
        #pass
        mixer.init()
    
    def gameGoing(self):
        mixer.music.load(filename='GroundTheme.mp3')
        mixer.music.play(-1)
    
    def gotFood(self):
        mixer.music.stop
        mixer.music.load(filename='smb_1-up.wav')
        mixer.music.play()
        mixer.music.stop
        
        
    def gameOver(self):
        mixer.music.stop
        mixer.music.load(filename='smb_mariodie.wav')
        mixer.music.play()
        #