from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import reportlab.pdfbase.ttfonts
import os
import xlrd


# 创建pdf水印信息
def create_watermark(content) :
    """水印信息"""
    # 默认大小为21cm*29.7cm
    file_name = "mark.pdf"
    # 水印PDF页面大小
    c = canvas.Canvas(file_name, pagesize=(30 * cm, 30 * cm))
    # 移动坐标原点（坐标系左下为(0, 0))
    c.translate(4 * cm, 0 * cm)
    # 设置字体格式与大小，中文需要加载能够显示中文的字体，否则就会乱码
    # 注意字体路径
    try :
        pdfmetrics.registerFont(
            reportlab.pdfbase.ttfonts.TTFont('yahei', '/usr/share/fonts/dejavu/msyh.ttc'))
        c.setFont('yahei', 30)
    except :
        # 默认字体， 只能够显示英文
        c.setFont("Helvetica", 20)
        content = "watermark"

    # 旋转角度，坐标系被旋转
    c.rotate(30)
    # 指定填充颜色
    c.setFillColorRGB(0, 0, 0)
    # 设置透明度，1 为不透明
    c.setFillAlpha(0.20)
    # 画几个文本，注意坐标系旋转的影响
    for i in range(0, 30, 6):
        for j in range(-10, 30, 5):
            c.drawString(i * cm, j * cm, content)
    # 关闭并保存pdf文件
    c.save()
    return file_name


# 给每页pdf都加上水印
def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    pdf_output = PdfFileWriter()
    # 读取PDF文件
    if os.path.exists(pdf_file_in):
        input_stream = open(pdf_file_in, 'rb')

        pdf_input = PdfFileReader(input_stream, strict=False)

        # 获取PDF文件的页数
        pageNum = pdf_input.getNumPages()

        # 读入水印pdf文件
        pdf_watermask = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
        # 给每一页打水印
        for i in range(pageNum) :
            page = pdf_input.getPage(i)
            page.mergePage(pdf_watermask.getPage(0))
            # 压缩内容
            page.compressContentStreams()
            pdf_output.addPage(page)
        pdf_output.write(open(pdf_file_out, 'wb'))
    else :
        print(pdf_file_in + ' not exsit.')


# 图片添加水印
def add_text_to_image(image, text):
    font = ImageFont.truetype('/usr/share/fonts/dejavu/msyh.ttc', 46)

    # 添加背景
    new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # 添加水印
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(0, rgba_image.size[0], font_len * 40 + 200) :
        for j in range(0, rgba_image.size[1], 300) :
            image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 45))
    text_overlay = text_overlay.rotate(30)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    # 裁切图片
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text

# 将xlsx装换为csv文件
# def xlsx_to_csv_pd():
#     data_xls = pd.read_excel(r'D:\水印\files.xlsx', index_col=0)
#     data_xls.to_csv(r'D:\水印\files.csv', encoding='utf-8')

# 导入需要读取的第一个Excel表格的路径
data1 = xlrd.open_workbook(r'D:\水印\files.xlsx')
table = data1.sheets()[0]
# 创建一个空列表，存储Excel的数据
tables = []
# 将excel表格内容导入到tables列表中
def import_excel(excel) :
    for rown in range(excel.nrows) :
        tables.append(table.cell_value(rown, 0))

if __name__ == '__main__' :
    # 转换xlsx到csv格式
    # xlsx_to_csv_pd()
    # 将excel表格的内容导入到列表中
    import_excel(table)
    sum_pdf = 0
    sum_pic = 0
    sum_dot = 0
    for file in tables:
        # if os.path.exists(file):
        filename = os.path.basename(file)
        if file.endswith(('pdf', 'PDF')):
            sum_pdf += 1
            # pdf_file_in = '/databackup' + file
            # pdf_file_mark = create_watermark(r'中广核富盈')
            # pdf_file_out = '/watermarded/' + filename
            # print(pdf_file_out)
            # add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
        if file.endswith(('jpg', 'jpeg', 'JPG', 'JPEG', 'jfif', 'bmp', 'png', 'PNG')):
            sum_pic += 1
            # print(file)
            # img = Image.open(file)
            # im_after = add_text_to_image(img, u'中广核富盈')
            # if file.endswith(('jpg', 'jpeg', 'JPG', 'jfif')) :
            #     im = im_after.convert("RGB")
            #     im.save('/watermarded/' + filename)
            # else:
            #     im_after.save('/watermarded/' + filename)
        if file.endswith(('.')):
            sum_dot += 1
        total = sum_pdf + sum_pic + sum_dot
        print(
            "total : %d files exist. there are %d pdf, %d pic %d dot" % (total, sum_pdf, sum_pic, sum_dot))
