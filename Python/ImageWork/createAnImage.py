from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (128, 128), '#00FF00')
d = ImageDraw.Draw(im)

fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d.text((32,32), "Hello World", font=fnt, fill=(0, 0, 255))


im.show()
im.show()

im.save("image.png")