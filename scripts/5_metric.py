import codecs

txt = 'INSERT INTO metric(id, name, name_en) VALUES'
ids = 1
metric_ru = [   "т", "кг", "г", "мг", "км", "м", "дм", "см", "мм", 
                "л", "мл", "ц", "шт", "пачек", "единиц"]
metric_en = [   "t", "kg", "g", "mg", "km", "m", "dm", "cm", "mm",
                "L", "ml", "c", "pieces", "packs", "units"]
for ru, en in zip(metric_ru, metric_en):
    txt += f''' ({ids},'{ru}','{en}'),'''
    ids += 1
txt = txt[:len(txt)-1] + ';'

with codecs.open("5_metric.txt", "w", 'utf-16') as output:
    output.write(txt)
