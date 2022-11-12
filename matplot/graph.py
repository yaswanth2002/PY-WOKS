import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
import matplotlib.pyplot as plt
import sys
import serial.tools.list_ports as p

ports = p.comports()
port=[]
for i in ports:
     port.append(i.device)
  
class Window(QDialog):
  

    def __init__(self):
        super(Window, self).__init__()
  
       
        self.setWindowTitle("Python")
  
        # setting geometry to the window
        self.setGeometry(100, 100, 300, 100)
  
        # creating a group box
        self.formGroupBox = QGroupBox("LOGIN ")
  
        # creating combo box to select degree
        self.degreeComboBox = QComboBox()
  
        # adding items to the combo box
        self.degreeComboBox.addItems(port)
  
        # creating a line edit
        self.nameLineEdit = QLineEdit()
        self.passLineEdit = QLineEdit() 
    
  
        # calling the method that create the form
        self.createForm()
  
        # creating a dialog button for ok and cancel
        self.pushbutton = QPushButton('Login')

        self.pushbutton.clicked.connect(self.launch_graph) # calling getInfo function whenever button is pressed
        
  
        # creating a vertical layout
        mainLayout = QVBoxLayout()
  
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
  
        # adding button box to the layout
        mainLayout.addWidget(self.pushbutton)
  
        # setting lay out
        self.setLayout(mainLayout)
  
    # get info method called when form is accepted
    def getInfo(self):
  
        # printing the form information
        print("USERNAME : {0}".format(self.nameLineEdit.text()))
        print("PASSWORD: {0}".format(self.passLineEdit.text()))
        print("COMPORT : {0}".format(self.degreeComboBox.currentText()))
        
  
        # closing the window
        self.close()
  
    # creat form method
    def createForm(self):
  
        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("USERNAME"), self.nameLineEdit)
        
        layout.addRow(QLabel("PASSWORD"), self.passLineEdit)
  
        # for degree and adding combo box
        layout.addRow(QLabel("COMPORT"), self.degreeComboBox)
        
        # setting layout
        self.formGroupBox.setLayout(layout)
        
    def launch_graph(self):
        x = [23,45,56,78] 
        y = [12,34,45,45]
       
        plt.plot(x,y)
        
        
        plt.show()
    def launch_graph(self):
        y = [23,45,56,78] 
        z = [12,35,45,45]
       
        plt.plot(y,z)
        
        
        plt.show()
  
# main method
if __name__ == '__main__':
  
    # create pyqt5 app
    app = QApplication(sys.argv)
  
    # create the instance of our Window
    window = Window()
  
    # showing the window
    window.show()
  
    # start the app
    sys.exit(app.exec())