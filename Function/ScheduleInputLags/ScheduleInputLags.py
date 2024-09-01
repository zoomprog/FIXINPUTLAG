import sys
import time
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
from pynput import keyboard
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)
        self.setParent(parent)
        self.ax.set_title('Input Lag Over Time')
        self.ax.set_xlabel('Key Press Index')
        self.ax.set_ylabel('Input Lag (seconds)')
        self.ax.grid(True)
        self.input_lags = []

    def update_plot(self):
        self.ax.clear()
        self.ax.bar(range(len(self.input_lags)), self.input_lags, color='green')
        self.ax.set_title('Input Lag Over Time')
        self.ax.set_xlabel('Key Press Index')
        self.ax.set_ylabel('Input Lag (seconds)')
        self.ax.grid(True)
        self.draw()

class ScheduleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Lag Tracker')
        self.setGeometry(100, 100, 800, 600)

        self.plot_canvas = PlotCanvas(self)
        self.setCentralWidget(self.plot_canvas)

        self.press_count = 0
        self.max_presses = 100
        self.start_time = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_key_presses)
        self.timer.start(100)

        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def check_key_presses(self):
        pass  # This can be used to periodically check something if needed

    def on_press(self, key):
        if self.start_time is None:
            self.start_time = time.time()
        else:
            end_time = time.time()
            input_lag = end_time - self.start_time
            self.plot_canvas.input_lags.append(input_lag)
            print(f"Input lag: {input_lag:.6f} seconds")
            self.start_time = None
            self.press_count += 1
            self.plot_canvas.update_plot()
            if self.press_count >= self.max_presses:
                self.listener.stop()

    def on_release(self, key):
        if key == keyboard.Key.esc:
            self.listener.stop()
            self.close()

