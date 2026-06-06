from PIL import Image, ImageFilter, ImageDraw, ImageFont
from pathlib import Path

#1
path = 'kartinka.jpg'
img = Image.open(path)
#img.show()
print(img.size, img.format, img.mode)


#2
new_size = (img.size[0] // 3, img.size[1] // 3)
resized_img = img.resize(new_size)

mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror_img = mirror_img.transpose(Image.FLIP_TOP_BOTTOM)
#mirror_img.show()

new_name = Path(path).stem + '_new' + Path(path).suffix
mirror_img.save(new_name)


#3
for i in range(1, 6):
    A = f'{i}.jpg'
    f_img = Image.open(A)
    f_img = f_img.filter(ImageFilter.EMBOSS)
    New_name = Path(A).stem + '_new' + Path(A).suffix
    f_img = f_img.save(New_name)
    #Image.open(New_name).show()


#4
imga = Image.open(path)

text = 'Pillow'
text_position = (100, 100)
transparency = 128
font = ImageFont.truetype('arial.ttf', size=180)

watermark = Image.new('RGBA', imga.size, (255, 255, 255, 0))
watermark_draw = ImageDraw.Draw(watermark)
watermark_draw.text(text_position, text, font=font, fill=(255, 255, 255, transparency))

watermarked_img = Image.alpha_composite(imga.convert('RGBA'), watermark)

watermarked_img.save('watermarked_img.png', 'PNG')
#Image.open('watermarked_img.png').show()
