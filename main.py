import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel, QMainWindow
from split import FileDialogExample
from merge import MergeWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Example")

        # 创建一个QTabWidget
        tabWidget = QTabWidget()

        # 创建第一个标签页
        tab1 = FileDialogExample()

        # 创建第二个标签页
        tab2 = MergeWindow()

        # 添加标签页到QTabWidget
        tabWidget.addTab(tab1, "拆分")
        tabWidget.addTab(tab2, "合并")

        # 设置中心部件
        self.setCentralWidget(tabWidget)


def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()