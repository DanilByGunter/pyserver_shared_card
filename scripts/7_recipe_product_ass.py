import codecs
import random, string
import uuid
from datetime import datetime
import faker
f = faker.Faker()

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for _ in range(length))

txt = 'INSERT INTO "recipe_product_association"(id_product, id_recipe, id_metric, count) VALUES'
n = 100

for pos in range(1, n):
    k = random.randint(0, 10)
    products = set()
    for _ in range(k):
        products.add(random.randint(1, 449))
    products = list(products)
    for x in range(len(products)):
        txt += f'''({products[x]},{pos},{random.randint(1, 15)},{random.randint(1, 20)}),'''
txt = txt[:len(txt)-1] + ';'

with codecs.open("7_recipe_product_association.txt", "w", "utf-16") as output:
    output.write(txt)