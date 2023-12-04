import telebot
from telebot import types


bot = telebot.TeleBot('6944749448:AAGX5FiTCm1WXyXBsdNnLg-iU0Wkm98FdsU')


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я Официальный телеграм-бот сети магазинов видео игр GameNSK в городе Новосибирск. Чем я могу тебе помочь?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🎮О нас!')
        btn2 = types.KeyboardButton('📝Услуги')
        btn3 = types.KeyboardButton('📞Связь с Магазином')
        btn4 = types.KeyboardButton('📰Новостой канал')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓Задайте интересующий вас вопрос❓', reply_markup=markup)
    elif message.text == '📝Услуги':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('💿Обмен')
        btn2 = types.KeyboardButton('💰Trade-in')
        btn3 = types.KeyboardButton('⬅ Вернутся к Выбору.')
        markup.add(btn1, btn2, btn3 )
        bot.send_message(message.from_user.id, 'Выберете услугу', reply_markup=markup) 
    elif message.text == '📞Связь с Магазином':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🟢WhatsApp!')
        btn2 = types.KeyboardButton('⚪Telegram')
        btn3 = types.KeyboardButton('🔵VK')
        btn4 = types.KeyboardButton('🌐Наши сайты')
        btn5 = types.KeyboardButton('⬅ Вернутся к Выбору.')
        markup.add(btn1, btn2, btn3, btn4,btn5 )
        bot.send_message(message.from_user.id, 'Выберете Месенджер', reply_markup=markup) 
    elif message.text == '⬅ Вернутся к Выбору.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🎮О нас!')
        btn2 = types.KeyboardButton('📝Услуги')
        btn3 = types.KeyboardButton('📞Связь с Магазином')
        btn4 = types.KeyboardButton('📰Новостой канал')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓Задайте интересующий вас вопрос❓', reply_markup=markup)
    elif message.text == '📰Новостой канал':
        bot.send_message(message.from_user.id, 'Читайте новости ' + '[по ссылке](https://t.me/gamensk)', parse_mode='Markdown')
    elif message.text == '⚪Telegram':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🚉Метро Площадь Маркса')
        btn2 = types.KeyboardButton('🚉Метро Заельцовская')
        btn3 = types.KeyboardButton('🚉Метро Березовая Роща')
        btn4 = types.KeyboardButton('⬅ Вернутся к Выбору')
        markup.add(btn1, btn2, btn3, btn4 )
        bot.send_message(message.from_user.id, 'Выбирите станцию Метро', reply_markup=markup)
    elif message.text == '🚉Метро Площадь Маркса':
        bot.send_message(message.from_user.id, 'Telegram ' + '[по ссылке](https://t.me/+79061935141)', parse_mode='Markdown')
    elif message.text == '🚉Метро Заельцовская':
        bot.send_message(message.from_user.id, 'Telegram ' + '[по ссылке](https://t.me/+79833124833)', parse_mode='Markdown')
    elif message.text == '🚉Метро Березовая Роща':
        bot.send_message(message.from_user.id, 'Telegram ' + '[по ссылке](https://t.me/+79537777830)', parse_mode='Markdown')
    elif message.text == '🔵VK':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🚊Метро Площадь Маркса')
        btn2 = types.KeyboardButton('🚊Метро Заельцовская')
        btn3 = types.KeyboardButton('🚊Метро Березовая Роща')
        btn4 = types.KeyboardButton('⬅ Вернутся к Выбору')
        markup.add(btn1, btn2, btn3, btn4 )
        bot.send_message(message.from_user.id, 'Выбирите станцию Метро', reply_markup=markup)
    elif message.text == '🚊Метро Заельцовская':
        bot.send_message(message.from_user.id, 'Наш VK ' + '[по ссылке](https://vk.com/gamensk2)', parse_mode='Markdown')
    elif message.text == '🚊Метро Площадь Маркса':
        bot.send_message(message.from_user.id, 'Наш VK ' + '[по ссылке](https://vk.com/gamensk1)', parse_mode='Markdown')
    elif message.text == '🚊Метро Березовая Роща':
        bot.send_message(message.from_user.id, 'Наш VK ' + '[по ссылке](https://vk.com/gamenskviar)', parse_mode='Markdown') 
    elif message.text == '⬅ Вернутся к Выбору':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🟢WhatsApp!')
        btn2 = types.KeyboardButton('⚪Telegram')
        btn3 = types.KeyboardButton('🔵VK')
        btn4 = types.KeyboardButton('🌐Наши сайты')
        btn5 = types.KeyboardButton('⬅ Вернутся к Выбору.')
        markup.add(btn1, btn2, btn3, btn4,btn5 )
        bot.send_message(message.from_user.id, 'Выберете Месенджер', reply_markup=markup)
    elif message.text == '🟢WhatsApp!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
        btn1 = types.KeyboardButton('🚇Метро Площадь Маркса')
        btn2 = types.KeyboardButton('🚇Метро Заельцовская')
        btn3 = types.KeyboardButton('🚇Метро Березовая Роща')
        btn4 = types.KeyboardButton('⬅ Вернутся к Выбору')
        markup.add(btn1, btn2, btn3, btn4 )
        bot.send_message(message.from_user.id, 'Выбирите станцию Метро', reply_markup=markup)
    elif message.text == '🚇Метро Заельцовская':
        bot.send_message(message.from_user.id, 'WhatsApp ' + '[по ссылке](https://wa.me/79833124833)', parse_mode='Markdown')
    elif message.text == '🚇Метро Площадь Маркса':
        bot.send_message(message.from_user.id, 'WhatsApp ' + '[по ссылке](https://wa.me/79061935141)', parse_mode='Markdown')
    elif message.text == '🚇Метро Березовая Роща':
        bot.send_message(message.from_user.id, 'WhatsApp ' + '[по ссылке](https://wa.me/79537777830)', parse_mode='Markdown')  
    elif message.text == '🌐Наши сайты':
        bot.send_message(message.from_user.id, '🌐Наш сайт Маркса' + '[по ссылке](https://game-nsk.ru/?ysclid=lo6u6wx57c251650607)', parse_mode='Markdown')
        bot.send_message(message.from_user.id, '🌐Наш сайт Подземка ' + '[по ссылке](https://gamensk-podzemka.ru/)', parse_mode='Markdown')
    elif message.text == '🎮О нас!':
        bot.send_message(message.from_user.id, "👋 Преимущество покупки в GаmеNsk \n✔Защита от подделок, мы не продаем не оригинальный товар под видом оригинала.\n✔ Мы не бросаем своего покупателя: на все наши товары распространяется гарантия, как на б/у так и на новые.\n✔Вы покупаете только проверенную технику! Мы тестируем б/у технику и предоставляем вам время и возможность на проверку перед покупкой!\n✔Профессиональная консультация! Персонал в нашем магазине не просто продавцы, а настоящие специалисты! которые покажут, расскажут и научат вас пользоваться.\n🚛Доставка.Совершайте покупки не выходя из дома! \nМы занимаемся отправкой товаров по Городу, Области, а также в любой город России!\n🥇Репутация для нас не пустой звук!\n- Более 7 лет на рынке!\n- Большое количество положительных отзывов на Авито,Яндекс,2GIS.\n- Огромное количество постоянных и доверяющих нам клиентов", parse_mode= 'Markdown')
    elif message.text == '💿Обмен':
        bot.send_message(message.from_user.id, "Правила и Условия Обмена!!!\n1)Обмен равноценного диска стоит 200р.\nа)Если вы меняете диск стоимостью 800р на диск стоимостью 800р то оплата составит 200р.\nб)Если вы меняете диск стоимостью 800р на диск стоимостью 600р то оплата составит 200р за услугу обмена, но стоимость диска Уменьшается и при следующем обмене потерянная стоимость не учитывается!\nв)Если вы меняете диск стоимостью 800р на диск стоимостью 1000р то оплата составит 400р = 200р(Разница в стоимости дисков) + 200р за услугу обмена, но стоимость диска Возрастает!!!\n\n2)Обмен 2-х и более дисков на один возможен только по системе Trade - In!!!\nа)Вы не можете суммировать общую стоимость нескольких дисков для обмена на один дорогостоящий!\nб)Но вы можете погасить сумму разницы для обмена суммой от продажи ваших дисков!!!\n\n3)Обмен одного диска на два и более возможен!!!\nа)Предположим у вас диск стоимостью 1000р, но диск который вас интересует стоит 500р, и что бы не терять 500р вы можете выбрать диск в эту сумму или превышая её, как это будет выглядеть:500р+500р=1 000р оплата составит 400р за услугу обмена 2-х дисков.00+300+400=1 000р оплата составит 600р за услугу обмена 3-х дисков.\nб)Если же сумма выбранных вами дисков превышает стоимость вашего диска тогда это будет так:600+800=1 400-1 000=400(Разница в стоимости дисков)+ 400р за услугу обмена 2-х дисков, итого оплата составит 800р.\n\n4)Новые диски отличаются по стоимости от Б\У!!!\nа)Если вы берёте диск Новый в упаковке(Плёнке), то после его вскрытия его стоимость приравнивается к Б\У. Пример:Вы поменяли свой Б\У диск стоимостью 1200р на Новый диск стоимостью 1300р с доплатой в 300р.Но после распаковки ваш Новый диск стал Б\У и его стоимость теперь 1000р, и при следующем обмене будет учтена именно она!!!\n\n5)Обмен на НОВИНКИ и РЕДКИЕ ДИСКИ возможен только по системе TRADE-IN!!!\n\n6)Диски со временем теряют в цене, и это нормально!!!\nа)Вы купили диск. Прошли игру за неделю, пришли меняться, стоимость диска может измениться в меньшую сторону, по причинам которые от нас не зависят:№1) СКИДКИ в крупных сетевых магазинах!№2) Понижение РРЦ(Рекомендованная Розничная Цена)!№3) Спрос и актуальность!\n\n7) Мы не можем принимать все диски без разбора!\nа)У нас есть СТОП-лист!!!Это список игр, которые по тем или иным причинам временно не принимаются к обмену. Надеемся что вы отнесётесь с пониманием! Мы делаем это не из вредности, а для того, чтобы наш ассортимент смог удовлетворить игровой аппетит каждого из вас!\nб)Обратите внимание, что СТОП-листы магазинов нашей сети отличаются! То что не подлежит обмену в одном, могут с радостью принять в другом!\n\n8)При обмене дисков проверяйте приобретаемый товар на месте, не отходя от кассы.", parse_mode= 'Markdown')
    elif message.text == '💰Trade-in':
         bot.send_message(message.from_user.id, "Что же такое ''Traid-In''? \nЕсли переводить дословно то ''В обмен'' .\nТо есть, вы можете приобрести товар сдав то что у вас имеется в счëт погашения части стоимости приобретаемого товара. \nНапример:Вы хотите приобрести очки виртуальной реальности стоимостью 30.000₽, а у вас дома есть старая игровая приставка с дисками. Предположем мы ваш комплект оцениваем в 10.000₽. Соответственно доплата на желаемое устройство составит 20.000₽.", parse_mode= 'Markdown')
@bot.message_handler(content_types=['Photo'])
def get_text_messages(message):   
    if message.photo : 
        bot.send_message.photo.file_id
bot.polling(none_stop=True, interval=0)