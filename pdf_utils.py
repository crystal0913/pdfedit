# encoding:utf-8
from PyPDF3 import PdfFileReader, PdfFileWriter


def read(pdf_path: str):
    # 获取 PdfFileReader 对象
    return PdfFileReader(pdf_path)


def split(pdf_reader: PdfFileReader, start: int, end: int, out_path: str):
    if start < 1 or start > end:
        return 0
    pdfFileWriter = PdfFileWriter()
    for index in range(start-1, end):
        page_obj = pdf_reader.getPage(index)
        pdfFileWriter.addPage(page_obj)
    # 添加完每页，再一起保存至文件中
    with open(out_path, 'wb') as outf:
        pdfFileWriter.write(outf)
    return 1


def merge(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合并的文档的 list
    :param outFile:    合并后的输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter()
    for inFile in inFileList:
        # 依次循环打开要合并文件
        pdfReader = PdfFileReader(open(inFile, 'rb'))
        numPages = pdfReader.getNumPages()
        for index in range(0, numPages):
            pageObj = pdfReader.getPage(index)
            pdfFileWriter.addPage(pageObj)

        # 最后,统一写入到输出文件中
        pdfFileWriter.write(open(outFile, 'wb'))

def insert(pdf_file: str, insert_file: str, insert_after_page, start, end, output_pdf_path):
    orig_pdf = read(pdf_file)
    if not insert_after_page:
        insert_after_page = orig_pdf.getNumPages()  # 不填默认在文档末尾插入
    else:
        insert_after_page = int(insert_after_page)
    writer = PdfFileWriter()
    if insert_after_page > orig_pdf.getNumPages():
        insert_after_page = orig_pdf.getNumPages()
    if insert_file.endswith('pdf'):
        insert_pdf = read(insert_file)
        if not start:
            start = 1
        else:
            start = int(start)
        if not end:
            end = insert_pdf.getNumPages()
        else:
            end = int(end)
        # 插入指定页面前的所有页面
        for i in range(insert_after_page):
            writer.addPage(orig_pdf.getPage(i))
        # 插入新的文件
        for i in range(start-1, min(end, insert_pdf.getNumPages())):
            writer.addPage(insert_pdf.getPage(i))
        # 插入指定页面后的所有页面
        for i in range(insert_after_page, orig_pdf.getNumPages()):
            writer.addPage(orig_pdf.getPage(i))
        with open(output_pdf_path, 'wb') as out:
            writer.write(out)