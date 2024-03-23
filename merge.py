import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton,
                             QFileDialog, QLineEdit, QLabel)
import pdf_utils as pdf


class MergeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.setWindowTitle('选择文件路径示例')
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText('待编辑的文件')
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText('待插入的文件')

        self.openFile1 = QPushButton('Open', self)
        self.openFile1.clicked.connect(self.openFileDialog1)
        self.openFile2 = QPushButton('Open', self)
        self.openFile2.clicked.connect(self.openFileDialog2)

        self.l1 = QLabel('插入位置在第几页之后:', self)
        self.l2 = QLabel('待插入文件的页码区间:', self)
        self.line_after = QLineEdit()
        self.line_start = QLineEdit()
        self.line_end = QLineEdit()

        self.button = QPushButton('插入')
        self.button.clicked.connect(self.insert_pdf)

        layout = QGridLayout()
        # self.setGeometry(20, 100, 400, 300)
        # self.setFixedSize(600, 400)
        layout.addWidget(self.input1, 0, 0, 1, 2)
        layout.addWidget(self.input2, 1, 0, 1, 2)

        layout.addWidget(self.openFile1, 0, 2, 1, 1)
        layout.addWidget(self.openFile2, 1, 2, 1, 1)

        layout.addWidget(self.l1,2,0,1,1)
        layout.addWidget(self.line_after, 2, 1, 1, 1)

        layout.addWidget(self.l2,3,0,1,1)
        layout.addWidget(self.line_start, 3, 1, 1, 1)
        layout.addWidget(self.line_end, 3, 2, 1, 1)

        layout.addWidget(self.button,4,1)   # 位于第2行第1列，占1行2列
        self.setLayout(layout)
        self.pdf_path1 = None
        self.pdf_path2 = None

        # self.show()
    def openFileDialog1(self):
        # 打开文件对话框，并获取选择的文件路径
        file_path = QFileDialog.getOpenFileName(self, '打开文件', '/', 'pdf(*.pdf)')[0]
        if file_path:
            self.pdf_path1 = file_path
            print(file_path)
            self.input1.setText(file_path)

    def openFileDialog2(self):
        # 打开文件对话框，并获取选择的文件路径
        file_path = QFileDialog.getOpenFileName(self, '打开文件', '/', 'pdf或图片(*.pdf *.jpg *.png)')[0]
        if file_path:
            self.pdf_path2 = file_path
            self.input2.setText(file_path)

    def insert_pdf(self):
        pdf.insert(
            self.pdf_path1,
            self.pdf_path2,
            self.line_after.text(),
            self.line_start.text(),
            self.line_end.text(),
            f'{self.pdf_path1[:-4]}-new.pdf'
        )