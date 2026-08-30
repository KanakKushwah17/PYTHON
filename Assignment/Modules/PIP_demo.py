from PIL import Image

image = Image.open(r"C:\PYTHON\Assignment\Modules\photo.jpg")

print("Image opened successfully!")
print("Size:", image.size)
print("Format:", image.format)

image.show()










#------------------------------------Width and Height----------------------------------------
width, height = image.size

print("Width:", width)
print("Height:", height)

























#-------------------------------------------Image Format---------------------------------
print(image.format)
"""PNG
JPG/JPEG
WEBP
BMP
GIF
    """



































#-----------------------------------Image Mode--------------------------------
print(image.mode)



























#----------------------------------- resize an image-----------------------------------
resized = image.resize((500, 300))

resized.show()
























#-------------------------------Save the resized image-------------------------------------
resized.save("small_photo.jpg")

















#------------------------------------Image crop---------------------------------
cropped = image.crop((100, 100, 500, 400))
#left,top,right,bottom

cropped.show()











#-------------------------------------Rotate an Image--------------------------------
rotated = image.rotate(90)

rotated.show()

#image.rotate(180)
#image.rotate(270)













#------------------------------------Flip an Image-----------------------------------
#horizontal
flipped = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

flipped.show()

#vertical
flipped = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

flipped.show()

















#----------------------------Convert Grayscale-----------------------
gray = image.convert("L")

gray.show()
































#--------------------------------Get Individual Pixels------------------
pixel = image.getpixel((100, 100))

print(pixel)


















#----------------------Change pixel----------------------------------------
image.putpixel((100, 100), (255, 0, 0))























#------------------------------Image Info------------------------------
print(image.info)
















#---------------------------Overall--------------------------------------
from PIL import Image

image = Image.open("photo.jpg")

print("Format:", image.format)
print("Size:", image.size)
print("Mode:", image.mode)

width, height = image.size

print("Width:", width)
print("Height:", height)

gray = image.convert("L")
gray.save("gray_photo.jpg")

print("Grayscale image created!")
