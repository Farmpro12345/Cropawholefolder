from PIL import Image  # Import Image class from library.
import glob


image_list = []
cropped_images = []

canon = (129,129,1708,1268)
iphone = (200,129,1708,1268)
fail = (150,129,1514,1138)


for filename in glob.glob("C:\\Users\\sjurb\\Desktop\\testos\\1\\*.jpg"):
    print(filename)
    img = Image.open(filename)
    image_list.append(img)

for image in image_list:
    image = image.crop(canon)
    cropped_images.append(image)

for (i, new) in enumerate(cropped_images):
    new.save('{}{}{}'.format('C:\\Users\\sjurb\\Desktop\\testos\\2\\',i+1,'.jpg'))

