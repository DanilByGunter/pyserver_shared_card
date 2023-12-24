import codecs

txt = 'INSERT INTO shop(id, name, name_en, status) VALUES'
ids = 1
shop_ru = [ "Пятерочка", "Перекресток", "Дикси", "Магнит", "У палыча",
            "ВкусВилл", "Магнолия", "Белорусский фермер", "Окей",
            "Виктория", "Лента", "Верный", "Атак", "Ашан", "Монетка",
            "Красное и белое", "Бристоль", "Азбука вкуса", "Фикспрайс",
            "Спар", "Караван", "Метро", "Продуктовый", "Гипермаркет",
            "Супермаркет", "Торговый Центр", "Рынок"]
shop_en = [ "Pyaterochka", "Crossroads", "Dixie", "Magnet", "At palych",
            "Vkusville", "Magnolia", "Belarusian farmer", "Okay",
            "Victoria", "Lenta", "Faithful", "Atak", "Auchan", "Coin",
            "Red and White", "Bristol", "ABC of Taste", "Fixprice",
            "Spar", "Caravan", "Metro", "Grocery", "Hypermarket",
            "Supermarket", "Shopping Center", "Market"]
for ru, en in zip(shop_ru, shop_en):
    txt += f''' ({ids},'{ru}','{en}',True),'''
    ids += 1

shop_ru = [ "Озон", "Яндекс Маркет", "Ламода", "Ебэй", "Амазон",
            "Алиэкспресс", "Вайлдберриз", "Онлайн-маркет", "СберМаркет",
            "Эльдорадо", "Золотое яблоко", "Рив Гош", "Будь Здоров",
            "Алия", "Летуаль", "Подружка", "Семь+я", "Магазин электроники", "Шоурум", 
            "Обувной магазин", "Строительный магазин", "Детский мир",
            "МВидео", "ДНС", "Спортмастер", "Икея", "ОБИ",
            "Гипермаркет", "Аптека", "Товары для животных",
            "Читай-город", "Туристический магазин", "Автомаркет",
            "Хоббилэнд", "Леонардо", "Соколов", "585 золото", "Санлайт",
            "Стим", "Сексшоп", "Б/у рынок", "Рынок"]
shop_en = [ "Ozon", "Yandex Market", "Lamoda", "Ebay", "Amazon",
            "Aliexpress", "Wildberries", "Online market", "Supermarket",
            "Eldorado", "Golden Apple", "Rive Gauche", "Be Healthy",
            "Aliya", "Letual", "Girlfriend", "Seven+Me", "Electronics Store", "Showroom",
            "Shoe store", "Hardware store", "Detsky Mir",
            "MVideo", "DNS", "Sportmaster", "Ikea", "OBI",
            "Hypermarket", "Pharmacy", "Pet products",
            "Read the city", "Tourist store", "Automarket",
            "Hobbyland", "Leonardo", "Sokolov", "585 gold", "Sunlight",
            "Steam", "Sex Shop", "Used market", "Market"]
for ru, en in zip(shop_ru, shop_en):
    txt += f''' ({ids},'{ru}','{en}',False),'''
    ids += 1
txt = txt[:len(txt)-1] + ';'

with codecs.open("3_shop.txt", "w", 'utf-16') as output:
    output.write(txt)
