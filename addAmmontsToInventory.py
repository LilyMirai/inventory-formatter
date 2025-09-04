import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#orden csv entrante: codigo, nombre, precio, inventario, descripcion, siniva, coniva, venta, final
#orden csv inventario: codigo, inventario, nombre
#orden csv inventario final: codigo, nombre, precio, inventario, descripcion, siniva, coniva, venta, final


barcode_list_final = []
name_list_final = []
price_list_final = []
inventory_list_final = []
description_list_final = []
siniva_list_final = []
coniva_list_final = []
venta_list_final = []
final_list_final = []

barcode_inventory = []
inventory_inventory = []
name_inventory = []


def processing_input_file(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            barcode_list_final.append(row[0])
            name_list_final.append(row[1])
            price_list_final.append(row[2])
            inventory_list_final.append(row[3])
            description_list_final.append(row[4])
            siniva_list_final.append(row[5])
            coniva_list_final.append(row[6])
            venta_list_final.append(row[7])
            final_list_final.append(row[8])

def processing_inventory_file(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name_inventory.append(row[0])
            inventory_inventory.append(row[1])
            barcode_inventory.append(row[2])

fileToProcess = filedialog.askopenfilename(
    title = "Select the CSV file to process",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

fileInventory = filedialog.askopenfilename(
    title = "Select the reference CSV file",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

processing_input_file(fileToProcess)
processing_inventory_file(fileInventory)

for name in name_inventory:
    if name in name_list_final:
        index = name_list_final.index(name)
        index_inventory = name_inventory.index(name)
        print("Found " + name + " in final as " + barcode_list_final[index] + ", updating inventory from " + inventory_list_final[index] + " to " + inventory_inventory[index_inventory])
        inventory_list_final[index] = inventory_inventory[index_inventory]
    else:
        print("Name " + name + " not found in final")

with open("Inventario Final CON cantidades.csv", mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        for i in range(len(name_list_final)):
            writer.writerow([barcode_list_final[i], name_list_final[i], price_list_final[i], inventory_list_final[i], description_list_final[i], siniva_list_final[i] if i < len(siniva_list_final) else "", coniva_list_final[i] if i < len(coniva_list_final) else "", venta_list_final[i] if i < len(venta_list_final) else "", final_list_final[i] if i < len(final_list_final) else ""])