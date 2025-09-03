# Inventory Formatter
Utilities to make the inventory process of a store easier.

Use count.py to convert a CSV or TXT file that contains a list of unorganized, repeated barcodes and turn them into a single instance per barcode plus the ammount of times it was present in a CSV format.

Use compare.py to compare that resulting CSV file with another that has barcodes and names/codes to assign to them, it will return "Inventario_Final.csv" with the structure "Name, Ammount, Barcode".
