import sys
import psutil
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TYUI V1.0")
        self.resize(800, 520)
        root = QWidget()
        layout = QVBoxLayout(root)
        title = QLabel("TYUI  |  System Monitor")
        title.setStyleSheet("font-size: 26px; font-weight: 700; color: #7ce4ff")
        self.cpu = QLabel()
        self.ram = QLabel()
        note = QLabel("Live CPU and RAM monitoring. Additional optimization features are not included in this baseline.")
        note.setStyleSheet("color: #9aa8c7; font-size: 12px")
        for item in (title, self.cpu, self.ram, note):
            layout.addWidget(item)
        layout.addStretch()
        self.setCentralWidget(root)
        self.setStyleSheet("QMainWindow, QWidget { background: #0c1019; color: #e8edff; font-family: 'Segoe UI'; font-size: 15px }")
        psutil.cpu_percent(interval=None)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh)
        self.timer.start(1000)
        self.refresh()

    def refresh(self):
        self.cpu.setText(f"CPU usage: {psutil.cpu_percent(interval=None):.1f}%")
        memory = psutil.virtual_memory()
        self.ram.setText(f"RAM: {memory.percent:.1f}% used | {memory.available / 1024**3:.1f} GB available / {memory.total / 1024**3:.1f} GB total")


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("TYUI")
    app.setApplicationVersion("1.0.0")
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
