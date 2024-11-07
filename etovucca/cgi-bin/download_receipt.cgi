#!/usr/bin/env python3

import os
import cgi

RECEIPT_DIRECTORY = "./receipts/"

print("Content-Type: text/plain")
print("Content-Disposition: attachment; filename=receipt.txt")
print()

form = cgi.FieldStorage()
file_name = form.getvalue("file")

file_path = os.path.join(RECEIPT_DIRECTORY, file_name)

if os.path.isfile(file_path):
    with open(file_path, "rb") as file:
        binary_content = file.read()
        try:
            text_content = binary_content.decode('utf-8')
            print(text_content)
        except UnicodeDecodeError:
            print(binary_content)
else:
    print("Error: File not found.")
