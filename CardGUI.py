from PIL import Image

img = Image.new('RGB', (64,64), "white") # create new white image
pix = img.load() # load pixel map
pix[32,32] = (255,0,0) # set some red pixels
pix[48,48] = (255,0,0)
pix[16,16] = (255,0,0)
img.show()