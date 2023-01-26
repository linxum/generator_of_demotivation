from PIL import ImageFont

def scale_textsize(custom_text, img):
	fontsize = 1
	img_fraction = 0.50

	font = ImageFont.truetype("Lobster-Regular.ttf", fontsize)
	while int(font.getlength(custom_text)) < img_fraction * img.size[0]:
		fontsize += 1
		font = ImageFont.truetype("Lobster-Regular.ttf", fontsize)

	fontsize -= 1
	return fontsize
