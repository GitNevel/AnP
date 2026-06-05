from PIL import Image, ImageDraw, ImageFont


img = Image.open('kartinka.jpg')

width, height = img.size
left = int(input('Введите высоту:'))
top = int(input('Введите ширину:'))
right = width - left
bottom = height - top

cropped_img = img.crop((left, top, right, bottom))

cropped_img.save("cropped_base.jpg")
#cropped_img.show()

#9.2
dict = {
    "Новый год": "1.jpg",
    "День рождения": "2.jpg"
}

holiday = input('Какой у вас праздник?')

if holiday in dict:
    name = dict[holiday]
    img = Image.open(name)
    #img.show()
else:
    print("Такого праздника нет в списке.")


#9.2
dict = {
    "Новый год": "1.jpg",
    "День рождения": "2.jpg"
}

holiday = input('Какой у вас праздник?')

if holiday in dict:
    name = input("Введите имя того, кого хотите поздравить: ")
    text = f"{name}, поздравляю!"

    name = dict[holiday]
    imga = Image.open(name)

    font = ImageFont.truetype("arial.ttf", size=60)
    text_position = (350, 100)
    transparency = 250

    watermark = Image.new('RGBA', imga.size, (255, 255, 255, 0))
    watermark_draw = ImageDraw.Draw(watermark)
    watermark_draw.text(text_position, text, font=font, fill=('Red'))

    watermarked_img = Image.alpha_composite(imga.convert('RGBA'), watermark)

    watermarked_img.save('watermarked_img.png', 'PNG')
    watermarked_img.show()
else:
    print("Такого праздника нет в списке.")
