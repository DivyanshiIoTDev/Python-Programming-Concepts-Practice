"""from PIL import Image

# Example usage of the image module
print("Image module imported successfully!")



# importing Image from PIL
from PIL import Image,ImageFilter#to apply blur effect
from PIL.ImageFilter import(BLUR,SHARPEN)
# open an image
img=Image.open("imgprac.png")
print(img.format)
width,height=img.size
crop_img=img.crop((0,0,width/2,height/2))
#crop_img.show()
crop_img.save("croppedimg.png")
crop_img=Image.open("croppedimg.png")#format of an image can oly be told when it has been opened
print(crop_img.format)
#Converting to bw with grayscale
scale='1'
grey_image=crop_img.convert("L")
#grey_image.show()
bw_image=crop_img.convert(scale)
#bw_image.show()
"""
#retrieving size of the image
from PIL import Image
with Image.open("imgprac.png") as image:
   width,height=image.size
   grey_img=image.convert('L')
   grey_img.show()
   print(width,height)
"""
#rotating an image
rotated_image=crop_img.rotate(75)
#rotated_image.show()
flipped_img=rotated_image.transpose(Image.FLIP_TOP_BOTTOM)
blur_img=crop_img.filter(BLUR)
flipped_img.show()

#converting to bw,greyscale
grey_scale=image.convert("L")
grey_scale.show()
#convert to greyscale then convert to bw
#using threshold
threshold=1
bw_image=grey_scale.convert(threshold)
bw_image.show()



# Apply a simple blur filter
#blurred_image = image.filter(ImageFilter.BLUR)
#blurred_image.show()

#To crop image using 4 valued tuple
crop_img=image.crop((0,0,width/2,height/2))
#crop_img.show()
#crop_img.save("croppedimg.png")
#Image.open("croppedimg.png").show()

#rotating the image
rotate_img=image.rotate(90)
rotate_img.show()

#saving an image by renaming
image.save("testimg.png")
image.show()

#to resize image using 2 tuple
resize_img=image.resize((width//2,height//2))
resize_img.show()


new_img=Image.open("croppedimg.png")
print(new_img)# not display the image itself but rather provide a representation of the Image object such as its format, size, and mode.


#transposing an image
transposed_img=img.transpose(Image.FLIP_TOP_BOTTOM)#flipping the image by 180 degree vertically
transposed_img2=img.transpose(Image.FLIP_LEFT_RIGHT)#flipping the image by 180 degree horizontally
transposed_img.show()
"""



