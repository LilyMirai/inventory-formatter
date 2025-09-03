import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

fileToProcess = filedialog.askopenfilename(
    title = "Select the CSV file to process",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

with open(fileToProcess, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    barcodes = [row[0] for row in reader if row]  # Assuming barcodes are in the first column

def countInstances(barcodes):
    barcode_list = []
    ammount_list = []

    for barcode in barcodes:
        if barcode in barcode_list:
            print("Barcode already in list, adding to: " + barcode)
            index = barcode_list.index(barcode)
            ammount_list[index] += 1
        else:
            print("New barcode, adding to list: " + barcode)
            barcode_list.append(barcode)
            ammount_list.append(1)
    
    with open("output.csv", mode='w', newline='', encoding='utf-8') as output_file:
        for barcode in barcode_list:
            index = barcode_list.index(barcode)
            output_file.write(barcode_list[index] + "," + str(ammount_list[index]) + "\n")
        
countInstances(barcodes)