import telebot
from PIL import Image
import pytesseract
import urllib.request
from io import BytesIO
from confiq import TOKEN


bot = telebot.TeleBot(TOKEN)


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

@bot.message_handler(content_types=['photo'])
def handle_images(message):
  
    photo = message.photo[-1]
    
  
    file_info = bot.get_file(photo.file_id)
    
   
    file_path = file_info.file_path
    
    
    image_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    image_bytes = BytesIO(urllib.request.urlopen(image_url).read())
    
    
    img = Image.open(image_bytes)
    
    
    lang = 'kir'
    text = pytesseract.image_to_string(img, lang=lang)
    
    
    bot.reply_to(message, text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Салам! Текстти таануу үчүн сүрөт жүктөө.")


bot.polling(none_stop=True)
