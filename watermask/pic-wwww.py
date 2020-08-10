import os

from PIL import Image, ImageFont, ImageDraw


def add_text_to_image(imgpath="../img") :
    # imgpath  需要加水印的图片位置
    for parent, dirnames, filenames in os.walk(imgpath) :
        for filename in filenames :
            fullpath = os.path.join(parent, filename)
            if 'jpg' in fullpath :
                # 下面这两步是获取图片的名字,用于存储图片的时候 和原图保持一致
                image_name = os.path.split(fullpath)[1]
                name = os.path.splitext(image_name)[0]
                #  fullpath  图片的路径
                # 用RGBA的模式打开图片,
                im = Image.open(fullpath).convert('RGBA')
                # 创建一个和原图一样大小的图片
                txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
                # 设置字体的大小  可以根据自己的需求来,我这边是按照图片的宽度的1/10之一当做水印文字的大小
                font_size = int(txt.size[0] / 10)
                # 设置字体 
                fnt = ImageFont.truetype("c:/Windows/Fonts/Tahoma.ttf", font_size)
                # 在新建的图片上添加字体
                d = ImageDraw.Draw(txt)

                # 获取字体大小位置
                text_size_x, text_size_y = d.textsize(font_txt, font=fnt)
                # helloworld  水印文字
                # font 指定字体
                # fill 指定文字颜色和透明度
                d.text(((txt.size[0] - text_size_x) / 2, (txt.size[1] - text_size_y) / 2),
                       font_txt,
                       font=fnt,
                       fill=(255, 255, 255, 60))
                # 合并两张图片,并确定水印的位置
                out = Image.alpha_composite(im, txt)
                # out.show()
                # 由于我是用RGBA打开的图片,没有办法直接保存jpg  但是可以保存成png,想要保存jpg 需要先装换一个图片格式 out.convert('RGB')
                # RGBA意思是红色，绿色，蓝色，Alpha的色彩空间，Alpha指透明度。而JPG不支持透明度，所以要么丢弃Alpha,要么保存为.png文件
                out = out.convert('RGB')
                # 保存图片  路径+文件名字
                out.save("../img2/{}.jpg".format(name))