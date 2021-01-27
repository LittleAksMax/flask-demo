# flask-demo
> $ sudo pip install flask

Can put parameters into html with {{}}, have to name the expressions and pass them in render_template()

Can run certain python in this format
``` python
{% for _ in range(1, 10)  %}
    <p> {{_}} </p>
{% endfor %}
```
But you have to end it with the appropriate end 
But you have to end it with the appropriate end (in this case *endfor*)

You can get certain tools from bootstrap, stuff to do in base.html.
Can also make base html and make everything inherit from it, you can fill it with blocks that need filling for things that need to change. Very good for no duplicate code.

You can also use get and post methods to check for form entries.
I made a login html and also a login route in app.py that redirects to the user.html with the name parameter submitted in the login page.

Creating sessions is not bad; create a permanent session time, and a secret key for storing, use the session dict for data you want to store for every user for each session, usually name.

Flashing messages is used for showing some information on the GUI about events, i.e. logged out successfully; log in successful. Just import flash and post messages. Each message is either info, warning, or error type. Also changes in base.html for getting flashed messages. Should probably change basefile but it's fine for now. Probably best integrated with javascript, how to use javascript in these applications is below:

For ep7 I started from scratch. You have to make a static directory and split it into sections - javascript, images, styles - (not necessary but best practice), you can reference these files from the html files by doing a {{ url_for('static', filename=filename.js ) }} in the html files.

A flask blueprint is a way for you to organize your flask application into smaller and re-usable application. It also gives it extra functionality, say if you want to split off the pages an admin gets against what a regular client gets. Can also go further by putting each group of files into a admin directory, and putting an empty __init__.py file in to make it work like a package

## Deployment Procedure
Step 1: Setup a server on linode

Step 2: Download Putty and SSH in

Step 3: Download and Install Apache
- sudo apt update
- sudo apt install apache2
- apache2 -version

Step 4: Configure Firewall
- sudo ufw app list
- sudo ufw allow ‘Apache’

Step 5: Configure apache
- sudo systemctl status apache 2  

Step 6: Install and enable mod_wsgi
-       sudo apt-get install libapache2-mod-wsgi python-dev

Step 7:  Creating flask app
-       cd /var/www 
-       sudo mkdir webApp
-       cd webApp

Step 8: Install flask
-        sudo apt-get install python-pip 
-        sudo pip install Flask 
-        sudo pip install flask_sqlalchemy

Step 9: Use winSCP to transfer python files to server

Step 10: configure and enable virtual host
-       sudo nano /etc/apache2/sites-available/webApp.conf

CLICK TO DOWNLOAD THE CODE TO PUT IN webApp.conf
https://techwithtim.net/wp-content/uploads/2019/11/code-to-place-in-.conf-file.txt

-      sudo a2ensite webApp 
-      systemctl reload apache2

Step 11: Create .wsgi file
-      sudo nano webapp.wsgi 
Place the below code in the wsgi file

#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/webApp/")

from webApp import app as application
application.secret_key = 'Add your secret key'

Step 12: Restart apache
-      sudo service apache2 restart 

Step 13: Visit the ip address of your server in the browser to  access your website!
