from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
image = input("Input name of image file: ")

im = Image.open(image)
im = im.resize((1080, 1080))

draw = ImageDraw.Draw(im)
draw.text((0,0), "watermark", (255, 255, 255))
plt.subplot(1, 2, 1)
plt.imshow(im)
