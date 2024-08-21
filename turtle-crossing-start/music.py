import pygame
from pygame.locals import *
from pygame import mixer

class Music:
    def __init__(self) -> None:
        #pass
        mixer.init()
    
    def gameGoing(self):
        mixer.music.load(filename='GameStart.mp3')
        mixer.music.play(-1)
    
    def reachGoal(self):
        mixer.music.stop
        mixer.music.load(filename='Goal.mp3')
        mixer.music.play()
        mixer.music.stop
        
        
    def gameOver(self):
        mixer.music.stop
        mixer.music.load(filename='GameOver.mp3')
        mixer.music.play()
        #