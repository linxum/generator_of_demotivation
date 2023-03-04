from PIL import ImageFont


def scale_textsize(custom_text, img, custom_font):
	fontsize = 1
	img_fraction = 0.50

	if custom_font == "impact":
		font = ImageFont.truetype("impact.ttf", fontsize)
	elif custom_font == "rodchenko":
		font = ImageFont.truetype("Rodchenko.ttf", fontsize)
	else:
		font = ImageFont.truetype("Lobster.ttf", fontsize)
	while int(font.getlength(custom_text)) < img_fraction * img.size[0]:
		fontsize += 1
		if custom_font == "impact":
			font = ImageFont.truetype("impact.ttf", fontsize)
		elif custom_font == "rodchenko":
			font = ImageFont.truetype("Rodchenko.ttf", fontsize)
		else:
			font = ImageFont.truetype("Lobster.ttf", fontsize)

	fontsize -= 1
	return fontsize
