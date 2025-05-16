from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Physical Simulation")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Menu Bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Exit Action
        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Additional UI components can be added here

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())