from PIL import Image

def bilde():
  path = "images/mustang.jpeg"

  with Image.open(path) as img:
    print(path, img.format, f"{img.size[0]}x{img.size[1]} {img.mode}")
    img.resize((128, 128))
    img.rotate(45)
    img.show()
    img.save('new-image.jpeg')

bilde()