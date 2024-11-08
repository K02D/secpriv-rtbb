#!/bin/bash

render_register() {
    echo "Content-Type: text/html"
    echo ""
    echo "<link rel='stylesheet' href='https://spar.isi.jhu.edu/teaching/443/main.css'>"
    echo '<h2 id="dlobeid-etovucca-voting-machine">DLOBEID EtovUcca Voting Machine</h2><h1 id="voter-registration">Voter Registration</h1><br>'
    echo '<form enctype="multipart/form-data" action="./save_file.py" method="post">'
    echo '<label for="name">Voter Name</label><br>'
    echo '<input type="text" id="name" name="name"><br>'
    echo '<label for="county">County</label><br>'
    echo '<input type="text" id="county" name="county"><br>'
    echo '<label for="zipc">ZIP Code</label><br>'
    echo '<input type="number" id="zipc" name="zipc"><br>'
    echo '<label for="dob">Date of Birth</label><br>'
    echo '<input type="date" id="dob" name="dob"><br>'
    echo '<label for="photo">Upload Photo</label><br>'
    echo '<input type="file" id="photo" name="photo"><br>'
    echo '<input type="submit" value="Submit">'
    echo '</form>'
    echo '<a href="./home.cgi">Return to Homepage</a><br>'
}

render_register 