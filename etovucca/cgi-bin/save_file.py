#!/usr/bin/env python3
import cgi
import os
from urllib.parse import unquote

UPLOAD_DIR = "./uploads/"

def save_file():
    print("Content-Type: text/html")
    print()

    form = cgi.FieldStorage()
    name = form.getvalue("name")
    county = form.getvalue("county")
    zipc = form.getvalue("zipc")
    dob = form.getvalue("dob")

    file_item = form["photo"]

    if file_item.filename:
        with open(UPLOAD_DIR+'/'+unquote(file_item.filename), "wb") as f:
            f.write(file_item.file.read())

        print(f"<b>Voter registered successfully with photo uploaded</b><br>")
    else:
        print("<b>Voter registered, but no photo was uploaded.</b><br>")

    print('<a href="./home.cgi">Return to Homepage</a>')

if __name__ == "__main__":
    save_file()
