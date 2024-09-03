import pygame
from pygame.locals import *
from pygame import mixer

class Music:
    def __init__(self) -> None:
        #pass
        mixer.init()
    
 
    
    def brakeTime(self):
        mixer.music.stop
        mixer.music.load(filename='smb_1-up.wav')
        mixer.music.play()
        mixer.music.stop
        
        
    def finish(self):
        mixer.music.stop
        mixer.music.load(filename='smb_mariodie.wav')
        mixer.music.play()
        mixer.music.stop
        #