#!/usr/bin/env python3

import os
import csv
import ast
from collections import OrderedDict
from datetime import datetime

#prod_file_name = 'C:/revature/domin-project0/product.csv'
#inv_file_name = 'C:/revature/domin-project0/inventory.csv'
#sale_file_name = 'C:/revature/domin-project0/sale.csv'
prod_file_name = './product.csv'
inv_file_name = './inventory.csv'
sale_file_name = './sale.csv'

#This is the main menu where the user selects what he/she wants to do
def main():
    """Main entry point of function.
    This program is a product inventory management system
    """
    more_action = True
    while more_action:
        print()
        print('*********************************')
        print('*                               *')
        print('*   Menu: 1 - Add Products      *')
        print('*         2 - List Products     *')
        print('*         3 - Add Inventory     *')
        print('*         4 - Check Inventory   *')
        print('*         5 - Enter Sales       *')
        print('*         6 - Order Products    *')
        print('*                               *')
        print('*********************************')
        print()

        prompt = 'Please enter a choice from the Menu: '
        action = input(prompt)

        if action == '1':
            add_products()
        elif action == '2':
            display_products()
        elif action == '3':
            add_inventory()
        elif action == '4':
            display_inventory()
        elif action == '5':
            enter_sales()
        
        prompt = '\nDo you want to continue? (Y/N): '
        if ((input(prompt)).upper() == 'N'):
            more_action = False


def add_products():
    """
    This function adds a product into the products database.
    The product.csv should be in the local directory relative to this program
    """
    prod_dict = {}

    #read in a CSV from storage to add existing products
    if os.path.exists(prod_file_name):
        prod_file = open(prod_file_name)
        with open(prod_file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()

    #give user option to add more products
    add_more = True
    while add_more:
        prompt = '\nPlease enter product id, product name, unit price, order price, and unit (separated by commas):\n'
        prod = input(prompt).split(',')
        prod_temp = {'prod_desc': prod[1], 'unit_price': float(prod[2]), 'order_price': float(prod[3]), 'unit': prod[4]}    #dict
        prod_dict[int(prod[0])] = str(prod_temp)    #str

        prompt = '\nDo you want to enter another product? (Y/N): '
        if input(prompt).upper() == 'N':
            add_more = False
    
    #sort the product dictionary before writing to the csv file
    prod_dict = OrderedDict(sorted(prod_dict.items()))

    #once the user has added all of the products, write products to file.
    if os.path.exists(prod_file_name):
        os.remove(prod_file_name)

    prod_file = open(prod_file_name, 'w', newline='', encoding='utf-8')

    writer = csv.writer(prod_file)
    for key, value in prod_dict.items():
        writer.writerow([key, value])
    prod_file.close()

    #print out all of the products
    print('\nList of Products:')
    print('')
    print('Prod ID\tProd Name\tUnit_Price\tOrder Price\tUnit')

    for prod_id in prod_dict:
        print(prod_id, '\t', end='')

        prod_dict_str = prod_dict[prod_id]
        prod_detail_dict = ast.literal_eval(prod_dict_str)

        for prod_col in prod_detail_dict:
            print(prod_detail_dict[prod_col], '\t', end = ' ')
        print()


def display_products():
    """
    This function lists the products.
    The product.csv should be in the local directory relative to this program
    """
    prod_dict = {}

    #read in a CSV from storage to display existing products
    if os.path.exists(prod_file_name):
        prod_file = open(prod_file_name)
        with open(prod_file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()

        #print out all of the products
        print()
        print('\nList of Products:')
        print()
        print('Prod ID\tProd Name\tUnit_Price\tOrder Price\tUnit')

        for prod_id in prod_dict:
            print(prod_id, '\t', end='')

            prod_dict_str = prod_dict[prod_id]
            prod_detail_dict = ast.literal_eval(prod_dict_str)

            for prod_col in prod_detail_dict:
                print(prod_detail_dict[prod_col], '\t', end = ' ')
            print()
    else:
        #let the user know that there are currently no products on the database
        print('\nThere are currently no products in the database\n')


def add_inventory():
    """
    This function adds items to the inventory database.
    The inventory items are stored in `inventory.csv`, which is local to the program
    """

    prod_dict = {}

    #read in a CSV from storage to display existing products
    if os.path.exists(prod_file_name):
        prod_file = open(prod_file_name)
        with open(prod_file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()
    else:
        #let the user know that there are currently no products on the database to enter inventory for
        #exit from the function
        print('\nYou cannot enter inventory because there are currently no products in the database.')
        print('Please enter first the products you want to enter inventory for.\n')
        return

    inv_dict = {}

    #reads in existing inventory items from the inventory.csv file.
    if os.path.exists(inv_file_name):
        inv_file = open(inv_file_name)
        with open(inv_file_name) as inv_file:
            csv_reader = csv.reader(inv_file, delimiter=',')
            for row in csv_reader:
                inv_dict[int(row[0])] = row[1]     #str, str
        inv_file.close()

    #Adds more inventory items based on user input.
    add_more = True
    while add_more:
        prompt = '\nPlease enter product id, stock qty, reorder level, and reorder qty (separated by commas):\n'
        inv = input(prompt).split(',')
        inv_temp = {'stock_qty': int(inv[1]), 'reorder_level': int(inv[2]), 'reorder_qty': int(inv[3])}    #dict
        inv_dict[int(inv[0])] = str(inv_temp)    #str

        prompt = '\nDo you want to enter another product inventory? (Y/N): '
        if input(prompt).upper() == 'N':
            add_more = False

    #sort the product dictionary before writing to the csv file
    inv_dict = OrderedDict(sorted(inv_dict.items()))

    #writes out the new modified inventory back into the file.
    if os.path.exists(inv_file_name):
        os.remove(inv_file_name)

    inv_file = open(inv_file_name, 'w', newline='', encoding='utf-8')

    writer = csv.writer(inv_file)
    for key, value in inv_dict.items():
        writer.writerow([key, value])
    inv_file.close()

    #outputs the inventory
    print('\nInventory of Products:\n')
    print('Prod ID\tStock Qty\tReorder Level\tReorder Qty')

    for inv_id in inv_dict:
        print(inv_id, '\t', end='')

        inv_dict_str = inv_dict[inv_id]
        inv_detail_dict = ast.literal_eval(inv_dict_str)

        for inv_col in inv_detail_dict:
            print(inv_detail_dict[inv_col], '\t', end = ' ')
        print()


def display_inventory():
    """
    This function displays the inventory.
    The inventory items are stored in `inventory.csv`, which is local to the program
    """
    prod_dict = {}

    #reads in existing inventory items from the inventory.csv file.
    if os.path.exists(inv_file_name):
        prod_file = open(inv_file_name)
        with open(inv_file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()

        #outputs the inventory
        print('\nInventory of Products:\n')
        print('Prod ID\tStock Qty\tReorder Level\tReorder Qty')

        for prod_id in prod_dict:
            print(prod_id, '\t', end='')

            prod_dict_str = prod_dict[prod_id]
            prod_detail_dict = ast.literal_eval(prod_dict_str)

            for prod_col in prod_detail_dict:
                print(prod_detail_dict[prod_col], '\t', end = ' ')
            print()
    else:
        #let the user know that there are currently no inventory for any product on the database
        print('\nThere are currently no inventory for any product in the database\n')


def enter_sales():
    """
    This function enter sales to the database.
    The sale items are stored in `sale.csv`, which is local to the program
    """

    inv_dict = {}

    #reads in existing inventory items from the inventory.csv file.
    if os.path.exists(inv_file_name):
        inv_file = open(inv_file_name)
        with open(inv_file_name) as inv_file:
            csv_reader = csv.reader(inv_file, delimiter=',')
            for row in csv_reader:
                inv_dict[int(row[0])] = row[1]     #str, str
        inv_file.close()
    else:
        #let the user know that there are currently no inventory for any product on the database
        #exit from the function
        print('\nYou cannot enter sales because there are currently no inventory for any product in the database.')
        print('Please enter first the inventory of the products you want to enter sales for.')
        return

    prod_dict = {}

    #reads in existing products from the product.csv file.
    if os.path.exists(prod_file_name):
        prod_file = open(prod_file_name)
        with open(prod_file_name) as prod_file:
            csv_reader = csv.reader(prod_file, delimiter=',')
            for row in csv_reader:
                prod_dict[int(row[0])] = row[1]     #str, str
        prod_file.close()
    else:
        #let the user know that there are currently no inventory for any product on the database
        #exit from the function
        print('\nYou cannot enter sales because there are currently no inventory for any product in the database.')
        print('Please enter first the inventory of the products you want to enter sales for.')
        return

    old_sale_dict = {}
    sale_key = 0 #read from last line of sale file
    sale_id = 0 #read from last line of sale file

    #reads in existing sale items from the sale.csv file.
    if os.path.exists(sale_file_name):
        max_key = 0
        sale_file = open(sale_file_name)
        with open(sale_file_name) as sale_file:
            csv_reader = csv.reader(sale_file, delimiter=',')
            for row in csv_reader:
                old_sale_dict[int(row[0])] = row[1]     #str, str
                temp_key = int(row[0])
                if temp_key > max_key:
                    max_key = temp_key
        sale_file.close()

        sale_key = max_key + 1

        sale_detail_str = old_sale_dict[max_key]
        sale_detail_dict = ast.literal_eval(sale_detail_str)

        sale_id = int(sale_detail_dict['sale_id']) + 1

    #Adds sale items based on user input.
    sale_dict = {}
    total_sale_amount = 0
    add_more = True
    while add_more:
        prompt = '\nPlease enter product id, and qty sold (separated by comma):\n'
        sale = input(prompt).split(',')
        prod_id = int(sale[0])
        qty = int(sale[1])

        if prod_id in prod_dict and prod_id in inv_dict:
            inv_dict_str = inv_dict[prod_id]
            inv_detail_dict = ast.literal_eval(inv_dict_str)

            stock_qty = int(inv_detail_dict.get('stock_qty', 0))
            if stock_qty >= qty:
                new_stock_qty = stock_qty - qty

                prod_dict_str = prod_dict[prod_id]
                prod_detail_dict = ast.literal_eval(prod_dict_str)

                prod_desc = prod_detail_dict.get('prod_desc', '')
                unit = prod_detail_dict.get('unit', '')
                unit_price = float(prod_detail_dict.get('unit_price', 0.0))
                extd_price = round(unit_price * qty, 2)
                trans_date = str(datetime.now())

                #Add this sale item in the sales dictionary
                sale_temp = {'sale_id': sale_id, 'prod_id': prod_id, 'prod_desc': prod_desc, 'qty': qty, 'unit': unit, \
                    'unit_price': unit_price, 'extd_price': extd_price, 'trans_date': trans_date}    #dict
                sale_dict[sale_key] = str(sale_temp)    #str

                #Update the stock qty of this product in the inventory
                inv_temp = {'stock_qty': new_stock_qty, 'reorder_level': int(inv_detail_dict['reorder_level']), \
                    'reorder_qty': int(inv_detail_dict['reorder_qty'])}    #dict
                inv_dict[prod_id] = str(inv_temp)    #str

                total_sale_amount += extd_price

                sale_key += 1
            else:
                print('\nProduct ID ' + str(prod_id) + ' only has ' + str(inv_detail_dict['stock_qty']) + ' items in stock. This sale item cannot be processed. Please adjust the sale quantity.\n')
        else:
            if not prod_id in prod_dict:
                print('\nProduct ID "' + str(prod_id) + '" is not found in the product table. This sale item cannot be processed.\n')
            elif not prod_id in inv_dict:
                print('\nProduct ID "' + str(prod_id) + '" is not found in the inventory table. This sale item cannot be processed.\n')

        prompt = '\nDo you want to enter another sale item for Sale ID ' + str(sale_id) + '? (Y/N): '
        if input(prompt).upper() == 'N':
            add_more = False

    #append the sales items back into the sale file.
    sale_file = open(sale_file_name, 'a', newline='', encoding='utf-8')

    writer = csv.writer(sale_file)
    for key, value in sale_dict.items():
        writer.writerow([key, value])
    sale_file.close()

    #sort the product dictionary before writing to the csv file
    inv_dict = OrderedDict(sorted(inv_dict.items()))

    #write out the new modified inventory back into the file.
    if os.path.exists(inv_file_name):
        os.remove(inv_file_name)

    inv_file = open(inv_file_name, 'w', newline='', encoding='utf-8')

    writer = csv.writer(inv_file)
    for key, value in inv_dict.items():
        writer.writerow([key, value])
    inv_file.close()

    #output the sales
    print('\nTransaction Date: ' + str(datetime.now()))
    print('Sales ID: ' + str(sale_id) + '\n')
    print('Prod ID\tProd Desc\tQty\tUnit\tPrice\tExtd Price')

    for sale_key in sale_dict:
        sale_dict_str = sale_dict[sale_key]
        sale_detail_dict = ast.literal_eval(sale_dict_str)

        print(sale_detail_dict['prod_id'], sale_detail_dict['prod_desc'], sale_detail_dict['qty'], \
            sale_detail_dict['unit'], sale_detail_dict['unit_price'], sale_detail_dict['extd_price'])

    print('\nTotal Sales Amount: ' + str(total_sale_amount))



if __name__ == '__main__':
    main()

