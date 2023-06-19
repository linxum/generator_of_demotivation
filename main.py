import telebot
import requests
from PIL import Image, ImageDraw, ImageFont
import sts
import time

black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
cyan = (0, 255, 255)
blue = (0, 0, 255)
magenta = (255, 0, 255)
white = (255, 255, 255)

token = '<YOUR TOKEN>'
upper_text = ""
lower_text = ""
custom_color = white
custom_stroke = black
custom_font = "lobster"
custom_size = 0

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def com_start(message):
    bot.send_message(
        message.chat.id, "Привет! Это генератор демотивации! Напиши текст, пришли картинку и получишь мем!")


@bot.message_handler(commands=['help'])
def com_help(message):
    bot.send_message(message.chat.id, "Изменение цвета текста (по умолчанию белый)")
    bot.send_message(message.chat.id, "/color [white] [black] [red] [blue] [green] [cyan] [magenta] [yellow]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение цвета текста в системе RGB")
    bot.send_message(message.chat.id, "/rgb <R> <G> <B>")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение цвета обводки текста (по умолчанию чёрная)")
    bot.send_message(message.chat.id, "/stroke [white] [black] [red] [blue] [green] [cyan] [magenta] [yellow]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение шрифта текста (по умолчанию Lobster)")
    bot.send_message(message.chat.id, "/font [lobster] [impact] [rodchenko]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение размера текста (по умолчанию автоматически, то есть 0)")
    bot.send_message(message.chat.id, "/size <размер>")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если хочешь текст сверху, то для верхнего поля напиши текст")
    bot.send_message(message.chat.id, "/upper [текст]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Дальше пишешь (нижний) текст и отправляешь картику")


def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['color'])
def setup_color(message):
    global custom_color
    set_color = extract_arg(message.text)
    if set_color:
        if set_color[0].lower() == "black":
            custom_color = black
            bot.reply_to(message, "Принял черный цвет")
        elif set_color[0].lower() == "white":
            custom_color = white
            bot.reply_to(message, "Принял белый цвет")
        elif set_color[0].lower() == "red":
            custom_color = red
            bot.reply_to(message, "Принял красный цвет")
        elif set_color[0].lower() == "blue":
            custom_color = blue
            bot.reply_to(message, "Принял синий цвет")
        elif set_color[0].lower() == "green":
            custom_color = green
            bot.reply_to(message, "Принял зеленый цвет")
        elif set_color[0].lower() == "cyan":
            custom_color = cyan
            bot.reply_to(message, "Принял голубой цвет")
        elif set_color[0].lower() == "yellow":
            custom_color = yellow
            bot.reply_to(message, "Принял желтый цвет")
        elif set_color[0].lower() == "magenta":
            custom_color = magenta
            bot.reply_to(message, "Принял фиолетовый цвет")
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['stroke'])
def setup_stroke(message):
    global custom_stroke
    set_stroke = extract_arg(message.text)
    print(set_stroke)
    if set_stroke:
        if set_stroke[0].lower() == "black":
            custom_stroke = black
            bot.reply_to(message, "Принял черную обводку")
        elif set_stroke[0].lower() == "white":
            custom_stroke = white
            bot.reply_to(message, "Принял белую обводку")
        elif set_stroke[0].lower() == "red":
            custom_stroke = red
            bot.reply_to(message, "Принял красную обводку")
        elif set_stroke[0].lower() == "blue":
            custom_stroke = blue
            bot.reply_to(message, "Принял синюю обводку")
        elif set_stroke[0].lower() == "green":
            custom_stroke = green
            bot.reply_to(message, "Принял зеленую обводку")
        elif set_stroke[0].lower() == "cyan":
            custom_stroke = cyan
            bot.reply_to(message, "Принял голубую обводку")
        elif set_stroke[0].lower() == "yellow":
            custom_stroke = yellow
            bot.reply_to(message, "Принял желтую обводку")
        elif set_stroke[0].lower() == "magenta":
            custom_stroke = magenta
            bot.reply_to(message, "Принял фиолетовую обводку")
        elif set_stroke[0].lower() == "nona":
            custom_stroke = custom_color
            bot.reply_to(message, "Обводка убрана")
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['rgb'])
def setup_rgb(message):
    global custom_color
    set_color = extract_arg(message.text)
    if set_color:
        custom_color = (int(set_color[0]), int(set_color[1]), int(set_color[2]))
        bot.reply_to(message, "Получил")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['font'])
def setup_font(message):
    global custom_font
    set_font = extract_arg(message.text)
    if set_font:
        if set_font[0].lower() == "impact":
            custom_font = "impact"
            bot.reply_to(message, "Несу шрифт Impact")
        elif set_font[0].lower() == "rodchenko":
            custom_font = "rodchenko"
            bot.reply_to(message, "Несу шрифт Rodchenko")
        elif set_font[0].lower() == "lobster":
            custom_font = "lobster"
            bot.reply_to(message, "Несу шрифт Lobster")
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['size'])
def setup_size(message):
    global custom_size
    set_size = extract_arg(message.text)
    if set_size:
        if set_size[0] == "0":
            custom_size = 0
            bot.reply_to(message, "Размер текста будет выбран автоматически")
        elif int(set_size[0]) > 0:
            custom_size = int(set_size[0])
            bot.reply_to(message, "Размер текста: " + set_size[0])
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['upper'])
def setup_sec_text(message):
    global upper_text
    set_text = message.text[7:]
    if set_text:
        upper_text = set_text
    bot.reply_to(message, "Получено: " + upper_text)


@bot.message_handler(commands=['lower'])
def setup_sec_text(message):
    global lower_text
    set_text = message.text[7:]
    if set_text:
        lower_text = set_text
    bot.reply_to(message, "Получено: " + lower_text)


@bot.message_handler(content_types=['photo'])
def create_photo(message):
    global upper_text, lower_text, custom_color, custom_font, custom_size, custom_stroke
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(
        token, file_info.file_path))

    bot.reply_to(message, "Работаем!")

    with open("photo.jpg", 'wb') as new_file:
        new_file.write(file.content)

    img = Image.open("photo.jpg")
    draw = ImageDraw.Draw(img)

    if custom_size == 0:
        if upper_text != "":
            if custom_font == "impact":
                font1 = ImageFont.truetype("impact.ttf", size=sts.scale_textsize(upper_text, img, custom_font))
            elif custom_font == "rodchenko":
                font1 = ImageFont.truetype("Rodchenko.ttf", size=sts.scale_textsize(upper_text, img, custom_font))
            else:
                font1 = ImageFont.truetype("Lobster.ttf", size=sts.scale_textsize(upper_text, img, custom_font))
        if lower_text != "":
            if custom_font == "impact":
                font2 = ImageFont.truetype("impact.ttf", size=sts.scale_textsize(lower_text, img, custom_font))
            elif custom_font == "rodchenko":
                font2 = ImageFont.truetype("Rodchenko.ttf", size=sts.scale_textsize(lower_text, img, custom_font))
            else:
                font2 = ImageFont.truetype("Lobster.ttf", size=sts.scale_textsize(lower_text, img, custom_font))

    else:
        if upper_text != "":
            if custom_font == "impact":
                font1 = ImageFont.truetype("impact.ttf", size=custom_size)
            elif custom_font == "rodchenko":
                font1 = ImageFont.truetype("Rodchenko.ttf", size=custom_size)
            else:
                font1 = ImageFont.truetype("Lobster.ttf", size=custom_size)
        if lower_text != "":
            if custom_font == "impact":
                font2 = ImageFont.truetype("impact.ttf", size=custom_size)
            elif custom_font == "rodchenko":
                font2 = ImageFont.truetype("Rodchenko.ttf", size=custom_size)
            else:
                font2 = ImageFont.truetype("Lobster.ttf", size=custom_size)

    W, H = img.size
    if upper_text != "":
        w1, h1 = font1.getbbox(upper_text)[2] - font1.getbbox(upper_text)[0], font1.getbbox(upper_text)[3]
        draw.text(((W - w1) / 2, 0), upper_text, fill=custom_color, stroke_fill=custom_stroke, font=font1,
                  stroke_width=5)
    if lower_text != "":
        w2, h2 = font2.getbbox(lower_text)[2] - font2.getbbox(lower_text)[0], font2.getbbox(lower_text)[3]
        draw.text(((W - w2) / 2, H - h2), lower_text, fill=custom_color, stroke_fill=custom_stroke, font=font2,
                  stroke_width=5)

    img.save("photo_edited.jpg")

    bot.send_photo(message.chat.id, open('photo_edited.jpg', 'rb'))
    upper_text = ""
    lower_text = ""
    custom_color = white
    custom_font = "lobster"
    custom_size = 0
    custom_stroke = black


@bot.message_handler(content_types=['text'])
def setup_text(message):
    global lower_text
    lower_text = message.text
    bot.reply_to(message, "Получено: " + lower_text)


bot.polling()
