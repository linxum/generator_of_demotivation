from PIL import ImageFont

def scale_textsize(txt, image):
	fontsize = 1
	img_fraction = 0.50

	font = ImageFont.truetype("Lobster-Regular.ttf", fontsize)
	while int(font.getlength(txt)) < img_fraction * image.size[0]:
		fontsize += 1
		font = ImageFont.truetype("Lobster-Regular.ttf", fontsize)

	fontsize -= 1
	return fontsize
