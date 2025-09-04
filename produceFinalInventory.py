import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

#orden csv entrante: codigo, nombre, precio, inventario, descripcion, siniva, coniva, venta, final
#orden csv referencia: codigo, nombre
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

reference_barcodes = []
reference_names = []

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


def processing_reference_file(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            reference_barcodes.append(row[0])
            reference_names.append(row[1])

fileToProcess = filedialog.askopenfilename(
    title = "Select the CSV file to process",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)
processing_input_file(fileToProcess)

fileToReference = filedialog.askopenfilename(
    title = "Select the reference CSV file",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)
processing_reference_file(fileToReference)

for name in reference_names:
    if name not in name_list_final:
        print("Name " + name + " from reference not found in process file, adding...")
        barcode_list_final.append(reference_barcodes[reference_names.index(name)])
        name_list_final.append(name)
        price_list_final.append("0")
        inventory_list_final.append("0")
        description_list_final.append("")
        siniva_list_final.append("")
        coniva_list_final.append("")
        venta_list_final.append("")
        final_list_final.append("")
    else:
        if name in name_list_final:
            index = name_list_final.index(name)
            index_ref = reference_names.index(name)
            if barcode_list_final[index] == "": #if empty, replace
                print("Found " + name + ", barcode was empty, replacing...")
                barcode_list_final[index] = reference_barcodes[index_ref]
            else: #not empty
                if barcode_list_final[index] != reference_barcodes[index_ref]: #if different
                    print("Found " + name + ", barcode was different, replacing...")
                    barcode_list_final[index] = reference_barcodes[index_ref]
                else: #if same
                    print("Found " + name + ", barcode was the same, doing nothing...")

with open("Inventario_Final.csv", mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        for i in range(len(name_list_final)):
            writer.writerow([barcode_list_final[i], name_list_final[i], price_list_final[i], inventory_list_final[i], description_list_final[i], siniva_list_final[i] if i < len(siniva_list_final) else "", coniva_list_final[i] if i < len(coniva_list_final) else "", venta_list_final[i] if i < len(venta_list_final) else "", final_list_final[i] if i < len(final_list_final) else ""])