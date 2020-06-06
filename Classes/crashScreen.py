from kivy import Logger
from kivy.animation import Animation
from kivy.core.image import Image as CoreImage
from kivy.clock import Clock
from kivy.graphics import *

from Classes.screen import Screen


class CrashScreen(Screen):
    def __init__(self, Globals, *args, **kwargs):
        super(CrashScreen, self).__init__(*args, **kwargs)

        self.Globals = Globals

        self.canyonClock = None
        self.starClock = None
        self.drawClock = None


        ratio = CoreImage("textures/canyon surface.png").width / CoreImage("textures/canyon surface.png").height
        self.h = self.Globals.height
        self.w = ratio * Globals.width

        self.starLayout = self.ids["stars"]
        self.canyonLayout = self.ids["canyon"]

        self.starLayout.pos = (Globals.width, 0)
        self.canyonLayout.pos = (Globals.width, 0)

        Logger.info("Application: Crash Screen setup")


    def post_init(self):
        Logger.info("Application: Crash Screen entered")

        self.canyonClock = Clock.schedule_once(self.move_canyon, self.Globals.GameSettings.crash_move_delay)
        self.starClock = Clock.schedule_once(self.move_stars, self.Globals.GameSettings.crash_move_delay)
        self.drawClock = Clock.schedule_interval(self.draw, 0)


    def move_canyon(self, _):
        Logger.info("Application: Crash Screen canyon move started")

        animation = Animation(pos=self.starLayout.pos, duration=0)
        animation += Animation(pos=(self.starLayout.width - self.starLayout.pos[0], self.starLayout.pos[1]),
                               duration=self.Globals.GameSettings.crash_move_length)

        print(self.starLayout.pos, (self.starLayout.width - self.starLayout.pos[0], self.starLayout.pos[1]), animation.duration)

        animation.start(self.canyonLayout)


    def move_stars(self, _):
        Logger.info("Application: Crash Screen stars move started")


    def draw(self, _):
        with self.starLayout.canvas:
            Rectangle(pos=self.starLayout.pos, size=(self.w, self.h), source="textures/canyon surface stars.png")

        with self.canyonLayout.canvas:
            Rectangle(pos=self.canyonLayout.pos, size=(self.w, self.h), source="textures/canyon surface.png")
