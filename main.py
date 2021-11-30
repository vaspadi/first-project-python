from PIL import Image

def bilde():
  path = "images/mustang.jpeg"

  with Image.open(path) as img:
    print(path, img.format, f"{img.size[0]}x{img.size[1]} {img.mode}")
    img.show

bilde()