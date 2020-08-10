# /usr/bin/env python
# -*- coding:utf-8 -*-
# 本示例使用两个第三方库来实现为PDF文件添加文字水印
# 这两个库是pyPdf和reportlab
# 使用的Python版本是Python 2.7
# http://pybrary.net/pyPdf
# http://www.reportlab.com

import os
# 库文件的导入
from PyPDF2 import  PdfFileReader, PdfFileWriter # PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas

from PIL import Image, ImageDraw, ImageFont
import os

# 指定要使用的字体和大小；/Library/Fonts/是macOS字体目录；Linux的字体目录是/usr/share/fonts/
font = ImageFont.truetype('C:/Windows/Fonts/STXINGKA.TTF', 45)


# image: 图片  text：要添加的文本 font：字体
def add_text_to_image(image_name, text, font=font):
    image = Image.open(image_name)
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # 设置文本文字位置
    print(rgba_image)
    # text_xy = (rgba_image.size[0] - text_size_x, rgba_image.size[1] - text_size_y)  #底部
    # text_xy = ((rgba_image.size[0] - text_size_x) / 2, (rgba_image.size[1] - text_size_y) / 2)  # 中间
    text_xy = ((rgba_image.size[0] - text_size_x), 0)  # 中间
    # 设置文本颜色和透明度
    # image_draw.text(text_xy, text, font=font, fill=(76, 234, 124, 180))
    image_draw.text(text_xy, text, font=font, fill=(0, 0, 0))

    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text

def add_mark(info_name, text):
    print(info_name)
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas("watermark.pdf")
    c.setFont("Courier", 35)

    # 设置水印文字的灰度
    c.setFillGray(0.0, 1)

    # 设置水印文件，并将文字倾斜45度角
    c.saveState()
    c.translate(280, 750)
    c.rotate(0)
    c.drawCentredString(0, 0, text)
    c.restoreState()
    c.save()

    output = PdfFileWriter()
    input1 = PdfFileReader(open(info_name, 'rb'))
    water = PdfFileReader(open('watermark.pdf', 'rb'))

    # 获取pdf文件的页数
    pageNum = input1.getNumPages()
    print(pageNum)
    # 给每一页打水印
    for i in range(pageNum):
        page = input1.getPage(i)
        page.mergePage(water.getPage(0))
        output.addPage(page)
    return output

def run():
    # os.mkdir("D:/result/")
    file_name = "D:/水印前/"
    files = os.listdir(file_name)
    print(files)
    r = 0
    for t_file in files:
        file_all_img = file_name + os.sep + t_file
        if os.path.isfile(file_all_img):
            continue
        for file_img in os.listdir(file_all_img):
            file_img_all_img_all = file_all_img + os.sep + file_img
            if file_img_all_img_all.endswith('pdf'):
                out_put = add_mark(file_img_all_img_all, t_file)
                outStream = open('results' + os.sep + '{}.pdf'.format(r), 'wb')
                out_put.write(outStream)
                outStream.close()
                os.remove("watermark.pdf")
            else:
                im_after = add_text_to_image(image_name=file_img_all_img_all, text=t_file)
                im_after.save("results/{}.png".format(r))
            r += 1



if __name__ == '__main__':
    run()