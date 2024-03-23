import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QPushButton,
                             QFileDialog, QLineEdit, QLabel)
import pdf_utils as pdf

class FileDialogExample(QWidget):
    def __init__(self):
        super().__init__()
        self.pdf_path = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('选择文件路径示例')

        # 创建一个按钮，点击后打开文件对话框
        self.openFileDialogButton = QPushButton('打开文件对话框', self)
        self.openFileDialogButton.clicked.connect(self.openFileDialog)
        self.file_path_label = QLabel('未选择文件', self)
        self.file_path_label.setWordWrap(True)
        # 创建输入框
        self.input1 = QLineEdit()
        self.input1.setPlaceholderText('起始页')
        self.input2 = QLineEdit()
        self.input2.setPlaceholderText('终止页')
        # 创建按钮，点击后获取输入值
        self.button = QPushButton('抽取')
        self.button.clicked.connect(self.handleButtonClick)

        self.result_label = QLabel('', self)
        self.result_label.setWordWrap(True)

        layout = QGridLayout()
        # self.setGeometry(20, 100, 400, 300)
        self.setFixedSize(600, 400)
        layout.addWidget(self.openFileDialogButton,0,0)
        layout.addWidget(self.file_path_label,1,0,1,2)
        layout.addWidget(self.input1,2,0)
        layout.addWidget(self.input2,2,1)
        layout.addWidget(self.button,3,0,1,2)   # 位于第2行第1列，占1行2列
        layout.addWidget(self.result_label, 4,0,1,2)
        self.setLayout(layout)

        self.show()

    def openFileDialog(self):
        # 打开文件对话框，并获取选择的文件路径
        file_path = QFileDialog.getOpenFileName(self, '打开文件', '/', 'pdf(*.pdf)')[0]
        if file_path:
            self.pdf_path = file_path
            print(file_path)
            self.file_path_label.setText(file_path)

    def handleButtonClick(self):
        # 获取输入值
        if not self.input1.text() or not self.input2.text() or not self.pdf_path:
            self.result_label.setText('empty input')
            return
        start_page = int(self.input1.text())
        end_page = int(self.input2.text())
        # 打印输入值，或者进行其他处理
        pdf_reader = pdf.read(self.pdf_path)
        page_count = pdf_reader.getNumPages()
        if end_page > page_count:
            end_page = page_count
        out_pdf_path = f'{self.pdf_path[:-4]}-{start_page}-{end_page}.pdf'
        res = pdf.split(pdf_reader, start_page, end_page, out_pdf_path)
        if res == 0:
            self.result_label.setText('error pages')
        else:
            self.result_label.setText(out_pdf_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialogExample()
    sys.exit(app.exec_())