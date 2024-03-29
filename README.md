# Generator of demotivation

Этот репозиторий содержит код для Telegram-бота для автоматического создания мемов-демотиваторов.

## Особенности

* Возможность расположить текст в 3 различных комбинациях (сверху, снизу и всё вместе).
* Выбор цвет шрифта и обводки как с помощью готовый пресетов, так и в палитре RGB.
* По умолчанию доступно 3 самых популярных шрифта для мемов (Lobster, Impact и Rodchenko).
* Размер текста может быть выбран автоматически или вручную.

## Начало работы

Чтобы развернуть бота на вашем сервере, выполните следующие шаги:

### Предварительные условия

Убедитесь, что у вас установлены:

- Python 3.8 или выше
- pip для установки зависимостей

### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/linxum/generator_of_demotivation.git
   cd generator_of_demotivation
   ```
2. Установите зависимости:
  ```bash
  pip install -r requirements.txt
  ```
3. В файле main.py добавьте ваш токен в кавычках Telegram-бота в следующую строчку, вместо token:
  ```python
  bot = telebot.TeleBot(token)
   ```
4. Запустите бота:
  ```bash
  python main.py
  ```

# Поддержка
Если вам нравится этот проект, вы можете поддержать нас звездочкой на GitHub.
