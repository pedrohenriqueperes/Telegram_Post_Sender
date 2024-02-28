import telebot
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

import time
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Substitua "SEU_TOKEN_AQUI" pelo token do seu bot
TOKEN = os.getenv('bot_token')
# Substitua 'SEU_CANAL_ID' pelo ID do seu canal
CHANNEL_ID =os.getenv('channel_id')
# Diretório contendo as mídias a serem enviadas
MEDIA_DIR = ''

bot = telebot.TeleBot(TOKEN)

def create_markup():
    markup = InlineKeyboardMarkup()
    # Adicione quantos botões você quiser aqui
    # O texto do botão e o URL podem ser personalizados
    botao1 = InlineKeyboardButton("Texto do botão 1", url="https://www.google.com/search?client=opera&hs=GtP&sca_esv=4fbfcb9c8f0bb25b&sca_upv=1&sxsrf=ACQVn08M31unlS4Jaw_D1_AdDvz3n2vcKQ:1709132615773&q=rua+tempranillo+sao+roque+cep&uds=AMwkrPtf40cQEE8x2HwLs_wcbJ5sTaYV728a6Oo4gzJVURqGeCk0ibt5Xu_CF6MkxRUSI1EgA0Ak6CyEROlJx8WTcPpmcqIeBz3lJJmc8DpEYvmbZqj51DeS_K8VpHnMyVbHjbKupOfMRdDpELWNaRgri3Fl7j0ef6AmGQ6vU28Nr0dTDX9tJFC3GsqEt4iCgGoJJWfhPxiNQPF11tmgQ7H6r095S8HunIELmjXpP_Tmjl-dQCM8x8JMf71U1YXWBTrqYgdxxZWm7cAY8OWmLQ6gokUIQPRSPoJZH_ITn1AnyUfqc50NsSgGzYQ2Sh6bN1x0jG4a-4XyxdDFB5j1k4Zxbj5YLkzOZA&udm=2&prmd=misvnbtz&sa=X&ved=2ahUKEwjisL-Tp86EAxVPJbkGHTqWDUIQtKgLegQIChAB&biw=1256&bih=628&dpr=2#vhid=H6UrXXakD8VMmM&vssid=mosaic")
    botao2 = InlineKeyboardButton("Texto do botão 2", url="https://www.google.com/search?client=opera&hs=GtP&sca_esv=4fbfcb9c8f0bb25b&sca_upv=1&sxsrf=ACQVn08M31unlS4Jaw_D1_AdDvz3n2vcKQ:1709132615773&q=rua+tempranillo+sao+roque+cep&uds=AMwkrPtf40cQEE8x2HwLs_wcbJ5sTaYV728a6Oo4gzJVURqGeCk0ibt5Xu_CF6MkxRUSI1EgA0Ak6CyEROlJx8WTcPpmcqIeBz3lJJmc8DpEYvmbZqj51DeS_K8VpHnMyVbHjbKupOfMRdDpELWNaRgri3Fl7j0ef6AmGQ6vU28Nr0dTDX9tJFC3GsqEt4iCgGoJJWfhPxiNQPF11tmgQ7H6r095S8HunIELmjXpP_Tmjl-dQCM8x8JMf71U1YXWBTrqYgdxxZWm7cAY8OWmLQ6gokUIQPRSPoJZH_ITn1AnyUfqc50NsSgGzYQ2Sh6bN1x0jG4a-4XyxdDFB5j1k4Zxbj5YLkzOZA&udm=2&prmd=misvnbtz&sa=X&ved=2ahUKEwjisL-Tp86EAxVPJbkGHTqWDUIQtKgLegQIChAB&biw=1256&bih=628&dpr=2#vhid=H6UrXXakD8VMmM&vssid=mosaic")
    markup.add(botao1)
    markup.add(botao2)
    return markup

def send_media():
    for file in os.listdir(MEDIA_DIR):
        file_path = os.path.join(MEDIA_DIR, file)
        if os.path.isfile(file_path):
            caption = "Sua legenda aqui"  # Personalize sua legenda
            markup = create_markup()
            with open(file_path, 'rb') as media:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    bot.send_photo(CHANNEL_ID, media, caption=caption, reply_markup=markup)
                elif file.lower().endswith(('.mp4', '.avi', '.mov')):
                    bot.send_video(CHANNEL_ID, media, caption=caption, reply_markup=markup)
                elif file.lower().endswith('.mp3'):
                    bot.send_audio(CHANNEL_ID, media, caption=caption, reply_markup=markup)
                else:
                    bot.send_document(CHANNEL_ID, media, caption=caption, reply_markup=markup)
            time.sleep(1)  # Espera por 3 minutos antes de enviar a próxima mídia

if __name__ == '__main__':
    while True:
        send_media()
