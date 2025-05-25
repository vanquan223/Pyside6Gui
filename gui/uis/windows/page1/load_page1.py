from gui.core.functions import Functions
from gui.core.json_themes import Themes
from gui.widgets import *
from qt_core import *


class LoadPage1:
    def __init__(self, ui):
        self.ui = ui
        themes = Themes()
        self.themes = themes.items
        self.setup_ui()

    def setup_ui(self):
        # SETUP PAGE 1

        # CIRCULAR PROGRESS 1
        self.circular_progress_1 = PyCircularProgress(
            value = 80,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["text_title"],
            font_size = 14,
            bg_color = self.themes["app_color"]["dark_four"]
        )
        self.circular_progress_1.setFixedSize(200,200)

        # CIRCULAR PROGRESS 2
        self.circular_progress_2 = PyCircularProgress(
            value = 45,
            progress_width = 4,
            progress_color = self.themes["app_color"]["context_color"],
            text_color = self.themes["app_color"]["context_color"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_2.setFixedSize(160,160)

        # CIRCULAR PROGRESS 3
        self.circular_progress_3 = PyCircularProgress(
            value = 75,
            progress_width = 2,
            progress_color = self.themes["app_color"]["pink"],
            text_color = self.themes["app_color"]["white"],
            font_size = 14,
            bg_color = self.themes["app_color"]["bg_three"]
        )
        self.circular_progress_3.setFixedSize(140,140)

        # PY SLIDER 1
        self.vertical_slider_1 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_1.setMinimumHeight(100)

        # PY SLIDER 2
        self.vertical_slider_2 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_2.setMinimumHeight(100)

        # PY SLIDER 3
        self.vertical_slider_3 = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_four"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_3.setOrientation(Qt.Horizontal)
        self.vertical_slider_3.setMaximumWidth(200)

        # PY SLIDER 4
        self.vertical_slider_4 = PySlider(
            bg_color = self.themes["app_color"]["dark_three"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            handle_color = self.themes["app_color"]["context_color"],
            handle_color_hover = self.themes["app_color"]["context_hover"],
            handle_color_pressed = self.themes["app_color"]["context_pressed"]
        )
        self.vertical_slider_4.setOrientation(Qt.Horizontal)
        self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_heart.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Icon button - Heart",
            width = 40,
            height = 40,
            radius = 20,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN with tooltip",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["green"],
        )

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_add_user.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "BTN actived! (is_actived = True)",
            width = 40,
            height = 40,
            radius = 8,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["white"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["context_color"],
            is_active = True
        )

        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text = "Button Without Icon",
            radius  =8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)

        # PUSH BUTTON 2
        self.push_button_2 = PyPushButton(
            text = "Button With Icon",
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.push_button_2.setMinimumHeight(40)
        self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text = "",
            place_holder_text = "Place holder text",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.table_widget.setColumnCount(3)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("NAME")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("NICK")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("PASS")

        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)

        for x in range(10):
            row_number = self.table_widget.rowCount()
            self.table_widget.insertRow(row_number) # Insert row
            self.table_widget.setItem(row_number, 0, QTableWidgetItem(str("Wanderson"))) # Add name
            self.table_widget.setItem(row_number, 1, QTableWidgetItem(str("vfx_on_fire_" + str(x)))) # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText("12345" + str(x))
            self.table_widget.setItem(row_number, 2, self.pass_text) # Add pass
            self.table_widget.setRowHeight(row_number, 22)
        
        # ADD WIDGETS
        self.ui.load_pages.page1_ui.row_1_layout.addWidget(self.circular_progress_1)
        self.ui.load_pages.page1_ui.row_1_layout.addWidget(self.circular_progress_2)
        self.ui.load_pages.page1_ui.row_1_layout.addWidget(self.circular_progress_3)
        self.ui.load_pages.page1_ui.row_2_layout.addWidget(self.vertical_slider_1)
        self.ui.load_pages.page1_ui.row_2_layout.addWidget(self.vertical_slider_2)
        self.ui.load_pages.page1_ui.row_2_layout.addWidget(self.vertical_slider_3)
        self.ui.load_pages.page1_ui.row_2_layout.addWidget(self.vertical_slider_4)
        self.ui.load_pages.page1_ui.row_3_layout.addWidget(self.icon_button_1)
        self.ui.load_pages.page1_ui.row_3_layout.addWidget(self.icon_button_2)
        self.ui.load_pages.page1_ui.row_3_layout.addWidget(self.icon_button_3)
        self.ui.load_pages.page1_ui.row_3_layout.addWidget(self.push_button_1)
        self.ui.load_pages.page1_ui.row_3_layout.addWidget(self.push_button_2)
        self.ui.load_pages.page1_ui.row_3_layout.addWidget(self.toggle_button)
        self.ui.load_pages.page1_ui.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.page1_ui.row_5_layout.addWidget(self.table_widget)

    def clear_widgets(self):
        # Clear all widgets in page 1
        for i in reversed(range(self.ui.load_pages.page1_ui.row_1_layout.count())):
            widget = self.ui.load_pages.page1_ui.row_1_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        for i in reversed(range(self.ui.load_pages.page1_ui.row_2_layout.count())):
            widget = self.ui.load_pages.page1_ui.row_2_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        for i in reversed(range(self.ui.load_pages.page1_ui.row_3_layout.count())):
            widget = self.ui.load_pages.page1_ui.row_3_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        for i in reversed(range(self.ui.load_pages.page1_ui.row_4_layout.count())):
            widget = self.ui.load_pages.page1_ui.row_4_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        for i in reversed(range(self.ui.load_pages.page1_ui.row_5_layout.count())):
            widget = self.ui.load_pages.page1_ui.row_5_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()