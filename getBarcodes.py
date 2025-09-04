import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

barcode_list_process = []
barcode_list_reference = []
name_list_process = []
name_list_reference = []
added = 0
final_name_list = []
final_barcode_list = []
wasemptyreplaced = 0
wasdifferent = 0
wasthesame = 0

def processing_reference_file(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            barcode_list_reference.append(row[0])
            name_list_reference.append(row[1])

def processing_file_to_process(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            barcode_list_process.append(row[0])
            name_list_process.append(row[1])

fileToProcess = filedialog.askopenfilename(
    title = "Select the CSV file to process",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

fileToReference = filedialog.askopenfilename(
    title = "Select the reference CSV file",
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
)

processing_file_to_process(fileToProcess)
processing_reference_file(fileToReference)

for name in name_list_reference:
    if name not in name_list_process:
        print("Name " + name + " from reference not found in process file, adding...")
        barcode_list_process.append(barcode_list_reference[name_list_reference.index(name)])
        name_list_process.append(name)
        added += 1

for name in name_list_process:
    print("Processing name: " + name)
    if name in name_list_reference:
        index = name_list_reference.index(name)
        index_process = name_list_process.index(name)
        if barcode_list_reference[index] == "": #if empty in reference, skip
            print("Found, was empty in reference, skipping...")
            continue
        if barcode_list_process[index_process] == "": #if empty, replace
            print("Found, was empty, replacing...")
            barcode_list_process[index_process] = barcode_list_reference[index]
            wasemptyreplaced += 1
        elif barcode_list_process[index_process] == barcode_list_reference[index]: #if same, leave alone
            print("Found, was the same, unchanged...")
            wasthesame += 1
            pass
        else: #if different, replace 
            print("Found, was different, replacing...")
            barcode_list_process[index_process] = barcode_list_reference[index]
            wasdifferent += 1
    else:
        print("Name " + name + " not found in reference")



with open("Inventario_Con_Codigos.csv", mode='w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        for i in range(len(name_list_process)):
            writer.writerow([barcode_list_process[i], name_list_process[i]])

print("Finished! Added " + str(added) + " new items.")
print("Replaced " + str(wasemptyreplaced) + " empty barcodes.")
print("Replaced " + str(wasdifferent) + " different barcodes.")
print("Left " + str(wasthesame) + " barcodes unchanged.")