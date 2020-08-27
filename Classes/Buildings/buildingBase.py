from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, DictProperty
from kivy.graphics import *

from Classes.globals import get_Globals


class BuildingBase(Widget):
    rotation = NumericProperty(0)
    frame = NumericProperty(0)
    name = StringProperty("BuildingBase")
    data = DictProperty({})

    def __init__(self, *args, **kwargs):
        super(BuildingBase, self).__init__(*args, **kwargs)
        self.Globals = get_Globals()

    def draw(self):
        with self.canvas:
            Rectangle(pos=self.pos, size=(100, 100), texture=self.Globals.BuildingTextures.get_texture(self.name, self.data, self.frame))