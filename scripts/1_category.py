import codecs

txt = 'INSERT INTO category(id, name, name_en, status) VALUES'

category_ru = ["Готовая еда", "Овощи", "Зелень", "Фрукты", "Ягоды", 
               "Молоко", "Кисломолочные продукты", "Яичные продукты",
               "Мясо", "Мясные субпродукты", "Курица", "Куриные субродукты",
               "Рыба", "Морепродукты", "Сыры", "Творог", " Молочные продукты",
               "Соевые продукты", "Грибы", "Жиры", "Масла", "Орехи",
               "Крупы и злаки", "Специи и пряности", "Мука", "Хлеб",
               "Макароны и паста", "Семена", "Сладости", "Кондитерские изделия",
               "Фастфуд", "Напитки", "Соки", "Лимонады", "Алкоголь",
               "Вегатарианские продукты", "Веганские продукты",
               "Кофе", "Чай", "Полуфабрикаты", "Снеки", "Консервация",
               "Детское питание", "Хлебобулочные изделия", "Другое"]
category_en = ["Ready-made food", "Vegetables", "Greens", "Fruits", "Berries",
                "Milk", "Fermented dairy products", "Egg products",
                "Meat", "Meat offal", "Chicken", "Chicken offal",
                "Fish", "Seafood", "Cheeses", "Cottage cheese", " Dairy products",
                "Soy products", "Mushrooms", "Fats", "Oils", "Nuts",
                "Cereals and cereals", "Spices and spices", "Flour", "Bread",
                "Pasta and pasta", "Seeds", "Sweets", "Confectionery",
                "Fast food", "Drinks", "Juices", "Lemonades", "Alcohol",
                "Vegetarian products", "Vegan products",
                "Coffee", "Tea", "Semi-finished products", "Snacks", "Preservation",
                "Baby food", "Bakery products", "Other"]
ids = 1
for ru, en in zip(category_ru, category_en):
    txt += f''' ({ids},'{ru}','{en}',True),'''
    ids += 1

category_ru = ["Электроника", "Одежда", "Обувь", "Дом и сад",
               "Детские товары", "Красота и здоровье",
               "Бытовая техника", "Спорт и отдых", "Строительство и ремонт",
               "Продукты питания", "Аптека", "Товары для животных",
               "Книги", "Туризм", "Рыбалка", "Охота", "Автотовары",
               "Мебель", "Хобби и творчество", "Ювелирные укражения",
               "Аксессуары", "Игры", "Консоли", "Канцелярские товары",
               "Товары для взрослых", "Антиквариат", "Коллекционирование",
               "Цифровые товары", "Бытовая химия", "Гигиена", "Музыка и видео",
               "Автомобили", "Квартиры"]
category_en = ["Electronics", "Clothing", "Shoes", "Home and Garden",
                "Childrens goods", "Beauty and health",
                "Household appliances", "Sports and recreation", "Construction and repair",
                "Food", "Pharmacy", "Pet products",
                "Books", "Tourism", "Fishing", "Hunting", "Automotive products",
                "Furniture", "Hobbies and creativity", "Jewelry",
                "Accessories", "Games", "Consoles", "Stationery",
                "Adult goods", "Antiques", "Collectibles",
                "Digital goods", "Household chemicals", "Hygiene", "Music and video",
                "Cars", "Apartments"]

for ru, en in zip(category_ru, category_en):
    txt += f''' ({ids},'{ru}','{en}',False),'''
    ids += 1
txt = txt[:len(txt)-1] + ';'

with codecs.open("1_category.txt", "w", "utf-16") as output:
    output.write(txt)
