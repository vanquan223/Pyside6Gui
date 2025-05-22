# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
from helpers import resource_path

# APP FUNCTIONS
# ///////////////////////////////////////////////////////////////
class Functions:

    # SET SVG ICON
    # ///////////////////////////////////////////////////////////////
    def set_svg_icon(icon_name):
        folder = "gui/images/svg_icons/"
        return resource_path(folder + icon_name)

    # SET SVG IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_svg_image(icon_name):
        folder = "gui/images/svg_images/"
        return resource_path(folder + icon_name)

    # SET IMAGE
    # ///////////////////////////////////////////////////////////////
    def set_image(image_name):
        folder = "gui/images/images/"
        return resource_path(folder + image_name)