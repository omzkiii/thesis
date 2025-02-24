import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebEngineViewer(QWidget):
    """Handles displaying the generated route in a browser."""
    def __init__(self, place, amenities, generate_func):
        super().__init__()
        file_name = f"{place} - {amenities[0]}.html"
        
        self.browser = QWebEngineView()
        file_path = os.path.abspath(file_name)

        if os.path.exists(file_path):
            self.browser.setUrl(QUrl(f"file:///{file_path}"))
        else:
            generate_func(place, amenities)
            self.browser.setUrl(QUrl(f"file:///{file_path}"))
            print(f"File not found: {file_path}")

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Route Viewer")
        self.show()

class RouteSelectionApp(QWidget):
    """Main selection window to choose a place and amenity for route generation."""
    def __init__(self, generate_func):
        super().__init__()
        self.generate_func = generate_func
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.place_dropdown = QComboBox()
        self.place_dropdown.addItems(["Sampaloc, Manila", "Quiapo, Manila", "Tondo, Manila"])

        self.amenity_dropdown = QComboBox()
        self.amenity_dropdown.addItems(["Schools", "Offices", "Hospitals"])

        self.button = QPushButton("Generate Route")
        self.button.clicked.connect(self.openRouteHtml)

        layout.addWidget(self.place_dropdown)
        layout.addWidget(self.amenity_dropdown)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle("ODTC Route Generator")
        self.setGeometry(200, 200, 300, 150)

    def openRouteHtml(self):
        amenities_dict = {"Schools": ["school", "college", "institute", "university"]}
        place = self.place_dropdown.currentText()
        amenity = amenities_dict.get(self.amenity_dropdown.currentText())
        self.web_viewer = WebEngineViewer(place, amenity, self.generate_func)

def launch_route_generator():
    """Launches the PyQt5 GUI for route selection."""
    app = QApplication(sys.argv)
    route_window = RouteSelectionApp(generate_func=lambda p, a: print(f"Generating for {p} - {a}"))
    route_window.show()
    app.exec_()
