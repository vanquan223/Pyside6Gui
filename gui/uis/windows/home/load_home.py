from gui.core.functions import Functions
from gui.core.json_themes import Themes
from gui.widgets import *
from qt_core import *

class LoadHome():
    def __init__(self, ui):
        self.ui = ui
        themes = Themes()
        self.themes = themes.items
        self.setup_ui()

    def setup_ui(self):
        
        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value = 80,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200,200)
        
        self.ui.load_pages.home_ui.statisticsLayout.addWidget(self.circular_progress_1)