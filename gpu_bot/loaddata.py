""" use 'https://github.com/Chinmay-395/dynamic_filter/blob/master/src/loaddata.py'
    for reference.
    Run this in django shell
"""
from gpuApi.models import Product
import csv

product_csv = open('ProjectGpu-withoutID.csv', 'r', encoding="utf-8")
reader = csv.reader(product_csv)
headers = next(reader, None)[1:]

for row in reader:
    product_dict = {}
    for h, val in zip(headers, row[1:]):
        product_dict[h] = val
    wine = Product.objects.create(**product_dict)

product_csv.close()
