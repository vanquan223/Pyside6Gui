from gui.core.functions import Functions
from gui.core.json_themes import Themes
from gui.widgets import *
from qt_core import *

class LoadReport():
    def __init__(self, ui):
        self.ui = ui
        themes = Themes()
        self.themes = themes.items
        self.setup_ui()

    def setup_ui(self):
        
        pass