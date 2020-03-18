import random
import telebot
from news_parser import get_news

# выбор1: или при нажатии кнопкки "хочу статью" выдается выбор категорий:
# общие знания, знаменитые ученые, химия, физика, технологии, спелеология, софт, робототехника,
# психология, природа, палеонтология, здоровье и медицина, моя планета, математика, космонавтика, история,
# искусственный интеллект, интернет, геология, гаджеты, биология, астрономия, археология, антропология
# добавить кнопки на выбор
# https://new-science.ru/category/obshhie-znaniya/
# при выборе кнопки моделируется ссылка на рубрику
# со странички рубрики парсится список ссылок на ссответствующие статьи + краткие описания+ картинка (?)
# функция get_article(url, category)
# словарь или список? содержит: ссылка, заголовок, краткое описание, ссылка на картинку?
# список из N статей, N - лимит одной страницы. на каждой кнопке написано сколько статей осталось
bot = telebot.TeleBot('1039998429:AAGyq53ZL4jl_mD2u1KEtLdpiQK8xStcPm8')

url = 'https://new-science.ru/category/'

stickers = ['CAACAgIAAxkBAAOEXm0Sg7zAdv3eiz6EG4QgtAurMpsAAtYAA1advQoJdckM4i8hChgE',
            'CAACAgUAAxkBAAOFXm0ShemDHu8OsdAAAbf478JzXT0mAAL6AgAC6QrIA6RYNk_W-iAgGAQ',
            'CAACAgUAAxkBAAOGXm0ShyMtgYOjn7bBKuTagWt-naEAAicDAALpCsgDwj2O8ojHMrAYBA',
            'CAACAgIAAxkBAAOHXm0SiAqoG8CLqZN6jkaWoGvEbhsAAu0DAAJG-6wEqYSzfnPPLVMYBA',
            'CAACAgIAAxkBAAOIXm0SjIvUWLvZ2Rs8KW1iIxgDqNkAAggOAAKoCC8IOfQUNoQNvPAYBA',
            'CAACAgEAAxkBAAOJXm0So3LCJZZFcx3lfN9bkIFfTrkAAmAUAAKZf4gCkyWiP-DjRjEYBA',
            'CAACAgQAAxkBAAOKXm0Spr5Y9_3lXQlZ7BAgBLkMajoAAggBAAJrrl4J-BOB9Az3XNQYBA'
            'CAACAgQAAxkBAAOLXm0SqHPhAVbwrRtgBI3mr404rjIAAlgBAAJrrl4JY8qtau-m4X0YBA',
            'CAACAgIAAxkBAAOMXm0Squ66b7ZGat-2VVux9scHxj0AAnsBAAJcmYoKxaO-l5I_hQABGAQ',
            'CAACAgIAAxkBAAONXm0Sq2bMWnm2W9FkJ_7jx_yVC2YAAoMBAAJcmYoK_wRa_GX1YNQYBA',
            'CAACAgQAAxkBAAOOXm0SrXlMvbUfas_IuitjF0UlGGgAAm4AAy_f-AmLP5tEToHkGxgE',
            'CAACAgUAAxkBAAOPXm0Sr7LaKeqlzUpbNmz6anSIFKwAAkUDAALpCsgDJ4NsWxfxrL0YBA',
            'CAACAgUAAxkBAAOQXm0SsVpCYlqGicxXMX84LY0D4fYAAvwCAALpCsgDvvvGy-HTuaMYBA',
            'CAACAgIAAxkBAAORXm0Ss1gYEnp7K3NPP4EGOraF0R8AAmoAA55wKw2FOONoFoD8ZhgE',
            'CAACAgIAAxkBAAOSXm0StKycmVRoxDT0uNnXMZ16TBkAAoQBAAJcmYoKbObzN2kdwywYBA',
            'CAACAgIAAxkBAAOTXm0StZghuMS1XkZYPbOGsuAigxQAAn4BAALEq2gLiWJgo2uWbuIYBA',
            'CAACAgIAAxkBAAOUXm0StzcSpXCL8q4Bf28RRTDNotkAAvMKAAIvD_AGfM15v1ybFFQYBA',
            'CAACAgIAAxkBAAOVXm0SuK7OhdMS_z58_z78wejeXosAAggIAAJcAmUD6Xh4kegDn8AYBA',
            'CAACAgIAAxkBAAOWXm0Suj2tIMmKT1GEZgzAHYaqSTAAAvkAAzDUnRFfaF64mrzqzRgE',
            'CAACAgIAAxkBAAOXXm0Su6XqNPHTf0RDLpnMbqcqo_YAAn8EAAIQixUAARMM7AYE6otzGAQ',
            'CAACAgIAAxkBAAOYXm0SvfFC28T-9A0Mdm_iJg5-ckkAAuoAA1yZigpVjrZbba5wxRgE',
            'CAACAgIAAxkBAAOZXm0Sv79kUWxITVUw-hcwPg8_4HsAAgEAA8A2TxMYLnMwqz8tURgE',
            'CAACAgQAAxkBAAOaXm0SwcC4QZJXk424wKXPbKRQ1IsAAloBAAJrrl4JvAABBj20QdhpGAQ',
            'CAACAgIAAxkBAAObXm0Sx-4R4dXY9DlSE_-DbNZGTmIAAlQAA55wKw0hBaWjbvXPCBgE',
            'CAACAgUAAxkBAAOcXm0Sy750br0kwGHeD1Aj5yAoq6gAAjsDAALpCsgDrvLm1uPuKy0YBA',
            'CAACAgIAAxkBAAOdXm0S4hob612xBfV5k501ty-NwOEAAt0KAAJb1ikAAW_Wf6NhMAh0GAQ',
            'CAACAgIAAxkBAAOeXm0S6nDpEGCtmwQ0LEUcWfSgteUAAgEAAztgJBTVZYCBD8F1eBgE',
            'CAACAgIAAxkBAAOfXm0S8FXMBdTJIitcqiUl8w0i7WkAAigBAAIQIQIQwL8KBjmgc9sYBA',
            'CAACAgIAAxkBAAOgXm0S9YMrxW_DsVuluD5-9EvFgNcAAj0AAx8BTBX8tw7sli8UCBgE',
            'CAACAgIAAxkBAAOhXm0S_1f_9NVbMKKXcK5yqzKZdWQAAvQCAAKW-hIFwTe1E0FNgzoYBA',
            'CAACAgIAAxkBAAOiXm0TBgtesNqC-cd-SG9ge8aBLFUAAsUDAALyfoIMV6vmPWPo-T4YBA',
            'CAACAgQAAxkBAAOjXm0TEdlR-85xF1STPU2gmGXIyxcAAmkAAy_f-AnTEav2EF8yUhgE',
            'CAACAgUAAxkBAAOkXm0TIPki0zMfA2oROoJWt9lq_McAAlgAAwxgswiJJr4n3T7tBxgE',
            'CAACAgIAAxkBAAOlXm0TJIHjUX1wcwABgx4EShLASRAGAALCAANcmYoKmiPRSMYMNH0YBA',
            'CAACAgQAAxkBAAOmXm0TLg4sfk24eG1JF9-MCk4j6r0AAggBAAJrrl4J-BOB9Az3XNQYBA',
            'CAACAgQAAxkBAAOnXm0TL8EhN2MmL7M0u-zZFQaLvOsAAiMBAAJrrl4JGNATQcxhUIIYBA',
            'CAACAgQAAxkBAAOoXm0TNjAgsKmKoo9xqdk-o4uQwUYAAlwBAAJrrl4J4HxS03d1fGQYBA',
            'CAACAgIAAxkBAAOpXm0TRzeIWIzHPhjTNHlvKTd3EIAAAoMBAAJLDg8AARE0PQslDSX8GAQ',
            'CAACAgIAAxkBAAOqXm0TSwGtLsb73hXZBP_PMNZngbQAAn8BAAJLDg8AAW-ufXZOMLeBGAQ',
            'CAACAgIAAxkBAAOrXm0TUoNu2lhoAAGr_GSBcQcVqJQNAAKPAQACSw4PAAHjCLpoFaf33RgE',
            'CAACAgEAAxkBAAOsXm0TZlh1fXVso-w01G_S8hP-oP4AAjsUAAKZf4gCvP67qmd2-4wYBA',
            'CAACAgIAAxkBAAOtXm0Th19Y_JEOTttRgq-e3_zmb_sAAgcKAAIvD_AGmK9cwcsnrDwYBA',
            'CAACAgIAAxkBAAOuXm0TnI5D6GmwbOi1crtXCntwixIAAjsBAAJSFWwAAQHiN11JPakxGAQ'
            ]


@bot.message_handler(content_types=['sticker'])
def send_text(message):
    print(message)


# список с шутками
jokes = ['Эйнштейн, Паскаль и Ньютон играют в прятки. Эйнштейн считает, а тем временем Паскаль и Ньютон должны '
         'прятаться. Паскаль убегает и успешно прячется, а Ньютон и не собирается никуда бежать. Вместо этого '
         'он чертит вокруг себя на земле квадрат. Эйнтштейн открывает глаза и говорит \n — Ньютон, как же просто '
         'было тебя найти! \n — Ничего подобного — отвечает он \n — Ты нашёл Паскаля! Обрати внимание на землю '
         '\n один Ньютон в квадрате!',

         "—  Как часто можно шутить о химии? \n— Периодически",

         "Шрёдингер ходил по комнате в поисках нагадившего котёнка, а тот сидел в коробке ни жив ни мертв",

         "Гелий заходит в бар и заказывает пиво.Бармен оборачивается и говорит: «Простите, мы не обслуживаем "
         "благородные газы».Гелий не реагирует.",

         "Чертов бозон Хиггса. Думает, что мир крутится вокруг него.",

         "Мало кто помнит лаборантку Пьера и Марии Кюри. Да она сильно и не светилась.",

         "Нейтрон заходит в бар и спрашивает: «Почем у вас выпивка?» Бармен отвечает: «Тебе хватит, "
         "ты уже и так заряжен».",

         "Тахион заходит в бар. Бармен ему: \n- Тахионы не обслуживаются! \n - Странно, — говорит тахион, — а"
         " завтра обслуживали».",

         "— Почему битная система имеет размер 32, 64, 128, 256, 512, 1024? \n— Ну, это же так просто! "
         "Вот смотри. Есть у тебя к примеру 1000 рублей. Или, для ровного счёта, 1024...",

         "Биолог, химик и статистик отправились на охоту. Биолог стреляет по оленю, но мажет на пять метров влево. "
         "Химик стреляет по оленю, не попадает, пуля застревает в дереве на пять метров вправо. Статистик: \n- Мы его "
         "подстрелили!»",

         "Черные дыры образовались там, где Бог поделил на ноль",

         "Словарь для математиков. Рекурсия (сущ.) - см. рекурсия.",

         " Трилогия Толкиена:\n1. Властелин Колец\n 2. Властелин Групп: Абелева группа.\n3. Властелин Полей: "
         "Делители нуля",

         "Типов людей всего 10: те, кто понимает двоичную систему счисления, и те, кто не понимает.",

         "Физику, математику и инженеру дали задание найти объём красного резинового мячика. "
         "Физик погрузил мяч в стакан с водой и измерил объём вытесненной жидкости. "
         "Математик измерил диаметр мяча и рассчитал тройной интеграл. Инженер достал из стола "
         "«Таблицу объёмов красных резиновых мячей» и нашёл нужное значение.",

         " Гейзенберг вел машину, когда его остановила дорожная полиция. \n - Вы что, не знаете, с какой скоростью "
         "Вы едете? — спросил его полицейский. \n— Нет», — ответил Гейзенберг, — Но я точно знаю, где я нахожусь в"
         " данный момент».",

         "На защите диссертации по теоретической физике диссертант неоднократно ссылается на какого-то Однокамушкина. "
         "После защиты один профессор подошел и тихо поинтересовался: \n— Кто этот Однокамушкин? \n— Это Эйнштейн.",

         "Математик жене:\n— Какая ты у меня компактная!\n— Маленькая и хрупкая?\n— Нет, замкнутая и ограниченная.",

         "Первый Закон экономистов: Для каждого экономиста найдётся такой, который с ним полностью согласен,"
         " и такой, который с ним полностью не согласен.\nВторой Закон экономистов: Они оба неправы.",

         "Шрёдингер и Гейзенберг едут по трассе на конференцию, Шрёдингер за рулём. Внезапно раздаётся удар и он "
         "останавливает машину. Гейзенберг выглядывает на дорогу: "
         "\n— Боже мой, похоже я сбил кота! \n— Он умер?\n— Не могу сказать точно.",

         "Математик идет по yлице, дyмает о своем. Вдрyг видит yказатель: 'К-мерный театр'. "
         "Интересно стало, решил посмотреть. Через некоторое время выходит:\n — К = 2",

         "При раскопках в Египте нашли саркофаг с мумией. Археологи многих стран пытались определить, чья она, "
         "но не смогли. За дело взялись советские 'эксперты'. Они попросили оставить их наедине с мумией. "
         "Через сутки вышли, утирая пот со лба. \n— Его звали Аменхотеп XXIII.  \n— Как вы это установили?  "
         "\n— Сам признался",

         "Заходят Вернер Гейзенберг, Курт Гёдель и Ноам Хомский в бар. Гейзенберг смотрит по сторонам и говорит:\n "
         "— Поскольку здесь находимся мы втроём, и поскольку здесь бар, то это — наверняка анекдот. "
         "Однако, остаётся один вопрос — смешной он или нет? \nГёдель на секунду задумывается и отвечает:"
         "\n — Ну, так как мы находимся внутри анекдота, мы не можем сказать, смешной он или нет."
         " Чтобы это понять, нам нужно взглянуть на него снаружи. \n Хомский смотрит на них и говорит:"
         "\n —Конечно же, он смешной. Вы просто неправильно его рассказываете. "]


# Команда \start
@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard0 = telebot.types.InlineKeyboardMarkup()

    # кнопка "хочу смехуёчек!"
    key_joke = telebot.types.InlineKeyboardButton(text='Хочу смехуёчек!', callback_data='joke')
    keyboard0.add(key_joke)

    # кнопка "Хочу все знать!"
    key_news = telebot.types.InlineKeyboardButton(text='Хочу все знать!', callback_data='news')
    keyboard0.add(key_news)

    # кнопка "в интернете все не правы! хочу статью!"
    key_article = telebot.types.InlineKeyboardButton(text='в интернете все не правы!', callback_data='article')
    keyboard0.add(key_article)

    # кнопка связи
    key_connection = telebot.types.InlineKeyboardButton(text='Связаться с создательницей', url='telegram.me/Veir_Rocky')
    keyboard0.add(key_connection)

    bot.send_message(message.chat.id, 'Привет! Краткий экскурс в мои скромные возможности: \n \n'
                                      'Если тебе скучно, то я могу развлечь научным анекдотом. Для этого нажми кнопку '
                                      ' "*Хочу смехуёчек!*"\n\n Если хочешь узнать что-то интересное из мира науки, '
                                      'то нажми кнопку "*Хочу всё знать!*"\n\n Если же тебе необходимо '
                                      'искрометно швырнуть в комментарий оппоненту не менее искрометную статью, '
                                      'подтверждающую'
                                      ' твой, безусловно, рациональный взгляд на мир, то тебе в рубрику *"В интернете '
                                      'все не правы!"*" \n\nЕсли же тебе срочно, просто невероятно экстренно необходимо '
                                      'связаться с Создательницей, то тебе на соответствующую кнопку со всеми '
                                      'пожеланиями\\жалобами\\предложениями\\замечаниями\\восхвалениями.\nНаслаждайся!'
                                      '\nP.S. Помни, что спорить с непробиваемым стереотипным '
                                      'сознанием чаще всего себе дороже. Но раз ты обратился ко мне, значит, '
                                      'безусловно, все  пид\*р\*сы, а ты Дартаньян!',
                     reply_markup=keyboard0, parse_mode="Markdown")


categories = {'Антропология': 'antropologiya', 'Археология': 'arheologiya',
              'Астрономия': 'astronomiya', 'Биология': 'biologiya',
              'Гаджеты': 'gadzhety', 'Геология': 'geologiya',
              'Интернет': 'internet', 'Искусственный интеллект': 'iskusstvennyj-intellekt',
              'История': 'istoriya', 'Космонавтика': 'kosmonavtika',
              'Математика': 'mathematics', 'Палеонтология': 'paleontologiya',
              'Природа': 'priroda', 'Психология': 'psihologiya',
              'Софт': 'soft', 'Спелеология': 'speleologiya',
              'Технологии': 'tehnologii', 'Физика': 'fizika',
              'Химия': 'himiya', 'Знаменитые ученые': 'znamenitye-uchjony',
              'Общие знания': 'obshhie-znaniya', 'Робототехника': 'robototehnika',
              'Здоровье и медицина': 'medicina', 'Моя планета': 'moya-planeta'}


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == "joke":
        msg = random.choice(jokes)
        sticker = random.choice(stickers)
        bot.send_message(call.message.chat.id, msg)
        bot.send_sticker(call.message.chat.id, sticker)
    if call.data == 'news':
        keyboard1 = telebot.types.InlineKeyboardMarkup()
        # кнопка "хочу смехуёчек!"
        for topic in categories:
            key_topic = telebot.types.InlineKeyboardButton(text=str(topic), callback_data=categories[topic])
            keyboard1.add(key_topic)
        bot.send_message(call.message.chat.id, 'Выбери категорию:', reply_markup=keyboard1, parse_mode="Markdown")
    if call.data == :
        bot.send_message(call.message.chat.id, 'ты выбрал категорию ' + str(categories[topic]),  parse_mode="Markdown")


bot.polling()