# Write a telegram bot that takes an image and overlays text on top of it on Python

# importing necessary libraries 
import telebot
import requests
from PIL import Image, ImageDraw, ImageFont
import sts

# bot token 
token = '5904940309:AAGQ91eWPYObgvclRE-hPaQcj0VjhPAMBkI'
custom_text = "вставить текст"
# creating a bot object 
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start']) 
def start(message): 
	bot.send_message(message.chat.id, "Привет! Это генератор демотивации! Напиши текст, пришли картинку и получишь мем!")

@bot.message_handler(commands = ['help']) 
def help(message): 
	bot.reply_to(message, "Сначала текст, потом картинка, понял?")

@bot.message_handler(content_types = ['photo'])
def handle_photo(message):
	global custom_text

	# download the photo 
	fileID = message.photo[-1].file_id
	file_info = bot.get_file(fileID)
	file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

	bot.reply_to(message, "Работаем!")

	# save the photo
	with open("photo.jpg", 'wb') as new_file:
		new_file.write(file.content)

	# open the photo
	img = Image.open("photo.jpg")
	draw = ImageDraw.Draw(img)

	size = sts.scale_textsize(custom_text, img);
	font = ImageFont.truetype("Lobster-Regular.ttf", size = size)
	W, H = img.size

	draw.text(((W - int(font.getlength(custom_text))) /2, 0), custom_text, fill = (255, 255, 255), font = font)

	img.save("photo_edited.jpg")

	bot.send_photo(message.chat.id, open('photo_edited.jpg', 'rb'))

	custom_text = "вставить текст"

@bot.message_handler(content_types=['text'])
def setup_text(message):
	global custom_text
	custom_text = message.text
	bot.send_message(message.chat.id, "Принял")

bot.polling()
