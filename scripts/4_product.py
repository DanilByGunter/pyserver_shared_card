import codecs
import random

txt = 'INSERT INTO product(id, name, name_en, id_category, fat, protein, carb) VALUES'
ids = 1

cat = 45
n = cat*10
for i in range(1, n): 
    txt += f''' ({ids},'Продукт{i}','Product{i}','{cat}',{random.randint(0, 40)},{random.randint(0, 40)},{random.randint(0, 40)}),'''
    ids += 1
    if i%10==0:
        cat -= 1

txt = txt[:len(txt)-1] + ';'

with codecs.open("4_product.txt", "w", "utf-16") as output:
    output.write(txt)
