# ref
# https://liuxinwin_admin.gitee.io/pythonocc-docs/OCC.Display.OCCViewer.html
#

from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Core.Graphic3d import *

from Presentation.MainWindow.core import MainWindow

class DisplayFunctions(MainWindow):
    ## IMPORTS
    def navigate_to_imports(self):
        # variables

        # set page
        self.ui.stackedWidget.setCurrentIndex(0)
        
        # set display
        try:
            self.display.EraseAll()

            # cylinder shown
            if self.brachyCylinder:
                shape = self.brachyCylinder.shape
                color = Quantity_Color(0.25, 0.25, 0.25, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=shape, color=color)

        except Exception as error_message:
            print(error_message)

        try: 
            # needles shown
            if self.needles:
                color = Quantity_Color(0.35, 0.2, 0.35, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=self.display_needles, color=color)

        except Exception as error_message:
            print(error_message)

        try: 
            # tandem
            if self.display_tandem:
                color = Quantity_Color(0.2, 0.55, 0.55, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=self.display_tandem, color=color)

        except Exception as error_message:
            print(error_message)

        try:
            self.display.FitAll()
        except Exception as error_message:
            print(error_message)

    ## CYLINDER
    def navigate_to_cylinder(self):
        # variables

        # set page
        self.ui.stackedWidget.setCurrentIndex(1)
        
        # set display
        try:
            self.display.EraseAll()

            # cylinder shown
            if self.brachyCylinder:
                shape = self.brachyCylinder.shape
                color = Quantity_Color(0.35, 0.2, 0.35, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=shape, color=color)

        except Exception as error_message:
            print(error_message)

        try: 
            # needles shown
            if self.needles:
                color = Quantity_Color(0.35, 0.2, 0.35, Quantity_TOC_RGB)
                self.display.DisplayShape(shapes=self.display_needles, material=Graphic3d_NOM_TRANSPARENT)

        except Exception as error_message:
            print(error_message)

        try: 
            # tandem
            if self.display_tandem:
                color = Quantity_Color(0.2, 0.55, 0.55, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=self.display_tandem, color=color)

        except Exception as error_message:
            print(error_message)

        try:
            self.display.FitAll()
        except Exception as error_message:
            print(error_message)

    ## NEEDLE CHANNELS
    def navigate_to_channels(self):
        # variables

        # set page
        self.ui.stackedWidget.setCurrentIndex(2)
        
        # set display
        try:
            self.display.EraseAll()

            # cylinder shown
            if self.brachyCylinder:
                shape = self.brachyCylinder.shape
                self.display.DisplayShape(shapes=shape, material=Graphic3d_NOM_TRANSPARENT)

        except Exception as error_message:
            print(error_message)

        try: 
            # needles shown
            if self.needles:
                color = Quantity_Color(0.35, 0.2, 0.35, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=self.display_needles, color=color)

        except Exception as error_message:
            print(error_message)

        try: 
            # tandem
            if self.display_tandem:
                color = Quantity_Color(0.2, 0.55, 0.55, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=self.display_tandem, color=color)

        except Exception as error_message:
            print(error_message)

        try:
            self.display.FitAll()
        except Exception as error_message:
            print(error_message)

    ## TANDEM
    def navigate_to_tandem(self):
        # variables

        # set page
        self.ui.stackedWidget.setCurrentIndex(3)
        
        # set display
        try:
            self.display.EraseAll()

            # cylinder shown
            if self.brachyCylinder:
                shape = self.brachyCylinder.shape
                self.display.DisplayShape(shapes=shape, material=Graphic3d_NOM_TRANSPARENT)

        except Exception as error_message:
            print(error_message)

        try: 
            # needles shown
            if self.needles:
                self.display.DisplayShape(shapes=self.display_needles, material=Graphic3d_NOM_TRANSPARENT)

        except Exception as error_message:
            print(error_message)

        try: 
            # tandem
            if self.display_tandem:
                color = Quantity_Color(0.2, 0.2, 0.55, Quantity_TOC_RGB)
                self.display.DisplayColoredShape(shapes=self.display_tandem, color=color)

        except Exception as error_message:
            print(error_message)

        try:
            self.display.FitAll()
        except Exception as error_message:
            print(error_message)

    ## EXPORT
    def navigate_to_exports(self):
        # variables

        # set page
        self.ui.stackedWidget.setCurrentIndex(4)
        
        shape = None
        
        # set display
        try:
            self.display.EraseAll()

            # cylinder shown
            if self.brachyCylinder:
                shape = self.brachyCylinder.shape

        except Exception as error_message:
            print(error_message)

        try: 
            # needles shown
            if self.needles:
                shape = BRepAlgoAPI_Cut(shape, self.display_needles).Shape()

        except Exception as error_message:
            print(error_message)

        try: 
            # tandem
            if self.display_tandem:
                shape = BRepAlgoAPI_Cut(shape, self.display_tandem)

        except Exception as error_message:
            print(error_message)

        try:
            color = Quantity_Color(0.1, 0.8, 0.1, Quantity_TOC_RGB)
            self.display.DisplayColoredShape(shapes=shape, color=color)
            self.display.FitAll()
        except Exception as error_message:
            print(error_message)