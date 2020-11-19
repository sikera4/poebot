import telebot
import random
import requests
from telebot import types
bot = telebot.TeleBot('1481033988:AAGT5qgfAJa-gzdHRztNkdxH_5HQ7YDFz4c')
signs = ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
signseng = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
      bot.send_message(message.from_user.id, text='Напиши привет!')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if "привет" in message.text.lower():
        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе гороскоп на сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        for i in range(len(signs) - 1):
              keyboard.add(types.InlineKeyboardButton(text = signs[i], callback_data = i))
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
  else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
      if call.data == 0:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 1:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 2:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 3:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 4:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 5:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 6:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 7:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 8:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 9:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 10:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      elif call.data == 11:
            url = 'https://horo.mail.ru/prediction/{}/today/'.format(signseng[call.data])
            response = requests.get(url)
            soup = BeautifulShop(response.text, 'html.parser')
            result = soup.findAll('div', class_ ="article__item article__item_alignment_left article__item_html")
            msg = result[0].text
      bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0, timeout=45)


            

