import os
from PIL import Image

# Opens a image in RGB mode
imgs = [
    "eternal_life_demo_1.png",
    "eternal_life_demo_2.png",
    "eternal_life_demo_3.png",
    "eternal_life_demo_4.png",
    "eternal_life_demo_5.png",
]

# Setting the points for cropped image
left = 0
top = 0
right = 397
bottom = 322

for img in imgs:
    im = Image.open(img)
    # Cropped image of above dimension
    # (It will not change orginal image)
    im1 = im.crop((left, top, right, bottom))

    # Shows the image in image viewer
    im1.save(img)
