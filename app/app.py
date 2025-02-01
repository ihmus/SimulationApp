from ui import Simulation                                                                                       #BİSMİLLAHİRRAHMANİRRAHİM
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.Qt3DExtras import Qt3DWindow
from PyQt5.QtWidgets import QWidget
from screeninfo import get_monitors

monitor = get_monitors()[0]  # Birinci ekranı al
screen_width = monitor.width
screen_height = monitor.height

#print(f"Ekran Genişliği: {screen_width}, Ekran Yüksekliği: {screen_height}")

class MainWindow(QMainWindow):
    def __init__(self,h,w):
        super().__init__()

        self.setWindowTitle("ortam")
        self.setGeometry(w//2-2*w//6,h//2-2*h//6,2*w//3,2*h//3)

        # Simulation (Qt3DWindow) nesnesini oluştur
        self.simulation = Simulation()

        # Qt3DWindow'u QWidget içine göm
        self.container = QWidget.createWindowContainer(self.simulation)

        # Ana pencereye widget eklemek için layout kullan
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.container)
        central_widget.setLayout(layout)

        # QMainWindow’un ana widget'ı olarak ayarla
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow(screen_height,screen_width)
    window.show()
    app.exec_()