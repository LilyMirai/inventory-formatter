import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

barcode_list_reference = []
name_list_reference = []

barcodes = []
ammounts = []

line_to_write = []

def processing_reference_file():
    with open(fileToReference, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            barcode_list_reference.append(row[0])
            name_list_reference.append(row[1])

def processing_file_to_process():
    with open(fileToProcess, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            barcodes.append(row[0])
            ammounts.append(row[1])

fileToProcess = filedialog.askopenfilename(
    title = "Select the CSV file to process",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

fileToReference = filedialog.askopenfilename(
    title = "Select the reference CSV file",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

processing_reference_file()
processing_file_to_process()

for barcode in barcodes:
    if barcode in barcode_list_reference:
        index = barcode_list_reference.index(barcode)
        print("Found " + barcode + " in reference as " + name_list_reference[index])
        line_to_write.append(name_list_reference[index] + "," + str(ammounts[barcodes.index(barcode)]) + "," + barcode + "\n")
    else:
        print("Barcode " + barcode + " not found in reference")

with open("Inventario_Final.csv", mode='w', newline='', encoding='utf-8') as output_file:
        for line in line_to_write:
            index = line_to_write.index(line)
            output_file.write(line_to_write[index])