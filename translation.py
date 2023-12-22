translations = {
    'en': {
        'Успешная регистрация': 'Success registration',
        'Вы выбрали русский язык': 'You have chosen Russian language',
        'Вы выбрали английский язык': 'You have chosen English language',
        'Выберите язык': 'Select language',
        'Привет! Это бот шопа Fb аккаунтов Traffic Force': 'Hello! This is a Fb account shop bot Traffic Force',
        'Воспользуйтесь меню': 'Use the menu',
        '📱 Основное меню': '📱 Main menu',
        '📖 Правила&соглашения': '📖 Rules and agreements',
        '🛍 Товары': '🛍 Products',
        '📦 Категории': '📦 Categories',
        '📱 Контакты': '📱 Contacts us',
        '🛒 Мои покупки': '🛒 My purchases',
        '🔎 Поиск товаров': '🔎 Search for products',
        '📖 Правила&Соглашение': '📖 Rules&Agreement',
        '💰 Баланс профиля': '💰 Profile balance',
        '📺 О боте': '📺 About the bot',
        '📱 Открыть меню': '📱 Open menu',
        'Страница 1/1': 'Page 1/1',
        'Товары': 'Products',
        'Товар 1': 'Product 1',
        '⬅': '⬅',
        'Категории магазина': 'Store categories',
        'Саппорт': 'Support',
        'Баланс:': 'Balance:',
        '🤑 Пополнить баланс': '🤑 Top up balance',
        '👀 Ввести ваучер-код': '👀 Enter voucher code',
        'Введите что-то для поиска среди всех товаров': 'Enter something to search among all products',
        'Укажите сумму (число) в рублях на сколько хотите пополнить баланс': 'Specify the amount (number) in rubles by how much you want to top up your balance',
        'Пришлите ваучер-код. Если ваучер будет действительным, баланс будет зачислен!': 'Send me a voucher code. If the voucher is valid, the balance will be credited!',
        'А Вы точно совершали покупки с логином @ ❓ Я не смог найти ваши покупки!': "Have you definitely made purchases using login @ ❓ I couldn't find your purchases!!",
        'Это автоматический бот по продаже цифровых товаров! Такого бота удалось сделать с помощью аренды магазина в сервисе lequeshop.com Если нужен такой же бот, то бери ссылку выше и проходи регистрацию!': 'This is an automatic bot for selling digital goods! We managed to create such a bot by renting a store in the lequeshop.com service. If you need the same bot, then take the link above and register!'
    }
}


def _(text, lang='ru'):
    if lang == 'ru':
        return text
    else:
        global translations
        try:
            return translations[lang][text]
        except:
            return text
