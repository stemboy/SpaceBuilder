from kivy import Logger
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from Classes.baseBuilderScreen import BaseBuilderScreen
from Classes.crashScreen import CrashScreen
from Classes.introScreen import IntroScreen
from Classes.screen import Screen

from Classes.baseBuilder import BaseBuilder
from Classes.betterFloatLayout import BetterFloatLayout



class ScreenManager(ScreenManager):
    def __init__(self, Globals):
        super(ScreenManager, self).__init__()

        self.width = Globals.width
        self.height = Globals.height

        dumpScreen = Screen(name="Screen")
        introScreen = IntroScreen(Globals, name="IntroScreen")
        crashScreen = CrashScreen(Globals, name="CrashScreen")
        baseBuildScreen = BaseBuilderScreen(Globals, name="BaseBuilderScreen")

        self.add_widget(dumpScreen)
        self.add_widget(introScreen)
        self.add_widget(crashScreen)
        self.add_widget(baseBuildScreen)

        if Globals.User_data.get("introFinished"):
            self.current = "BaseBuilderScreen"
            Logger.info("Application: Starting in BaseBuilder")

        else:
            Logger.info("Application: Starting in Intro")
            self.current = "IntroScreen"

        Logger.info("Application: Screen Manager setup")

    def openCrashScreen(self, _=None):
        self.transition = FadeTransition()
        self.current = "CrashScreen"

    def openBaseBuilderScreen(self, _=None):
        self.transition = FadeTransition()
        self.current = "BaseBuilderScreen"
