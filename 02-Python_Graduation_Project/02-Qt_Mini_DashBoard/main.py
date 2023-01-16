import os
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication,QSlider,QLabel
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5 import QtCore
################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
os.system("pyuic5 -o Dash_Board_Code.py -x Dash_Board_GUI.ui")
# os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui.oQCkCR")

from Dash_Board_Code import *

################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: gray") #changing the color of the window
        #self.setStyleSheet("QSlider::handle:horizontal{background-color:red}""background-color:royalblue")
#-----------------------------------------------------------------------
## Customizing the Analogue widgets
#-----------------------------------------------------------------------
        self.ui.widget.enableBarGraph = True
        self.ui.widget.units = "KpH"
        self.ui.widget.minValue = 0
        self.ui.widget.maxValue = 220
        self.ui.widget.scalaCount= 21
        self.ui.widget.setGaugeTheme(0)
        self.ui.widget.setNeedleCenterColor(color1 = "red")
        self.ui.widget.setMouseTracking(False)
        #self.ui.widget.setOuterCircleColor(color1= "white")
        self.ui.widget_2.enableBarGraph = True
        self.ui.widget_2.units = "RPM"
        self.ui.widget_2.minValue = 0		
        self.ui.widget_2.maxValue = 7
        self.ui.widget_2.scalaCount= 7
        self.ui.widget_2.setNeedleCenterColor(color1= "red")
        self.ui.widget_2.setMouseTracking(False)
#-----------------------------------------------------------------------
## Customizing the speed slider widget and it's label
#-----------------------------------------------------------------------
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.horizontalSlider.valueChanged.connect(self.Sliding_Speed)
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(220)
        self.ui.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.ui.horizontalSlider.setTickInterval(10)
        # self.ui.horizontalSlider.setSingleStep(5)
#------------------------------------------------------------------------
## Customizing the RPM slider widget and it's label 
#------------------------------------------------------------------------
        #self.ui.label_2.setAlignment(QtCore.Qt.AlignCenter)
        #self.ui.horizontalSlider_2.valueChanged.connect(self.Sliding_RPM)
        #self.ui.horizontalSlider_2.setMinimum(0)
        #self.ui.horizontalSlider_2.setMaximum(7)
        #self.ui.horizontalSlider_2.setTickPosition(QSlider.TicksBelow)
        #self.ui.horizontalSlider_2.setTickInterval(1)
#------------------------------------------------------------------------
## Functions Used
#------------------------------------------------------------------------
    def Sliding_Speed(self,value):
        self.ui.label_2.setText(str(int(value*7/220)))
        self.ui.widget_2.updateValue(int(value*7/220))
        self.ui.label.setText(str(value))
        self.ui.widget.updateValue(value)
		#self.ui.label_2.setText(str((value))
################################################################################################
# Show window
################################################################################################
        self.show()
########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  