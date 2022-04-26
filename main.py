import telebot
from data_file import TOKEN, currency_dict
from extensions import CurrencyException, ExchangeCurrency


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f"Приветствую, {message.chat.username}! Я Валютный Бот и я могу:  \n- Показать список доступных валют через команду /values \
    \n- Вывести конвертацию валюты через команду: <имя валюты> <в какую валюту перевести> <количество переводимой валюты>\n \
- Напомнить, что я могу через команду /help")


@bot.message_handler(commands=['help'])
def helper(message: telebot.types.Message):
    text = 'Чтобы произвести конвертацию валют, введите команду в следующем формате: \n<имя валюты> <в какую валюту перевести> <количество переводимой валюты>\nЧтобы увидеть список всех доступных валют, введите команду\n/values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def send_values(message: telebot.types.Message):
    print(message.text)
    text_msg = 'Доступные валюты:'
    for key in currency_dict.keys():
        text_msg = '\n'.join((text_msg, key,))
    bot.reply_to(message, text_msg)


@bot.message_handler(content_types=['text'])
def verification_method(message: telebot.types.Message):
    try:
        convertible_data = message.text.split(' ')

        if len(convertible_data) != 3:
            raise CurrencyException('Введите команду или 3 параметра для конвертации валют.')

        currency_start, currency_convertible, amount = convertible_data
        total_result = ExchangeCurrency.verification_method(currency_start, currency_convertible, amount)
    except CurrencyException as e:
        bot.reply_to(message, f'{e}')
    except Exception as e:
        bot.reply_to(message, f'Запрос введен некорректно, попробуйте ещё раз.')
    else:
        currency_start_code = currency_dict[currency_start.lower()]
        currency_convertible_code = currency_dict[currency_convertible.lower()]
        text_result = f'Цена {amount} {currency_start_code} - {round(total_result, 2)} {currency_convertible_code}'
        bot.send_message(message.chat.id, text_result)


bot.polling(none_stop=True)