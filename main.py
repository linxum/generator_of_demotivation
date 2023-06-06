import telebot
import requests
from PIL import Image, ImageDraw, ImageFont
import sts
import time

token = '5904940309:AAGQ91eWPYObgvclRE-hPaQcj0VjhPAMBkI'
custom_text = "вставить текст"
custom_text_1 = "вставить текст"
custom_color = (255, 255, 255)
custom_font = "lobster"
custom_pos = -1
custom_size = 0

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def com_start(message):
    bot.send_message(
        message.chat.id, "Привет! Это генератор демотивации! Напиши текст, пришли картинку и получишь мем!")


@bot.message_handler(commands=['help', 'помощь'])
def com_help(message):
    bot.send_message(message.chat.id, "Изменение цвета текста (по умолчанию белый)")
    bot.send_message(message.chat.id, "/color [white] [black] [red] [blue] [green]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение цвета текста в системе RGB")
    bot.send_message(message.chat.id, "/rgb <R> <G> <B>")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение шрифта текста (по умолчанию Lobster)")
    bot.send_message(message.chat.id, "/font [lobster] [impact] [rodchenko]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение размера текста (по умолчанию автоматически, то есть 0)")
    bot.send_message(message.chat.id, "/size <размер>")
    time.sleep(1)
    bot.send_message(message.chat.id, "Изменение позиции текста (по умолчанию снизу)")
    bot.send_message(message.chat.id, "/pos [внизу] [вверху] [везде]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Если хочешь текст везде, то для верхнего поля напиши текст")
    bot.send_message(message.chat.id, "/text [текст]")
    time.sleep(1)
    bot.send_message(message.chat.id, "Дальше пишешь (нижний) текст и отправляешь картику")


def extract_arg(arg):
    return arg.split()[1:]


@bot.message_handler(commands=['color', 'цвет'])
def setup_color(message):
    global custom_color
    set_color = extract_arg(message.text)
    if set_color:
        if set_color[0] == "black" or set_color[0] == "Black" or set_color[0] == "черный" or set_color[0] == "Черный"  \
                or set_color[0] == "чёрный" or set_color[0] == "Чёрный":
            custom_color = (0, 0, 0)
            bot.reply_to(message, "Принял черного")
        elif set_color[0] == "white" or set_color[0] == "White" or set_color[0] == "белый" or set_color[0] == "Белый":
            custom_color = (255, 255, 255)
            bot.reply_to(message, "Принял белого")
        elif set_color[0] == "red" or set_color[0] == "Red" or set_color[0] == "красный" or set_color[0] == "Красный":
            custom_color = (255, 0, 0)
            bot.reply_to(message, "Принял красного")
        elif set_color[0] == "blue" or set_color[0] == "Blue" or set_color[0] == "Синий" or set_color[0] == "синий":
            custom_color = (0, 0, 255)
            bot.reply_to(message, "Принял синего")
        elif set_color[0] == "green" or set_color[0] == "Green" or set_color[0] == "зеленый" or set_color[0] == "Зеленый" \
                or set_color[0] == "Зелёный" or set_color[0] == "зелёный":
            custom_color = (0, 255, 0)
            bot.reply_to(message, "Принял зеленого")
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['rgb', 'ргб', 'кзс'])
def setup_rgb(message):
    global custom_color
    set_color = extract_arg(message.text)
    if set_color:
        custom_color = (int(set_color[0]), int(set_color[1]), int(set_color[2]))
        bot.reply_to(message, "Получил")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['font', 'шрифт'])
def setup_font(message):
    global custom_font
    set_font = extract_arg(message.text)
    if set_font:
        if set_font[0] == "impact" or set_font[0] == "Impact":
            custom_font = "impact"
            bot.reply_to(message, "Несу шрифт Impact")
        elif set_font[0] == "rodchenko" or set_font[0] == "Rodchenko":
            custom_font = "rodchenko"
            bot.reply_to(message, "Несу шрифт Rodchenko")
        elif set_font[0] == "lobster" or set_font[0] == "Lobster":
            custom_font = "lobster"
            bot.reply_to(message, "Несу шрифт Lobster")
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['pos', 'поз'])
def setup_pos(message):
    global custom_pos
    set_pos = extract_arg(message.text)
    if set_pos:
        if set_pos[0] == "внизу" or set_pos[0] == "Внизу":
            custom_pos = -1
            bot.reply_to(message, "Спускаю текст")
        elif set_pos[0] == "вверху" or set_pos[0] == "Вверху" or set_pos[0] == "сверху" or set_pos[0] == "Сверху":
            custom_pos = 1
            bot.reply_to(message, "Поднимаю текст")
        elif set_pos[0] == "везде" or set_pos[0] == "Везде":
            custom_pos = 0
            bot.reply_to(message, "Клонирую поле")
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['size', 'размер'])
def setup_size(message):
    global custom_size
    set_size = extract_arg(message.text)
    if set_size:
        if set_size[0] == "0" or set_size[0] == "0":
            custom_size = 0
            bot.reply_to(message, "Размер текста будет выбран автоматически")
        elif int(set_size[0]) > 0:
            custom_size = int(set_size[0])
            bot.reply_to(message, "Размер текста: " + set_size[0])
        else:
            bot.reply_to(message, "Не понял, повтори")
    else:
        bot.reply_to(message, "Не понял, повтори")


@bot.message_handler(commands=['text', 'текст'])
def setup_sec_text(message):
    global custom_text_1
    set_text = message.text[6:]
    if set_text:
        custom_text_1 = set_text
        print(custom_text_1)
    bot.reply_to(message, "Получено: " + custom_text_1)


@bot.message_handler(content_types=['photo'])
def create_photo(message):
    global custom_text, custom_text_1, custom_color, custom_font, custom_pos, custom_size
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
        if custom_font == "impact":
            font = ImageFont.truetype("impact.ttf", size=sts.scale_textsize(custom_text, img, custom_font))
        elif custom_font == "rodchenko":
            font = ImageFont.truetype("Rodchenko.ttf", size=sts.scale_textsize(custom_text, img, custom_font))
        else:
            font = ImageFont.truetype("Lobster.ttf", size=sts.scale_textsize(custom_text, img, custom_font))
    else:
        if custom_font == "impact":
            font = ImageFont.truetype("impact.ttf", size=custom_size)
        elif custom_font == "rodchenko":
            font = ImageFont.truetype("Rodchenko.ttf", size=custom_size)
        else:
            font = ImageFont.truetype("Lobster.ttf", size=custom_size)

    W, H = img.size
    w, h = font.getbbox(custom_text)[2] - font.getbbox(custom_text)[0], font.getbbox(custom_text)[3]

    if custom_pos == 1:
        draw.text(((W - w) / 2, 0), custom_text, fill=custom_color, font=font)
    elif custom_pos == -1:
        draw.text(((W - w) / 2, H - h), custom_text, fill=custom_color, font=font)
    else:
        draw.text(((W - w) / 2, 0), custom_text_1, fill=custom_color, font=font)
        draw.text(((W - w) / 2, H - h), custom_text, fill=custom_color, font=font)

    img.save("photo_edited.jpg")

    bot.send_photo(message.chat.id, open('photo_edited.jpg', 'rb'))
    custom_text = "вставить текст"
    custom_color = (255, 255, 255)
    custom_font = "lobster"
    custom_pos = False
    custom_size = 0


@bot.message_handler(content_types=['text'])
def setup_text(message):
    global custom_text
    custom_text = message.text
    bot.reply_to(message, "Получено: " + custom_text)


bot.polling()
