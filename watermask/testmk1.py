# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     testmk1
   Description :
   Author :       a
   date:          2020/7/10
-------------------------------------------------
"""
# coding:utf-8

# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import os
import xlrd

def add_text_to_image(image, text):
    font = ImageFont.truetype('C:\Windows\Fonts\msyh.ttc', 40)

    # 添加背景
    new_img = Image.new('RGBA', (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    new_img.paste(image, image.size)

    # 添加水印
    font_len = len(text)
    rgba_image = new_img.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)

    for i in range(0, rgba_image.size[0], font_len*40+40):
        for j in range(0, rgba_image.size[1], 160):
            image_draw.text((i, j), text, font=font, fill=(0, 0, 0, 45))
    # text_size_x, text_size_y = image_draw.textsize(text, font=font)
    # image_draw.text(((new_img.size[0] - text_size_x) / 2, (new_img.size[1] - text_size_y) / 2),
    #        text,
    #        font=font,
    #        fill=(0, 0, 0, 60))
    text_overlay = text_overlay.rotate(30)
    image_with_text = Image.alpha_composite(rgba_image, text_overlay)

    # 裁切图片
    image_with_text = image_with_text.crop((image.size[0], image.size[1], image.size[0] * 2, image.size[1] * 2))
    return image_with_text


#导入需要读取的第一个Excel表格的路径
# data1 = xlrd.open_workbook(r'D:\征信报告.xlsx')
# table = data1.sheets()[0]
# #创建一个空列表，存储Excel的数据
# tables = []
# #将excel表格内容导入到tables列表中
# def import_excel(excel):
#     for rown in range(excel.nrows):
#         tables.append(table.cell_value(rown,0))

# if __name__ == '__main__':
#     # 将excel表格的内容导入到列表中
#     import_excel(table)
#     for i in tables:
#         print(i)

if __name__ == '__main__':
    g = os.walk("D:/pic/")
    for path, d, filelist in g:
        for filename in filelist:
            if filename.endswith(('jpg', 'jfif', 'jpeg')):
                # print(os.path.join(path, filename))
                file = os.path.join(path, filename)
                print(file)
                print(filename)
                img = Image.open(file)
                im_after = add_text_to_image(img, u'中广核富盈')
                im = im_after.convert("RGB")
                im.save("D:/水印后/{}".format(filename))
            if filename.endswith(('bmp','png', 'PNG')):
                # print(os.path.join(path, filename))
                file = os.path.join(path, filename)
                print(file)
                print(filename)
                img = Image.open(file)
                im_after = add_text_to_image(img, u'中广核富盈')
                im_after.save("D:/水印后/{}".format(filename))
