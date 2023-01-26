from PIL import Image, ImageDraw, ImageFont

def scale_textsize(txt, image):
	fontsize = 1
	img_fraction = 0.50

	font = ImageFont.truetype("Lobster-Regular.ttf", fontsize)
	while int(font.getlength(txt)) < img_fraction * image.size[0]:
		# iterate until the text size is just larger than the criteria
		fontsize += 1
		font = ImageFont.truetype("Lobster-Regular.ttf", fontsize)

	# optionally de-increment to be sure it is less than criteria
	fontsize -= 1
	return fontsize
