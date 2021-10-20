import io

from PIL import Image, ImageChops

def pil2jpg(im):
    jpg_file = io.BytesIO()
    im.save(jpg_file, format='JPEG')
    jpg_file.seek(0)
    return jpg_file

# https://stackoverflow.com/questions/10615901/trim-whitespace-using-pil
def trimSpaces(im_binary):
    im = Image.open(im_binary)
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        return pil2jpg(im.crop(bbox))