from ui import *
import sys
import csv

## Create class for deh UI?!?

class Last(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
## Connecting deh buttons here
        self.push_URL.clicked.connect(self.grabURL)

## Define deh methoids here

    def grabURL(self):
        def append_list_as_row(file_name, list_of_elem):
            # Open file in append mode
            with open(file_name, 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = csv.writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow([list_of_elem])


        URLTemp = self.line_URL.text()
        append_list_as_row("URLs.csv", URLTemp)
        print (URLTemp)

## Ui stuff idk XD

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

## Create deh window instance
ui = Last(MainWindow)

## Show deh window
MainWindow.show()
app.exec_()
