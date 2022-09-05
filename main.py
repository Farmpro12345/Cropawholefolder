from PIL import Image  
import glob
from ui import pic_input
from ui import pic_output
from ui import cord_input

image_list = []
cropped_images = []

canon = (129,129,1708,1268)
iphone = (200,129,1708,1268)
fail = (150,129,1514,1138)


for filename in glob.glob(pic_input + "*.jpg"):
    print(filename)
    img = Image.open(filename)
    image_list.append(img)

for image in image_list:
    image = image.crop(cord_input)
    cropped_images.append(image)

for (i, new) in enumerate(cropped_images):
    new.save('{}{}{}'.format(pic_output,i+1,'.jpg'))

