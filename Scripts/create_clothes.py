"""Scipt to create clothes"""

# Utilities
import csv
import random

categories_list = ['camisa','blusa','camiseta','chaqueta', 'pantalones', 'falda', 'sombrero', 'gorra']
SIZES_LIST = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'NS']
color_list = ['amarillo', 'verde', 'rojo', 'azul', 'beige', 'naranja']
GENDER_LIST = ['F', 'M', 'U', 'NS']
brands_list = ['chevignon','americanino','rose pistol','diesel','gucci']


class Clothes:
    def __init__(self, how_many_clothes):
        self.how_many_clothes = how_many_clothes
    
    def get_description(self):
        pass
    
    def get_url_picture(self):
        pass
    
    def choice_function(self, values_list):
        value = random.choice(values_list)
        return value

    def random_nuber(self):
        pass

    def write(self):
        with open('clothes.csv', 'w') as clothes_file:
            writer = csv.writer(clothes_file)
            for i in range(self.how_many_clothes):
                category = self.choice_function(categories_list)
                size = self.choice_function(SIZES_LIST)
                color = self.choice_function(color_list)
                gender = self.choice_function(GENDER_LIST)
                brand = self.choice_function(brands_list)
                writer.writerow([
                    category,
                    size,
                    color,
                    gender,
                    brand
                ])

def run():
        how_many_clothes = int(input('¿cuantas prendas quieres crear?: '))
        create_clothe = Clothes(how_many_clothes).write
        create_clothe()
        print (f'Se han creado {how_many_clothes} prendas')
if __name__ == '__main__':
    
    try:
        run()
    except ValueError:
        print ('Error: Debe ingresar un numero entero de prendas a crear:')
        run()
