#!/usr/bin/env python

import os
import csv
import ast


# this is the main menu where the user selects what he wants to do
def main():
    print('*********************************')
    print('*                               *')
    print('*   Menu: 1 - Add Products      *')
    print('*         2 - List Products     *')
    print('*         3 - Add Inventory     *')
    print('*         4 - Check Inventory   *')
    print('*         5 - Order Products    *')
    print('*         6 - Enter Sales       *')
    print('*                               *')
    print('*********************************')
    print('')
    prompt = 'Please enter a choice from the Menu: '
    action = input(prompt)

    if action == '1':
        add_product()
    elif action == '3':
        add_inventory()


def add_product():
    prod_dict = {}

    file_name = 'E:/Buds Files/Work Files/Revature/Training/Exercises/Python/Project0/product.csv'
    if os.path.exists(file_name):
        prod_file = open(file_name)
        with open(file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()

    add_more = True
    while add_more:
        prompt = 'Please enter product id, product name, unit price, order price, and unit (separated by commas):\n'
        prod = input(prompt).split(',')
        prod_temp = {'prod_desc': prod[1], 'unit_price': float(prod[2]), 'order_price': float(prod[3]), 'unit': prod[4]}    #dict
        prod_dict[int(prod[0])] = str(prod_temp)    #str

        prompt = 'Do you want to enter another product? (Y/N): '
        if input(prompt).upper() == 'N':
            add_more = False

    if os.path.exists(file_name):
        os.remove(file_name)

    prod_file = open(file_name, 'w', newline='', encoding='utf-8')

    writer = csv.writer(prod_file)
    for key, value in prod_dict.items():
        writer.writerow([key, value])
    prod_file.close()

    print('List of Products:')
    print('')
    print('Prod ID\tProd Name\tUnit_Price\tOrder Price\tUnit')

    for prod_id in prod_dict:
        print(prod_id, '\t', end='')

        prod_dict_str = prod_dict[prod_id]
        prod_detail_dict = ast.literal_eval(prod_dict_str)

        for prod_col in prod_detail_dict:
            print(prod_detail_dict[prod_col], '\t', end = ' ')
        print()


def add_inventory():
    prod_dict = {}

    file_name = 'E:/Buds Files/Work Files/Revature/Training/Exercises/Python/Project0/inventory.csv'
    if os.path.exists(file_name):
        prod_file = open(file_name)
        with open(file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()

    add_more = True
    while add_more:
        prompt = 'Please enter product id, stock qty, reorder level, and reorder qty (separated by commas):\n'
        prod = input(prompt).split(',')
        prod_temp = {'stock_qty': int(prod[1]), 'reorder_level': int(prod[2]), 'reorder_qty': int(prod[3])}    #dict
        prod_dict[int(prod[0])] = str(prod_temp)    #str

        prompt = 'Do you want to enter another product inventory? (Y/N): '
        if input(prompt).upper() == 'N':
            add_more = False

    if os.path.exists(file_name):
        os.remove(file_name)

    prod_file = open(file_name, 'w', newline='', encoding='utf-8')

    writer = csv.writer(prod_file)
    for key, value in prod_dict.items():
        writer.writerow([key, value])
    prod_file.close()

    print('Inventory of Products:')
    print('')
    print('Prod ID\tStock Qty\tReorder Level\tReorder Qty')

    for prod_id in prod_dict:
        print(prod_id, '\t', end='')

        prod_dict_str = prod_dict[prod_id]
        prod_detail_dict = ast.literal_eval(prod_dict_str)

        for prod_col in prod_detail_dict:
            print(prod_detail_dict[prod_col], '\t', end = ' ')
        print()





if __name__ == '__main__':
    main()

