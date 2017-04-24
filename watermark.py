'''
install Pillow using the following command
> pip install Pillow
'''
from PIL import Image, ImageDraw, ImageFont

def watermark(text):
    
    original = Image.open('C:\Ellen\photo\stone.jpg').convert('RGBA')
    imageWaterMark = Image.new('RGBA', original.size, (255,255,255,0))

    width, height = original.size
    draw = ImageDraw.Draw(imageWaterMark)
    font = ImageFont.truetype('arial.ttf', int(height/10))
    textwidth, textheight = draw.textsize(text, font)
    
    # calculate the x,y coordinates of the text
    # draw watermark in the middle of the photo
    x = (width - textwidth)/2
    y = (height - textheight)/2
    draw.text((x, y), text, font=font, fill=(255,255,255,128))

    out = Image.alpha_composite(original, imageWaterMark)
    out.show()
    out.save('C:\Ellen\photo\w.jpg')

def main():
    wartermark_text = input("Please enter the watermarking text: ")
    watermark(wartermark_text)
    
if __name__ == '__main__':
    main()
