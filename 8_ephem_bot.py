"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem, datetime
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

ephem_built_in_planets = [name for _0, _1, name in ephem._libastro.builtin_planets()]
# список планет и лун с которыми работает модуль EPHEM

PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def locator(user_text_split):
    try:
      name = user_text_split[1].capitalize() # первый аттрибут после команды planet
    except IndexError:
      return "Не введено имя планеты"
    try:
      date = user_text_split[2] # пробуем взять второй аргумент
    except IndexError:
      date = datetime.datetime.now() # если второго не было, берем текущую дату/время
    if name in ephem_built_in_planets:
      return ephem.constellation(getattr(ephem, name)(date))
    else:
      return name + " Не название планеты/луны"

def find_constellation(update, context):
    update.message.reply_text('Ищем положение планеты по названию и дате: ')
    user_text = update.message.text.split(" ")
    update.message.reply_text(locator(user_text))
        
def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
