# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     pdf_mask
   Description :
   Author :       a
   date:          2020/7/11
-------------------------------------------------
"""

# 导入所需的Python库
# 使用两个第三方库来实现为PDF文件添加文字水印
# PyPdf2 和 reportlab
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
import reportlab.pdfbase.ttfonts
import os

# 创建水印信息
def create_watermark(content):
    """水印信息"""
    # 默认大小为21cm*29.7cm
    file_name = "mark.pdf"
    # 水印PDF页面大小
    c = canvas.Canvas(file_name, pagesize=(30 * cm, 30 * cm))
    # 移动坐标原点（坐标系左下为(0, 0))
    c.translate(4 * cm, 0 * cm)
    # 设置字体格式与大小，中文需要加载能够显示中文的字体，否则就会乱码
    # 注意字体路径
    try:
        pdfmetrics.registerFont(
            reportlab.pdfbase.ttfonts.TTFont('yahei', 'C:\Windows\Fonts\msyh.ttc'))
        c.setFont('yahei', 30)
    except:
        # 默认字体， 只能够显示英文
        c.setFont("Helvetica", 20)
        content = "watermark"

    # 旋转角度，坐标系被旋转
    # c.rotate(60)
    # 指定填充颜色
    c.setFillColorRGB(0, 0, 0)
    # 设置透明度，1 为不透明
    c.setFillAlpha(0.15)
    # 画几个文本，注意坐标系旋转的影响
    c.rotate(310)  # 旋转45度，坐标系被旋转
    for i in range(-30, 30, 8):
        for j in range(-20, 30, 7):
            c.drawString(i * cm, j * cm, content)

    # c.drawString(-7 * cm, 0 * cm, content)
    # c.drawString(7 * cm, 0 * cm, content)
    # c.drawString(0 * cm, 7 * cm, content)
    # c.drawString(0 * cm, -7 * cm, content)

    # 关闭并保存pdf文件
    c.save()
    return file_name

# 给每页pdf都加上水印
def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    pdf_output = PdfFileWriter()
    # 读取PDF文件
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermask = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermask.getPage(0))
        # 压缩内容
        page.compressContentStreams()
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))

    # 批量给文件夹中所有的PDF都打上水印
files = os.listdir('D:/水印前/')
print(files)
for file in files:
    if file.endswith(('pdf', 'PDF')):
        pdf_file_in = 'D:/水印前/' + file
        print(file)
        pdf_file_mark = create_watermark(r'中广核富盈')
        pdf_file_out = 'D:/水印后/tmp/' + file
        add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)

