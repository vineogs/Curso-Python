import time
from pygame import mixer

mixer.init()
mixer.music.load('D:/cbat.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)