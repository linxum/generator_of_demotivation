import telebot
import requests
from PIL import Image, ImageDraw, ImageFont
import sts

# bot token
token = '5904940309:AAGQ91eWPYObgvclRE-hPaQcj0VjhPAMBkI'
custom_text = "вставить текст"
# creating a bot object
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def com_start(message):
    bot.send_message(message.chat.id,
                     "Привет! Это генератор демотивации! Напиши текст, пришли картинку и получишь мем!")


@bot.message_handler(commands=['help'])
def com_help(message):
    bot.reply_to(message, "Сначала текст, потом картинка, понял?")


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global custom_text

    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(token, file_info.file_path))

    bot.reply_to(message, "Работаем!")

    with open("photo.jpg", 'wb') as new_file:
        new_file.write(file.content)

    img = Image.open("photo.jpg")
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("Lobster-Regular.ttf", size=sts.scale_textsize(custom_text, img))
    W, H = img.size
    w, h = font.getbbox(custom_text)[2] - font.getbbox(custom_text)[0], font.getbbox(custom_text)[3]
    draw.text(((W - w) / 2, H - h), custom_text, fill=(255, 255, 255), font=font)

    img.save("photo_edited.jpg")

    bot.send_photo(message.chat.id, open('photo_edited.jpg', 'rb'))
    custom_text = "вставить текст"


@bot.message_handler(content_types=['text'])
def setup_text(message):
    global custom_text
    custom_text = message.text
    bot.send_message(message.chat.id, "Принял")


bot.polling()
