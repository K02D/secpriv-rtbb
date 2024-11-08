#!/usr/bin/env python3
import cgi
import os
import subprocess
from urllib.parse import unquote, quote_plus

UPLOAD_DIR = "./uploads/"
PATH_TO_MACHINE = "./etovucca"

def save_file():
    print("Content-Type: text/html")
    print()

    form = cgi.FieldStorage()
    name = quote_plus(form.getvalue("name"))
    county = form.getvalue("county")
    zipc = form.getvalue("zipc")
    dob = form.getvalue("dob")
    file_item = form["photo"]
    if file_item.filename:
        with open(UPLOAD_DIR + '/' + unquote(file_item.filename), "wb") as f:
            f.write(file_item.file.read())
        photo_status = "Photo uploaded successfully."
    else:
        photo_status = "No photo was uploaded."
    try:
        name_check = subprocess.run(['./name_helper.py', name], 
                                  capture_output=True, 
                                  text=True)
        
        if name_check.returncode != 0 or not name_check.stdout.strip():
            print("<div>Error in registering voter, invalid name. Please try again.</div>")
            return

        result = subprocess.run([PATH_TO_MACHINE, 'add-voter', name, county, zipc, dob],
                              capture_output=True,
                              text=True)
        
        voter_id = result.stdout.strip()
        if voter_id and voter_id != "0":
            print(f"<div>{name_check.stdout} Your ID is: {voter_id}</div>")
            print(f"<div>{photo_status}</div>")
        else:
            print("<div>Error in registering voter. Please try again.</div>")
            
    except Exception as e:
        print(f"<div>Error during registration: {str(e)}</div>")

    print('<br><a href="./home.cgi">Return to Homepage</a>')

if __name__ == "__main__":
    save_file()