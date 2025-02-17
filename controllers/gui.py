import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class WebEngineViewer(QWidget):
    def __init__(self, place, amenities, generate_func):
        file_name = f"{place} - {amenities[0]}.html"
        super().__init__()

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
        self.setWindowTitle("Route")
        self.show()


class MainApp(QWidget):
    def __init__(self, generate_func):
        super().__init__()
        self.initUI(generate_func)

    def initUI(self, generate_func):
        layout = QVBoxLayout()
        self.generate_func = generate_func

        # Dropdown to select an HTML file
        self.place_dropdown = QComboBox()
        self.place_dropdown.addItems(
            ["Sampaloc, Manila", "Quiapo, Manila", "Tondo, Manila"]
        )

        self.amenity_dropdown = QComboBox()
        self.amenity_dropdown.addItems(["Schools", "Offices", "Hospitals"])

        # Button to open the selected HTML file
        self.button = QPushButton("Generate Route")
        self.button.clicked.connect(self.openRouteHtml)

        # Add widgets to layout
        layout.addWidget(self.place_dropdown)
        layout.addWidget(self.amenity_dropdown)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setWindowTitle("ODTC")
        self.setGeometry(200, 200, 300, 150)

    def openRouteHtml(self):
        amenities_dict = {"Schools": ["school", "college", "institute", "university"]}
        place = self.place_dropdown.currentText()
        amenity = amenities_dict.get(self.amenity_dropdown.currentText())
        self.web_viewer = WebEngineViewer(place, amenity, self.generate_func)


def gui(generate_func):
    app = QApplication(sys.argv)
    main_window = MainApp(generate_func)
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    print("gui")